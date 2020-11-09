from django.shortcuts import render
from django.http import JsonResponse
from .forms import buyNowForm
from .forms import friendForm
from .models import buyNow, friend
from gameMatchResult.models import singleGameMatchResult
from users.models import Profile
from django.db.models import Q
from django.http import HttpResponse
from .models import adWatch
from tournament.models import tournament, registration, tournamentMatch
# Create your views here.

def home(request):
    return render(request, 'game/home.html')

def shop(request):
    return render(request, 'game/shop.html')

def stats(request):
    return render(request, 'game/stats.html')

def ads(request):
    return render(request, 'game/ads.html')

def watchingAds(request):

    if request.method == "POST":
        userName = str(Profile.objects.get(user = request.user).user)
        adWatch.objects.create(
            name = userName
        )
    return HttpResponse('')

def getMatchResults(request):
    userName = str(Profile.objects.get(user = request.user).user)
    matchHistory = singleGameMatchResult.objects.filter( Q(winner=request.user) | Q(loser=request.user))
    matchHistoryArray = []
    for match in matchHistory:
        if match.winner == userName:
            opponent = match.loser
        else:
            opponent = match.winner
        entry = {
            "wager": match.pointsWagered,
            "opponent": str(opponent),
            "winner": str(match.winner),
            "date": match.date,
            "game": match.game,
            "modelName": "singleGameMatchHistory"
        }
        matchHistoryArray.append(entry)
    data = {
        "matchHistory": matchHistoryArray,
    }
    return JsonResponse(data)

def getData(request):
    winsCount = singleGameMatchResult.objects.filter(winner=request.user).count()
    lossCount = singleGameMatchResult.objects.filter(loser=request.user).count()
    gamesPlayed = winsCount + lossCount
    userName = str(Profile.objects.get(user = request.user).user)
    matchHistory = singleGameMatchResult.objects.filter( Q(winner=request.user) | Q(loser=request.user))
    maddenCount = singleGameMatchResult.objects.filter(game = "madden").count()
    valorantCount = singleGameMatchResult.objects.filter(game = "valorant").count()
    nbaCount = singleGameMatchResult.objects.filter(game = "nba2k21").count()
    fifaCount = singleGameMatchResult.objects.filter(game = "fifa21").count()
    nhlCount = singleGameMatchResult.objects.filter(game = "nhl21").count()
    i = 0
    matchHistoryArray = []
    while(i < gamesPlayed):
        if matchHistory[i].winner == userName:
            opponent = matchHistory[i].loser
        else:
            opponent = matchHistory[i].winner
        
        entry = {
            "wager": matchHistory[i].pointsWagered,
            "opponent": str(opponent),
            "winner": str(matchHistory[i].winner),
            "date": matchHistory[i].date,
            "game": matchHistory[i].game,
            "modelName": "singleGameMatchHistory"
        }
        matchHistoryArray.append(entry)
        i = i + 1 
    i = 0
    websiteObjects = matchHistoryArray
    ggPoints = []
    buyNowArray = buyNow.objects.filter(username = userName)
    adWatchArray = adWatch.objects.filter(username = userName)
    i = 0
    while i < adWatchArray.count():
        adWatchObject = {
            "date": adWatchArray[i].date,
            "modelName":adWatchArray[i].modelName
        }
        websiteObjects.append(adWatchObject)
        i = i + 1 
    i = 0
    while i < buyNowArray.count():
        price = 0
        if buyNowArray[i].item == "Ps4":
            price = 99000
        elif buyNowArray[i].item == "Ps4_Controller":
            price = 10000
        elif buyNowArray[i].item == "Xbox":
            price = 99000
        elif buyNowArray[i].item == "Xbox_Controller":
            price = 99000
        elif buyNowArray[i].item == "Madden":
            price = 99000
        elif buyNowArray[i].item == "Nba2k21":
            price = 99000
        elif buyNowArray[i].item == "Gaming_Monitor":
            price = 99000
        elif buyNowArray[i].item == "Gaming_Headset":
            price = 99000
        else:
            price = 0

        buyNowObject = {
            "price": price,
            "date": buyNowArray[i].date,
            "modelName": buyNowArray[i].modelName
        }
        websiteObjects.append(buyNowObject)
        i = i + 1
    i = 0
    ggPointsObjects = sorted(websiteObjects, key=lambda k: k['date']) 
    ggPoints = [500000]
    amount = 0
    while i < len(ggPointsObjects) :
        if ggPointsObjects[i]["modelName"]== "singleGameMatchHistory":
            if ggPointsObjects[i]["winner"] == userName:
                amount = ggPoints[i] + ggPointsObjects[i]["wager"]
            else:
                amount = ggPoints[i] - ggPointsObjects[i]["wager"]
        elif ggPointsObjects[i]["modelName"] == "adWatch":
            amount = ggPoints[i] + 100
        elif ggPointsObjects[i]["modelName"] == "buyNow":
            amount = ggPoints[i] - ggPointsObjects[i]["price"]
        ggPoints.append(amount)
        i = i + 1 


    data = {
        "username": userName, 
        "wins": winsCount,
        "losses": lossCount,
        "gamesPlayed": gamesPlayed,
        "ggPoints": ggPoints,
        "matchHistory": matchHistoryArray,
        "madden": maddenCount, 
        "valorant": valorantCount,
        "nba2k21": nbaCount, 
        "fifa21": fifaCount,
        "nhl21": nhlCount
    }

    return JsonResponse(data)

def buy_view(request):
    form = buyNowForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
    }
    return render(request, 'users/buy.html', context)
  
def dashboard(request):
    registrations = registration.objects.filter(player=request.user)
    tournaments = []
    for t in registrations:
        tournaments += tournament.objects.filter(id=t.id)
    context = {
        "tournament": tournaments,
        "registration": registrations,
    }    
    return render(request, 'game/dashboard.html', context)

def myTournaments(request):
    tournaments = tournament.objects.filter(creator=request.user)
    context = {
        "tournament": tournaments
    }
    return render(request, 'game/myTournaments.html', context)
  
def profile(request):
    if request.method == "POST" and "profileButton" in request.POST:
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip_code = request.POST.get("zip_code")
        bio = request.POST.get("bio")
        avatar = request.POST.get("avatar")
        youtube = request.POST.get("youtube")
        facebook = request.POST.get("facebook")
        steam = request.POST.get("steam")
        request.user.first_name = firstname
        request.user.last_name = lastname
        request.user.profile.address = address
        request.user.profile.city = city
        request.user.profile.state = state
        request.user.profile.zip_code = zip_code
        request.user.profile.bio = bio
        request.user.profile.avatar_url = avatar
        request.user.profile.youtube_url = youtube
        request.user.profile.steam_url = steam
        request.user.profile.facebook_url = facebook
        request.user.save()
        request.user.profile.save()
    elif request.method == "POST" and "friendButton" in request.POST:
        friendData = friend(requester=request.user)
        form = friendForm(request.POST, instance=friendData)
        if form.is_valid():
            form.save()
    form = friendForm()

    userName = str(Profile.objects.get(user = request.user).user)
    pendingRequests = friend.objects.filter(requester=request.user)

    context = {
        'form': form,
        'requests' : pendingRequests,
    }

    return render(request, 'game/profile.html', context)
    
def bracket(request):
    return render(request, 'game/bracket.html')
