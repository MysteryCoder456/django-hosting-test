from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateListForm


def home(request):
    return render(request, "main/base.html", {})


def index(request, id):
    ls = ToDoList.objects.get(id=id)

    if request.method == "POST":
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c" + str(item.id)):
                    item.complete = True
                else:
                    item.complete = False
                
                item.save()

        elif request.POST.get("addItem"):
            text = request.POST.get("newItem")

            if len(text) > 2:
                ls.item_set.create(text=text, complete=False)
            else:
                print("Item too short!")

        elif request.POST.get("delete"):
            for item in ls.item_set.all():
                item.delete()

    return render(request, "main/list.html", {"ls": ls})


def create(request):
    if request.method == "POST":
        form = CreateListForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            id = form.cleaned_data["id"]            
            t = ToDoList(id=id, name=name)
            t.save()

        return HttpResponseRedirect("/%s" % t.id)
    else:
        form = CreateListForm()
    return render(request, "main/create.html", {"form":form})