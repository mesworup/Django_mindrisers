from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome to the index page")

def home(request):
    return HttpResponse("HOMEEEEEE")

def aboutus(request):
    return HttpResponse("About Us")

def contact(request):
    return HttpResponse("Contact")

