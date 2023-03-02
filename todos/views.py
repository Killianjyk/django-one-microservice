from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodosForm, ItemForm

# Create your views here.
def todo_list_list(request):
    todo_lists = TodoList.objects.all()
    context = {
        "todo_list_list": todo_lists,
    }
    return render(request, "todos/main.html", context)

def todo_list_detail(request, id):
    list = TodoList.objects.get(id=id)
    context = {
        "list": list,
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


def todo_list_delete(request, id):
    this_list = get_object_or_404(TodoList, id=id)

    if request.method == "POST":
        this_list.delete()
        return redirect("todo_list_list")

    return render(request, "todos/delete.html")

def todo_item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            Todo_Item = form.save()
            return redirect("todo_list_detail", id=Todo_Item.list.id)
    else:
        form = ItemForm()
    context = {
        "form" : form,
    }

    return render(request, "items/create.html", context)


def todo_item_update(request, id):
    item = TodoItem.objects.get(id=id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = ItemForm(instance=item)
    context = {
        "form": form,
    }
    return render(request, "items/update.html", context)
