#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Django Project!!'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    username = 'CrozzDev'
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {
        'projects' : projects
    })

def tasks(request):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        'tasks' : tasks
    })

def create_task(request):
    if request.method == "GET":
        #show interface
        return render(request, 'create_task.html', {
            'form' : CreateNewTask()
        })
    else:
        #save data
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('/tasks/')
    
def create_project(request):
    if request.method == "GET":
        #show interface
        return render(request, 'create_project.html', {
            'form' : CreateNewProject()
        })
    else:
        #save data
        Project.objects.create(name=request.POST['name'])
        return redirect('/projects/')
    




