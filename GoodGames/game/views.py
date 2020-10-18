from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'game/home.html')
def shop(request):
    return render(request, 'game/shop.html')
def dashboard(request):
    return render(request, 'game/dashboard.html')
