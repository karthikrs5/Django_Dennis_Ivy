from django.shortcuts import render,redirect

from .models import Room,Topic

from .forms import RoomForm

# Create your views here.


def home(request):
    #q = request.GET.get('q')
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    #rooms = Room.objects.filter(topic__name=q)

    #icontains checks if atleast anything in 'q' matches the topic name
    rooms = Room.objects.filter(topic__name__icontains=q) 

    topics = Topic.objects.all()
    context={'rooms':rooms,'topics':topics}
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

