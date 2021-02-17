from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.

def index(request):
    '''Домашняя страница приложения Learning Log'''
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    '''Выводит список тем'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    '''Выводит одну тему и все ее записи'''
    topic = Topic.objects.get(id=topic_id)
    # Проверка, что тема принаджелижт пользователю
    if topic.owner !=request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    '''Определяет новую форму'''
    if request.method != 'POST':
        '''Данные не отправились.Создается пустая форма'''
        form = TopicForm()
    else:
        '''Отправлены данные POST. Обработать данные'''
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
        return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    '''Добавляет новую запись по конкретной теме'''
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        '''Данные не отправлялись, создается пустая форма'''
        form = EntryForm()
    else:
        '''Отправленны данные POST. Обработать данные'''
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
        return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    '''Редактирует существующую запись'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner !=request.user:
        raise Http404
    if request.method != 'POST':
        # Исходный запрос. форма заполняется данными текущей записи
        form = EntryForm(instance=entry)
    else:
        # Отправка данных POST. обработоать данные
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
