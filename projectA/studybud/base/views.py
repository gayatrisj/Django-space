from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Room, Topic
from django.http import HttpResponse
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

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            # Here you need to add logic to authenticate the user with the provided password
            # For example: 
            # if user.check_password(password):
            #     # Authentication successful
            # else:
            #     messages.error(request, "Invalid password")
        except User.DoesNotExist:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Authentication failed")
            
    context = {}
    return render(request, 'login_reg.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q) | 
         Q(description__icontains=q)
        ) 
    topic = Topic.objects.all()
    rooms_count = rooms.count()

    context = {'rooms': rooms, 'topics': topic, 'room_count':rooms.count()}
    return render(request,"home.html", context)

def room(request,num):
    room = Room.objects.get(id=num)
  
    context = {"room":room}
    return render(request, "room.html",context )

@login_required(login_url="/login")
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, "room_form.html",context)

@login_required(login_url="/login")
def updateRoom(request,id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse("Your not allowed to here")
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request ,"room_form.html", context)

@login_required(login_url="/login")
def deleteRoom(request, id):
    room = Room.objects.get(id=id)
    # form = RoomForm(instance=room)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, 'delete.html', {'obj': room})

