from django.shortcuts import render, redirect
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

def create_task(request):
    if request.method=='POST':
        titles=request.POST.get("title")
        descriptions=request.POST.get("description")
        if titles=="" or descriptions =="":
            context={
                "error":"both field are required."
            }
            return render (request, "create.html",context)
        # tala ko left ma vako title ra description chai model ko ho and right ko chai yeta mathi def gareko
        Todolist.objects.create(title = titles, description = descriptions)
        print(titles)
        return redirect('/task/') #if "/task/" xa vani "task/..." ma janxa tara if "task/" xa vani naya route hunxa ".../task"
    return render(request, "create.html")

# yesari data gaerako hunxa dct format
# {
#     "title":"hello",
#     "description":"hello smth"
# }

def complete_task(request,id):
    task= Todolist.objects.get(id = id)
    task.status=True
    task.save()
    return redirect('/task/')

def delete_task(request,id):
    de=Todolist.objects.get(id=id)
    de.delete()
    return redirect('/task/')


# example new edit form template
def edit_task(request):
    return render(request, "edit.html")