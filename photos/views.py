from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image,Location,Category


# Create your views here.
# def welcome(request):
    # category = request.GET.get('category')
    # if category == None:
    #    photos = Image.objects.all()
    
    # else:
    #     photos = Image.objects.filter(category__name__contains=category)

    # categories = Category.objects.all()
    # # photos = Photo.objects.all()

    # context = {'categories': categories, 'photos': photos}
    
    # return render(request, 'welcome.html')

def photos(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'welcome.html',{'images':images[::1],'locations': locations })

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
    else:
        message = 'No searches found yet'
        return render (request, 'search.html',{"message":message})


    return render(request, 'search.html',{'title':title,'images':found_results, 'message':message, 'categories':categories, 'locations':locations})
    
def location_filter(request, image_location):
    location = Location.get_location_id(image_location)
    images = Image.filter_by_location(image_location)
    title = f'{location} Photos'
    return render(request, 'location.html', {'title':title,'images':images,'location':location})

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'images/location.html', {'location_images': images})
