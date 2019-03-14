
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
   # return HttpResponse('HELLO FROM RUBAI')
    return render(request, 'posts/index.html')

def add (x,y):
    return(x+y)
