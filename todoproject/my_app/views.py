from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from . import models
# Create your views here.


def home(request):
    todo_items = models.Todo.objects.all().order_by('-added_date')
    print(todo_items)
    all_items = {
        'todo_items': todo_items
    }
    return render(request, 'my_app/index.html', all_items)


def add_todo(request):
    item = request.POST.get('todoitem')
    current_date = timezone.now()
    models.Todo.objects.create(text=item, added_date=current_date)
    print(item)

    return HttpResponseRedirect('/')


def delete_todo(request, todo_id):
    models.Todo.objects.get(id=todo_id).delete()
    print(todo_id)
    return HttpResponseRedirect('/')
