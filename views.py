from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("hello world")
def home(request):
    return render(request,"first.html")
def second(request):
    return render(request,"directory/second.html")

