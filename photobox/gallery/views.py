from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    photos = Image.objects.all()
    categories = Category.objects.all()

    return render(request, 'gallery/index.html', {'photos':photos, 'categories':categories})
