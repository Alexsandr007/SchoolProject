from django import forms
from .models import Teacher, School


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))


class TeacherCreationForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    school = forms.ModelChoiceField(label='School', queryset=School.objects.all(), empty_label='Select School',
                                    widget=forms.Select(attrs={'class': 'form-control', 'style': 'color:black;'}))

    class Meta:
        model = Teacher
        fields = ['username', 'email', 'password', 'school']
