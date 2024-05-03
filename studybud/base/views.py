from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Room, Topic, Message
from django.http import HttpResponse
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
    q = request.GET.get('q') if request.GET.get('q') !=None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    topics = Topic.objects.all()
    room_messages = Message.objects.all()
    room_messages = Message.objects.filter(Q(room__name__icontains=q))

    context = {
        'rooms':rooms,
         'topics':topics,
         'room_count':rooms.count(),
         'room_messages':room_messages

         }
    return render(request,'base/home.html',context)


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try :
            user = User.objects.get(username=username)
            print(user)
        except User.DoesNotExist:
            messages.error(request, "User does not exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Authentication failed")
            
    context = {'page': page}
    return render(request,'base/login_reg.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    page = 'register'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred")
    else:
        form = UserCreationForm()
    return render(request, 'base/login_reg.html', {'form': form, 'page': page})

def room(request,pk):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all() 
    
    participants = room.participants.all()
    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    context = {'room':room, 'messages1':messages,"participants":participants}
    return render(request,'base/room.html',context)

@login_required(login_url="/login")
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,'base/room_form.html', context)

@login_required(login_url="/login")
def updateRoom(request, pk):
    room = Room.objects.get(id=int(pk))
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You are not allowed here!!")

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form': form}
    return render(request,'base/room_form.html', context)

@login_required(login_url="/login")
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("You are not allowed here!!")
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})

@login_required(login_url="/login")
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    
    if request.user != message.user:
        return HttpResponse("You are not allowed here!!")
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj': message})

@login_required(login_url="/login")
def deleteActivity(request, pk):
    message = Message.objects.get(id=pk)
    
    if request.user != message.user:
        return HttpResponse("You are not allowed here!!")
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj': message})