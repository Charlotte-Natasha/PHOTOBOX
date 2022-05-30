from unicodedata import name
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='home'),
    path('category/<str:pk>', views.category, name='category'),
    path('location/<str:pk>', views.location, name='location'),
    path('search/', views.search, name='search')
]
