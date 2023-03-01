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
            Todo_List = form.save()
            return redirect("todo_list_detail", id=Todo_List.id)
    else:
        form = TodosForm()

    context = {
        "form": form
    }
    return render(request, "todos/create.html", context)

def todo_list_update(request, id=id):
    edit = get_object_or_404(TodoList, id=id)

    if request.method == "POST":
        form = TodosForm(request.POST, instance=edit)
        if form.is_valid():
            edit = form.save()
            return redirect("todo_list_detail", id=edit.id)

    else:
        form = TodosForm(instance=edit)

    context = {
        "form" : form
    }
    return render(request, "todos/update.html", context)
