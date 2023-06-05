from django.shortcuts import render,redirect

from django.db.models import Q

from .models import Room,Topic

from .forms import RoomForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login,logout

#imports flash messages
from django.contrib import messages

# Create your views here.

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
        
    context={}
    return render(request, 'base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')



def home(request):
    #q = request.GET.get('q')
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    #rooms = Room.objects.filter(topic__name=q)

    #icontains checks if atleast anything in 'q' matches the topic name
    #rooms = Room.objects.filter(topic__name__icontains=q)

    #to check for multiple conditions
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    room_count=rooms.count() 

    topics = Topic.objects.all()
    context={'rooms':rooms,'topics':topics,'room_count':room_count}
    return render(request, 'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=int(pk))
    context={'room':room}
    return render(request, 'base/room.html',context)

def createRoom(request):
    form=RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/room_form.html',context)

def updateRoom(request,pk):
    #to get the details of the selected room
    room = Room.objects.get(id=int(pk))

    #selects the particular instance
    form = RoomForm(instance=room)

    #now process the data
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request, 'base/room_form.html',context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=int(pk))
    if request.method == 'POST' :
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})

