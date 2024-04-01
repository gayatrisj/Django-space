from django.shortcuts import render
from django.shortcuts import redirect

from .models import Room
from .forms import RoomForm

# rooms = [
#     {'id': 1, 'name': 'lets learn web3'},
#     {'id': 2, 'name': 'python enthusiasts'},
#     {'id': 3, 'name': 'data science discussions'},
#     {'id': 4, 'name': 'AI and machine learning'},
#     {'id': 5, 'name': 'frontend development tips'},
#     {'id': 6, 'name': 'backend architecture'},
#     {'id': 7, 'name': 'cybersecurity talks'},
#     {'id': 8, 'name': 'cloud computing strategies'},
#     {'id': 9, 'name': 'blockchain innovations'},
#     {'id': 10, 'name': 'agile project management'}
# ]


def home(request):
    rooms = Room.objects.all()
    print(rooms)
    return render(request,"home.html", {'rooms': rooms})

def room(request,num):
    room = Room.objects.get(id=num)
  
    context = {"room":room}
    return render(request, "room.html",context )

def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, "room_form.html",context)

def updateRoom(request,id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request ,"room_form.html", context)

def deleteRoom(request, id):
    room = Room.objects.get(id=id)
    # form = RoomForm(instance=room)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, 'delete.html', {'obj': room})

