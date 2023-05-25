from django.contrib import admin
from django.urls import path

#This is required to send response to the browser
from django.http import HttpResponse

#simple function to send response
def home(request):
    return HttpResponse('Home Page')

#Adding another route
def room(request):
    return HttpResponse('ROOM')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path 
    path('',home),

    #adding path to the new route "ROOM"
    path('room/',room),
]
