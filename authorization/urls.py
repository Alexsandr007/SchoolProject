from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_teacher, name='login'),
    path('register/', views.register_teacher, name='register'),
]
