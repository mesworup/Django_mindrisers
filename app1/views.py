from django.shortcuts import render
from django.http import HttpResponse
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

# create dynamic html pages for all