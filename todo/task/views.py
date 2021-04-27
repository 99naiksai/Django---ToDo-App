from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from . models import Task
from . forms import TaskForm
# Create your views here.
def index(request):
    task = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            form = TaskForm()
        else:
            form = TaskForm()
    return render(request , 'task/list.html' , {'form':form , 'task':task})
    
def updateTask(request ,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
            form = TaskForm()
        else:
            form = TaskForm()
    return render(request , 'task/update_task.html' , {'form':form})

def deleteTask(request , pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return HttpResponseRedirect('/')
        
    return render(request , 'task/delete.html' , {'item':item})
