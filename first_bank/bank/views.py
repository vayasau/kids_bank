from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Money


def index(request):
    return HttpResponse("Bankas cia!")

def money(request, user_id):
    # trans_list = Money.objects.order_by('-trans_date')[:5]
    # output = ', '.join([t.amount for t in trans_list])
    return HttpResponse(f"Labas {user_id}, tavo transakcijos: ")
