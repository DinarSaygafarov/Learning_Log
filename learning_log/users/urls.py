'''Определяет схемы URL для пользователей'''
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path
from .import views

app_name = 'users'
urlpatterns = [
    # Страницы входа
    # url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
]