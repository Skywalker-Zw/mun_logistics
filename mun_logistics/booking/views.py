# booking/views.py
from django.views.generic import ListView, DetailView
from .models import Booking_Details
class BookingListView(ListView):
    model = Booking_Details
    template_name = "home.html"
    
class BookingDetailView(DetailView):
    model = Booking_Details   
    template_name = "booking_detail.html"