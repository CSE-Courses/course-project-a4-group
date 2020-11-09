from django.shortcuts import render, redirect
from .models import tournament as t_db
from .models import registration
from .forms import NewTournamentForm
from django.contrib import messages

# Create your views here.

def tournament(request, tid=0):
    if request.method == 'POST':
        tm = t_db.objects.get(id=tid)
        reg = registration(player=request.user, tournament=tm)
        reg.save()

    tournament = t_db.objects.get(id=tid)

    regs = registration.objects.filter(tournament=tid)

    context = {
        'tournament': tournament,
        'regs': regs
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
