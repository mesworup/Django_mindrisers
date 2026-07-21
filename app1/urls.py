from django.urls import path
from .views import *

 
urlpatterns = [
    path('index/', index),                              # path('index/', views.index)
    path('home/', home),
    path('contact/', contact),
    path('aboutus/', aboutus),
    path('task/', task),
    path('task/create', create_task),
    path('task/edit', edit_task),
    path('task/mark/<id>/', complete_task),
    path('task/delete/<id>/', delete_task),


]
