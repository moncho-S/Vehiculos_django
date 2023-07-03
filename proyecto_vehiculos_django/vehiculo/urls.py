from django.urls import path
from .views import *

urlpatterns = [
    path('',vehiculoView,name='vehiculoName'),
    path('add/',addView,name='addName'),
    path('list/',listView,name='listName'),
    path('logout/',logoutView,name='logoutName'),
    path('login/',loginView,name='loginName')
]