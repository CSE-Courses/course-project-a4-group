from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import buyNowForm
from .models import buyNow

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def buy_view(request):
    form = buyNowForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'users/buy.html', context)
    

