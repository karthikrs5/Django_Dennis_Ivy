from django.shortcuts import render
# Create your views here.

def home(request):
    render(request, 'home.html')

def room(request):
    render(request, 'room.html')
