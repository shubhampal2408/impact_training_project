# todoproject/urls.py

from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('mark_completed/<int:pk>/', views.mark_completed, name='mark_completed'),
    path('unmark_completed/<int:pk>/', views.unmark_completed, name='unmark_completed'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
]
