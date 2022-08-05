from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def start(request):
    return HttpResponse("Bankas cia!")

def money(request, user_id):
    return HttpResponse(f"Labas {user_id}, tavo balansas: ")
