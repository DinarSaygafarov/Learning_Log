'''Определяет схемы URL для learning_logs'''
from django.conf.urls import url
from .import views

app_name = 'learning_logs.urls'
urlpatterns = [
    # Домашняя страница
    url(r'^$', views.index, name='index'),
    # Вывод всех тем
    url(r'^topics/$', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]