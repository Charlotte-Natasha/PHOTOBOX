from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    photos = Image.objects.all()
    categories = Category.objects.all()

    return render(request, 'gallery/index.html', {'photos':photos, 'categories':categories})

def category(request, pk):

    category_id = Category.objects.get(id=pk)
    photos = Image.objects.filter(category=category_id).all()
    context = {'category_id':category_id, 'photos':photos}

    return render(request, 'gallery/index.html', context)   

def location(request, pk):

    location_id = Location.objects.get(id=pk)
    photos = Image.objects.filter(location=location_id).all()
    context = {'location_id':location_id, 'photos':photos}

    return render(request, 'gallery/index.html', context)     
