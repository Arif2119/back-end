from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('booking/', views.booking, name='booking'),
    path('about/', views.about, name='about'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart')
,
]