from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist
# Create your views here.

def index(request):
#    context = {
#        "title":"Welcome, This is the index page.",
#    }
   return render(request, 'index.html')#, context

def home(request):
    return render(request,"home.html")

def aboutus(request):
    return render(request, "aboutus.html")

def contact(request):
    return render(request, "contact.html")

# Dynamically fetching data from model/database and displaying using GET method
def task(request):
    task=Todolist.objects.all()
    context = {
        'tasks':task
    }
    return render(request, 'task.html', context)
# create dynamic html pages for all