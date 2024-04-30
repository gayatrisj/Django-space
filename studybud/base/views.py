from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
# rooms = [
#     {'id': 1, 'name': 'Advanced Python Programming'},
#     {'id': 2, 'name': 'Mastering ReactJS'},
#     {'id': 3, 'name': 'Deep Dive into Machine Learning'},
#     {'id': 4, 'name': 'Data Structures and Algorithms in Python'},
#     {'id': 5, 'name': 'Frontend Development Best Practices'},
#     {'id': 6, 'name': 'Cloud Computing Essentials'}
# ]
# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    
    context = {'room':room}
    return render(request,'base/room.html',context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=int(pk))
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form': form}
    return render(request,'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})
