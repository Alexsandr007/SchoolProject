from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm, TeacherCreationForm
from django.contrib.auth.models import User
from .models import Teacher


def login_teacher(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register_teacher(request):
    if request.method == 'POST':
        form = TeacherCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            school = form.cleaned_data['school']
            teacher = Teacher(username=username, email=email, school=school)
            teacher.set_password(password)  # Устанавливаем пароль с использованием метода set_password
            teacher.save()
            return redirect('home')  # Перенаправляем на страницу успешной регистрации
    else:
        form = TeacherCreationForm()

    return render(request, 'register.html', {'form': form})
