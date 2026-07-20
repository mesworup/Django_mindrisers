from django.urls import path
from .views import *

 
urlpatterns = [
    path('index/', index),                              # path('index/', views.index)
    path('home/', home),
    path('contact/', contact),
    path('aboutus/', aboutus),
    path('task/create', create_task),
    path('task/edit', edit_task),
]
