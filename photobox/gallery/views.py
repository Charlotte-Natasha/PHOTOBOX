from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    photos = Image.objects.all()

    return render(request, 'gallery/index.html', {'photos':photos})
