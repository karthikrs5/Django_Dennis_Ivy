from django.shortcuts import render

#importing HttpResponse to send response to browser
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Home")

def room(request):
    return HttpResponse("ROOM")
