# views.py
from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def add_todo(request):
    text = request.POST['text']
    Todo.objects.create(text=text)
    return redirect('index')