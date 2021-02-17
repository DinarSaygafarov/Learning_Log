'''Определяет схемы URL для пользователей'''
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from .import views

app_name = 'users'
urlpatterns = [
    # Страница входа
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Страница выхода
    path('logout/', LogoutView.as_view(template_name='learning_logs/index.html'), name='logout'),
]