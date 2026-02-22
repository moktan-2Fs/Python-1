from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id': 1, 'name': 'lets learn python'},
    {'id': 2, 'name': 'design with me(Moktan)'},
    {'id': 3, 'name': 'everyone is a jackass except me..'}

]

def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'room.html',{'rooms': rooms})


def main(request):
    context = {'rooms': rooms}
    return render(request, 'main.html',context)

def moktan(request):
    return render(request,'moktan.html')