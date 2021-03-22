from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.photos,name = 'welcome'),
    url(r'^search/',views.search_image, name = 'search_image'),
    url(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
   
]
