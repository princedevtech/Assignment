# tasks/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib.auth import login, authenticate

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view_tasks')  # Redirect to tasks page
        else:
            # Invalid login
            return render(request, 'tasks/login.html', {'error': 'Invalid credentials'})
    return render(request, 'tasks/login.html')
# View for displaying all tasks
def view_tasks(request):
    tasks = Task.objects.all()  # Fetch all tasks from the database
    return render(request, 'tasks/view_tasks.html', {'tasks': tasks})

# Add a new task
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_tasks')  # Redirect to the view_tasks page after adding
    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {'form': form})

# Mark task as complete
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('view_tasks')  # Redirect back to the task list after marking as complete
