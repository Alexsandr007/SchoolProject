from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, TeacherCreationForm
from django.contrib.auth.models import User
from .models import Teacher


def authorization(request):
    if request.method == 'POST':
        form_id = request.POST.get('form_id')
        if form_id == 'login':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = Teacher.objects.authenticate(request, username=username, password=password)
                print(user)
                if user:
                    # Аутентификация прошла успешно
                    return redirect('home')
                else:
                    # Неверные учетные данные
                    return HttpResponse("Invalid username or password")
            return render(request, 'login.html')
        elif form_id == 'register':
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
                return HttpResponse("Method not valid")
        else:
            return HttpResponse("Method not register or login")
    else:
        login_form = LoginForm()
        register_form = TeacherCreationForm()
        return render(request, 'login.html', {'login_form': login_form,'register_form': register_form})


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
