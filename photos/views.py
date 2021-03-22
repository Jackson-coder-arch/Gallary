from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image


# Create your views here.
# def welcome(request):
#     return render(request, 'Welcome.html')

def photos(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'welcome.html',{'image':images[::1]})

def search_image(request):
    title ='search'
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image_category' in request.Get and request.Get['image_category']:
        search_term = request.Get.get('image_category')
        found_results = Image.search_by_category(search_term)
        messge =f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'search.html',{'title':title,'images':found_results, 'message':message, 'categories':categories, 'locations':locations})

