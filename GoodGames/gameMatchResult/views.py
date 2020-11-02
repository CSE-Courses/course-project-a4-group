from django.shortcuts import render
from django.http import HttpResponse
from .forms import singleGameMatchResultForm
from .models import singleGameMatchResult
# Create your views here.

def gameMatchResult(request):
    form = singleGameMatchResultForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'gameMatchResult/gameMatchResult.html', context)
