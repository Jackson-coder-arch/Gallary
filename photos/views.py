from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image


# Create your views here.
# def welcome(request):
#     return render(request, 'Welcome.html')

def photos(request):
    images = Image.objects.all()
    # locations = Location.objects.all()
    return render(request, 'welcome.html',{'image':images[::1]})


