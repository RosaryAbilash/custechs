from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views Here

def index(response, name):
    text = ToDoList.objects.get(name=name)
    item = text.item_set.get(id=1)
    # HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(text.name, str(item.text)))
    return  render(response, "main/list.html", {"text": text})

def home(response):
    return  render(response, "main/home.html", {})

def about(response):
    return HttpResponse("<h1>About</h1><br></br><p>This is My new Django project</p>")
