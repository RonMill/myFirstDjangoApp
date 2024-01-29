from django.shortcuts import render
from .models import Room


# rooms = [
#   {'id': 1, 'name': 'Lets learn python!'},
#   {'id': 2, 'name': 'Desgin with me!'},
#   {'id': 3, 'name': 'Devs!'},
# ]


# Create your views here.
def home(request):
  rooms = Room.objects.all()
  context = {'rooms': rooms}
  return render(request, 'base/home.html', context)

def room(request, pk):
  room = Room.objects.get(id=pk)
  context = {'room': room}
  return render(request, 'base/room.html', context)

# first version with defined data inside this file
  # room = None
  # for i in rooms:
  #   if i['id'] == int(pk):
  #     room = i
  # context = {'room': room}