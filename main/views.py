from django.shortcuts import render
from django.http import HttpResponse
from main.models import Room, Reservation
from django.views import View
from django.http import HttpResponse
from datetime import datetime
def test(request):
    return HttpResponse("test")

class RoomList(View):
    '''7. Pokazanie wszystkich sal ( adres /).'''
    def get(self, request):
        context = {
            "Rooms": [[x,[y.date for y in x.reservation_set.all()]] for x in Room.objects.all()],
            "today": datetime.today().date()
        }
        return render(request, "list_room.html", context)


class DetailRoom(View):
    '''Pokazanie danych jednej sali ( /room/{id}).'''
    def get(self, request, pk):
        room = Room.objects.get(pk=pk)
        context = {
            "room": [room, room.reservation_set.filter(date__gte=datetime.today().date()).values_list("date", flat=True)]
        }
        return render(request, "detail_room.html", context)


def add_room(request):
    if request.method == "GET":
        return render(request, "add_room.html")
    if request.method == "POST":
        rooms = Room()
        rooms.name = request.POST['name']
        rooms.capacity = request.POST['capacity']
        if request.POST['projector'] == "Tak":
            rooms.projector = True
        if request.POST['projector'] == "Nie":
            rooms.projector = False
        if request.POST['tv'] == "Tak":
            rooms.tv = True
        if request.POST['tv'] == "Nie":
            rooms.tv = False
        if request.POST['air_conditioning'] == "Tak":
            rooms.air_conditioning = True
        if request.POST['air_conditioning'] == "Nie":
            rooms.air_conditioning = False
        rooms.save()
        return HttpResponse("Dodano pokój")


def delete_room(request, id):
    if Room.objects.filter(id=id):
        room = Room.objects.get(id=id)
        room.delete()
        return HttpResponse(f"Sala {room.name} została usunięta.")
    else:
        return HttpResponse(f"Nie ma sali o takim id.")

