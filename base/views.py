from django.shortcuts import render
# Create your views here.

rooms=[
    { 'id' :1 , 'name' :'Lets Learn Python!' },
    { 'id' :2 , 'name' :'Lets Learn JavaScript!' },
    { 'id' :3 , 'name' :'Lets Learn Django!' },
]

def home(request):
    return render(request, 'home.html',{'rooms':rooms})

def room(request):
    return render(request, 'room.html')
