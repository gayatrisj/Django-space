from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
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