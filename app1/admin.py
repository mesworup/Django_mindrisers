from django.contrib import admin
from .models import Todolist


# Register your models here.

# we can register using these ways
# @admin.register(Todolist) or 
# admin.site.register(Todolist, TodolistAdmin)



# admin.site.register(Todolist)



# display model in list form
# class TodolistAdmin(admin.ModelAdmin):
#     list_display=('id','title','description','date','status')
# admin.site.register(Todolist, TodolistAdmin)


# display model in searchfield form
class TodolistAdmin(admin.ModelAdmin):
    list_display=('id','title','description','status')
    search_fields = ('id','title')      # adds search field
    list_filter=('status',)             # adds a filter for status
    list_per_page=3                     # how many data to show on a page
admin.site.register(Todolist, TodolistAdmin)


# @admin.register(Todolist)
# class TodolistAdmin(admin.ModelAdmin):
#     list_display=('id','title','description','date','status')
#     search_fields = ('id','title')      # adds search field
#     list_filter=('status',)             # adds a filter for status
#     list_per_page=3                     # how many data to show on a page
# # admin.site.register(Todolist, TodolistAdmin)



