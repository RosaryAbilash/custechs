from django.shortcuts import render
from django.http import HttpResponse

# Create your views Here

def index(response):
    return HttpResponse("<h1>Custechs</h1>")

def about(response):
    return HttpResponse("<h1>About</h1>")