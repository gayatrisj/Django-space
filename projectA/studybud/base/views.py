from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'lets learn web3'},
    {'id': 2, 'name': 'python enthusiasts'},
    {'id': 3, 'name': 'data science discussions'},
    {'id': 4, 'name': 'AI and machine learning'},
    {'id': 5, 'name': 'frontend development tips'},
    {'id': 6, 'name': 'backend architecture'},
    {'id': 7, 'name': 'cybersecurity talks'},
    {'id': 8, 'name': 'cloud computing strategies'},
    {'id': 9, 'name': 'blockchain innovations'},
    {'id': 10, 'name': 'agile project management'}
]


def home(request):
    return render(request,"home.html", {'rooms': rooms})

def room(request,num):
    room = None
    for i in rooms:
        if i["id"] == num:
            room = i
    context = {"room":room}
    return render(request, "room.html",context )
