from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    photos = Image.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()

    return render(request, 'gallery/index.html', {'photos':photos, 'categories':categories, 'locations':locations})

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

def search(request):
    if request.method == "POST":
        searched = request.POST('searched')
        category = Category.objects.filter(title__contains=searched)

        return render(request, 'gallery/category.html', {'searched':searched, 'category':category})
    else:
        return render(request, 'gallery/category.html', {})   
