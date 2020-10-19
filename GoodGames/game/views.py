from django.shortcuts import render
from .forms import buyNowForm
from .models import buyNow

# Create your views here.

def home(request):
    return render(request, 'game/home.html')

def shop(request):
    return render(request, 'game/shop.html')

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
    return render(request, 'game/profile.html')

