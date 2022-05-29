from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    photos = Image.object.all()

    return render(request, 'gallery/index.html', {'photos':photos})
