from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import singleGameMatchResultForm
from .models import singleGameMatchResult
# Create your views here.

def gameMatchResult(request):
    if request.method == 'POST':
        form = singleGameMatchResultForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully submitted your game match result!')
            return redirect('gameMatchResult-form')
    else:
        form = singleGameMatchResultForm()
    context = {
        'form': form
    }
    return render(request, 'gameMatchResult/gameMatchResult.html', context)
