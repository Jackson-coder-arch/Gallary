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
    else:
        message = 'No searches found yet'
        return render (request, 'search.html',{"message":message}

def location_filter(request, image_location):
    location = Location.get_location_id(image_location)
    images = Image.filter_by_location(image_location)
    title = f'{location} Photos'
    return render(request, 'location.html', {'title':title,'images':images,'location':location})
