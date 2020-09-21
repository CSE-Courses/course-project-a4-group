from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def gameMatchResult(request):
    return HttpResponse('<h1>Game Match Result</h1>')
