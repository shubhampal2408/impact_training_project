# todo/views.py

from django.shortcuts import render, redirect,get_object_or_404
from .models import Todo
from .forms import TodoForm

# View to display the todo list
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

# View to add a new task
def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})

# View to mark a task as completed
def mark_completed(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

# View to delete a task
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todo_list')

# unmark the task
def unmark_completed(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = False
    todo.save()
    return redirect('todo_list')
