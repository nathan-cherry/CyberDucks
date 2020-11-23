from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Authentication
@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'accounts/index.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account Created Successfully')

            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


# Tasks
@login_required(login_url='login')
def tasks(request):
    tasks_list = Task.objects.filter(assigned_to__exact=request.user)
    new_tasks = tasks_list.filter(status__exact='NEW').count()
    open_tasks = tasks_list.filter(status__exact='OPN').count()
    completed_tasks = tasks_list.filter(status__exact='COM').count()
    suspended_tasks = tasks_list.filter(status__exact='SUS').count()

    context = {
        'tasks': tasks_list,
        'new': new_tasks,
        'open': open_tasks,
        'completed': completed_tasks,
        'suspended': suspended_tasks,
    }
    return render(request, 'accounts/tasks.html', context)


@login_required(login_url='login')
def task(request, task_id):
    form = NoteForm()
    task_obj = Task.objects.get(id__exact=task_id)
    notes = Note.objects.filter(task__exact=task_obj)

    context = {
        'task': task_obj,
        'notes': notes,
        'form': form,
    }
    if request.user == task_obj.assigned_to:
        return render(request, 'accounts/task.html', context)
    else:
        return render(request, 'accounts/error')


@login_required(login_url='login')
def createTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            submit = form.save(commit=False)
            submit.assigned_to = request.user
            submit.save()
            return redirect('/tasks/')

    context ={
        'form': form,
    }
    return render(request, 'accounts/forms/task.html', context)


@login_required(login_url='login')
def updateTask(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    notes = Note.objects.filter(task__exact=task_obj)
    form = TaskForm(instance=task_obj)
    context ={
        'form': form,
        'id': task_id,
        'notes': notes,
        'task': task_obj
    }
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task_obj)
        if form.is_valid():
            submit = form.save(commit=False)
            # Don't need to reassign the user
            # submit.assigned_to = request.user
            submit.save()
            return redirect('/tasks/' + task_id)
    return render(request, 'accounts/forms/task_update.html', context)


@login_required(login_url='login')
def deleteTask(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if request.method == "POST":
        task_obj.delete()
        return redirect('/tasks/')
    context ={
        'task': task_obj
    }
    return render(request, 'accounts/forms/task.html', context)


# Notes
@login_required(login_url='login')
def deleteNote(request, note_id):
    note_obj = Note.objects.get(id=note_id)
    task_id = str(note_obj.task.id)
    if request.method == "POST":
        note_obj.delete()
    return redirect('/tasks/' + task_id)


@login_required(login_url='login')
def createNote(request, task_id):

    form = NoteForm()
    task_obj = Task.objects.get(id__exact=task_id)
    notes = Note.objects.filter(task__exact=task_obj)

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            submit = form.save(commit=False)
            submit.creator = request.user
            submit.task = task_obj
            submit.save()
            return redirect('/tasks/' + task_id)

    context = {
        'form': form,
        'notes': notes,
        'task': task_obj,
    }
    return render(request, 'accounts/task.html', context)
