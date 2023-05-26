from django.shortcuts import render
# Create your views here.

rooms=[
    { 'id' :1 , 'name' :'Lets Learn Python!' },
    { 'id' :2 , 'name' :'Lets Learn JavaScript!' },
    { 'id' :3 , 'name' :'Lets Learn Django!' },
]

def home(request):
    context={'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request):
    return render(request, 'base/room.html')
