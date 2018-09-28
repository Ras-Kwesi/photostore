from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from .models import Image,Category,Location

# Create your views here.
def index(request):
    images = Image.getImage()
    return render(request,'index.html',{'images':images})