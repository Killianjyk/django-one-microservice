from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodosForm

# Create your views here.
def todo_list_list(request):
    todo_lists = TodoList.objects.all()
    context = {
        "todo_list_list": todo_lists,
    }
    return render(request, "todos/main.html", context)

def todo_list_detail(request, id):
    todo_item = get_object_or_404(TodoList, id=id)
    context = {
        "list_details": todo_item,
    }
    return render(request, "todos/detail.html", context)

def todo_list_create(request):
    if request.method == "POST":
        form = TodosForm(request.POST)
        if form.is_valid():
            TodoList = form.save()
            return redirect("todo_list_list")
    else:
        form = TodosForm()

    context = {
        "form": form
    }
    return render(request, "todos/create.html", context)
