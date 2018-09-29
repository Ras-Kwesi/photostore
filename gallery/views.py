from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from .models import Image,Category,Location

# Create your views here.
def index(request):
    images = Image.getImages()
    return render(request,'index.html',{'images':images})

def singleimage(request,image_id):
    try:
        image = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"location.html", {"image":image})

def imagesbylocation(request):
    images= Image.collectimagelocation()
    return render(request,'location.html',images=images)