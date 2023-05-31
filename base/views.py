from django.shortcuts import render,redirect

from .models import Room

from .forms import RoomForm

# Create your views here.


def home(request):
    rooms = Room.objects.all()
    context={'rooms':rooms}
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

