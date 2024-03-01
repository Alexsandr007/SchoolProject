from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm, UserCreationForm
from django.contrib.auth.models import User



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')  # Замените 'home' на URL вашей домашней страницы
                else:
                    return render(request, 'login.html', {'error_message': 'Ваш аккаунт заблокирован'})
            else:
                return render(request, 'login.html', {'error_message': 'Неверное имя пользователя или пароль'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create(username=username, email=email, password=password)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})