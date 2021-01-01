from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>Home Views</h1>')

def board_details(request, pet_id):
    return HttpResponse(f'<h1> this is the board with the Id {Id}</h1>')
