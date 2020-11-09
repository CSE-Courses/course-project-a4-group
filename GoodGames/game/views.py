from django.shortcuts import render
from django.http import JsonResponse
from .forms import buyNowForm
from .models import buyNow
from gameMatchResult.models import singleGameMatchResult
from users.models import Profile
from django.db.models import Q
from django.http import HttpResponse
from .models import adWatch
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
    ggPoints = [100000]
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
    return render(request, 'game/dashboard.html')
  
def profile(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip_code = request.POST.get("zip_code")
        bio = request.POST.get("bio")
        request.user.first_name = firstname
        request.user.last_name = lastname
        request.user.profile.address = address
        request.user.profile.city = city
        request.user.profile.state = state
        request.user.profile.zip_code = zip_code
        request.user.profile.bio = bio
        request.user.save()
        request.user.profile.save()

    return render(request, 'game/profile.html')
    
def bracket(request):
    return render(request, 'game/bracket.html')
