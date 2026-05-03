from django.shortcuts import render
from .models import Menu, Booking
# Create your views here.
def home(request):
    return render(request, 'index.html', {}
)

def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})
def booking(request):
    booking_items = Booking.objects.all()
    return render(request, 'booking.html', {'booking_items': booking_items})
def about(request):
    return render(request, 'about.html', {}
)
def create_booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        NO_of_guests = request.POST.get('guests')
        Bookingdate = request.POST.get('date')
        time = request.POST.get('time')
        booking = Booking(name=name, NO_of_guests=NO_of_guests, Bookingdate=Bookingdate, time=time)
        booking.save()
    return render(request, 'booking.html', {}
)
def add_to_cart(request):
    if request.method == 'POST':
        menu_id = request.POST.get('menu_id')
        menu_item = Menu.objects.get(id=menu_id)
        # handle cart logic
    return render(request, 'menu.html', {'menu_items': Menu.objects.all()})

      

    