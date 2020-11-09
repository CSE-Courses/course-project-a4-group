from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def gameMatchResult(request):
    return render(request, 'gameMatchResult/gameMatchResult.html')
