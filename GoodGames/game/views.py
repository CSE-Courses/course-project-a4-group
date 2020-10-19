from django.shortcuts import render
from django.http import JsonResponse
from .forms import buyNowForm
from .models import buyNow
# Create your views here.

def home(request):
    return render(request, 'game/home.html')

def shop(request):
    return render(request, 'game/shop.html')

def stats(request):
    return render(request, 'game/stats.html')
  
def getData(request):
    data = {
        "username": 'Kshutty', 
        "wins": 87,
        "losses": 53,
        "gamesPlayed": 140,
        "ggPoints": [300000, 230000, 140000, 180000, 110000, 160000, 250000, 350000],
        "matchHistory":[{
            "wager": 10000, 
            "opponent": "flyGuy",
            "winner": "kshutty",
            "game": "Madden"
        }, {
            "wager": 20000, 
            "opponent": "UBman",
            "winner": "kshutty",
            "game": "valorant"
        },{
            "wager": 30000, 
            "opponent": "billyBuffalo",
            "winner": "billyBuffalo",
            "game": "NBA2k21"
        },{
            "wager": 20000, 
            "opponent": "bulldog",
            "winner": "kshutty",
            "game": "Madden"
        },{
            "wager": 15000, 
            "opponent": "eliteGamer",
            "winner": "eliteGamer",
            "game": "valorant"
        }],
        "madden": 19, 
        "valorant": 11,
        "nba2k21": 5, 
        "fifa21": 8,
        "nhl21": 15
    }
    return JsonResponse(data)

def buy_view(request):
    form = buyNowForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
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

