def task(request):
    task=Todolist.objects.all()
    print(task)