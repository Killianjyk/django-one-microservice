from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem

# Create your views here.
def todo_list_list(request):
    todo_lists = TodoList.objects.all()
    context = {
        "todo_list_list": todo_lists,
    }
    return render(request, "todos/main.html", context)
