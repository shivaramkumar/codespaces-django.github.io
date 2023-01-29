# urls.py
from django.urls import path
from .views import index, complete_todo, add_todo

urlpatterns = [
    path('', index, name='index'),
    path('complete/<int:todo_id>', complete_todo, name='complete_todo'),
    path('add', add_todo, name='add_todo')
]
