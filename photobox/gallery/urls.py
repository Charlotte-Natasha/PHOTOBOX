from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='home'),
    path('category/<str:pk>', views.category, name='category')
]
