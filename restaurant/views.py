from django.shortcuts import render
from rest_framework.decorators import api_view

from restaurant.models import Booking, MenuItem
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework import generics

# Create your views here.
class MenuItemViewSet(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class singleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

