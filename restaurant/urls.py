from django.urls import path
from . import views
urlpatterns = [
    path('menu-items/', views.MenuItemViewSet.as_view()),
    path('menu-items/<int:pk>/', views.singleMenuItemView.as_view()),
    path('booking/', views.BookingView.as_view()),

]