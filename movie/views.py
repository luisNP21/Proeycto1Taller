from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Luis Angel'})

def about(request):
    return HttpResponse('Welcome to about page</h1>')


