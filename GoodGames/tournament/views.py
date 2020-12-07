from django.shortcuts import render, redirect
from .models import tournament as t_db
from .models import registration
from .models import tournamentMatch
from .forms import NewTournamentForm
from users.models import Profile
from django.contrib import messages
from underscore import _
from django.core import serializers
import json

# Create your views here.

def updateScore(request, id=0):
    match = tournamentMatch.objects.get(pk=id)
    if request.method == 'POST':
        if match.tourn_id.completed:
            messages.warning(request, 'This tournament is already completed!')
            return redirect('tournamentView', tid=match.tourn_id.id)
        win_id = int(request.POST.get('winner'))
        win = registration.objects.get(pk=win_id)
        match.winner = win
        match.save()
        if match.nextGame:
            next = tournamentMatch.objects.get(tourn_id=match.tourn_id, bracketNo=match.nextGame)
            if next.p1 is None:
                next.p1 = win
            elif next.p2 is None:
                next.p2 = win
            else:
                messages.warning(request, 'Winners already selected!')
                return redirect('tournamentView', tid=match.tourn_id.id)
            next.save()
        else:
            match.tourn_id.winner = win.player
            match.tourn_id.completed = True
            match.tourn_id.save()
        return redirect('tournamentView', tid=match.tourn_id.id)
    

    context = {
        'match': match,
    }
    return render(request, 'tournament/updateScore.html', context)

def tournament(request, tid=0):
    tm = t_db.objects.get(id=tid)
    regs = registration.objects.filter(tournament=tid)
    matches = tournamentMatch.objects.filter(tourn_id=tid)
    if request.method == 'POST' and 'register' in request.POST:
        reg = registration(player=request.user, tournament=tm)
        reg.save()

        

    if request.method == "POST" and 'start' in request.POST:
        if regs.count() != tm.no_of_players:
            messages.warning(request, 'Incorrect number of players registered!')
            return redirect(str(tid))
        tm.started = True
        tm.save()
        startBracket(regs, tm.no_of_players, tm)


    jsons = serializers.serialize('json', matches)

    users = {}

    for reg in regs:
        users[reg.id] = reg.player.username

    users = json.dumps(users)

    print(users)

    context = {
        'tournament': tm,
        'regs': regs,
        'matches': jsons,
        'users': users
    }
    
    return render(request, 'tournament/tournament.html', context)

def new(request):
    if request.method == 'POST':
        tournament = t_db(creator=request.user)
        form = NewTournamentForm(request.POST, instance=tournament)
        if form.is_valid():            
            form.save()
            messages.success(request, 'You have successfully created a new tournament!')
            return redirect('dashboard')
    else:
        form = NewTournamentForm()
    context = {
        'form': form
    }
    return render(request, 'tournament/new.html', context)

def startBracket(regs, base, tm):
    knownBrackets = [2, 4, 8, 16, 32]
    bracketCount = 0
    teams = _.shuffle(list(regs))
    closest = _.find(knownBrackets, lambda k, *a: k >= base)
    byes = closest - base

    if byes > 0:
        base = closest

    brackets = []
    rounds = 1
    baseT = base / 2
    baseC = base / 2
    teamMark = 0
    nextInc = base / 2

    print(teams[1])

    for i in range(1, base):
        print(teamMark)
        baseR = i / baseT
        isBye = False

        if byes > 0 and (i % 2 != 0 or byes >= baseT - i):
            isBye = True
            byes - 1
        last = _.map(_.filter(brackets, lambda b, *a: b['nextGame'] == i), lambda c, *a: { 'game': c['bracketNo']})
        brackets.append({
            'lastGames': None if rounds == 1 else [last[0]['game'], last[1]['game']],
            'nextGame': None if nextInc + i > base - 1 else nextInc + i,
            'p1': teams[teamMark] if rounds == 1 else None,
            'p2': teams[teamMark + 1] if rounds == 1 else None,
            'bracketNo': i,
            'roundNo': rounds,
            'bye': isBye,
        })

        teamMark += 2
        if i % 2 != 0:
            nextInc -= 1

        while baseR >= 1:
            rounds += 1
            baseC /= 2
            baseT = baseT + baseC
            baseR = i / baseT
        
    for match in brackets:
        match = tournamentMatch(tourn_id=tm, p1=match['p1'], p2=match['p2'], roundNo=match['roundNo'], bye=match['bye'], lastGames=match['lastGames'], nextGame=match['nextGame'], bracketNo=match['bracketNo'])
        match.save()
    return brackets
