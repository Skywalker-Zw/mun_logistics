# booking/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Booking_Details
from django.urls import reverse_lazy
class BookingListView(ListView):
    model = Booking_Details
    template_name = "home.html"
    
class BookingDetailView(DetailView):
    model = Booking_Details   
    template_name = "booking_detail.html"

class BookingCreate(CreateView):
    model = Booking_Details
    fields = "__all__"
    template_name = "create_booking.html"
    success_url = reverse_lazy("home")

class BookingUpdate(UpdateView):
    model = Booking_Details
    fields = "__all__"
    template_name = "update_booking.html"
    #success_url = reverse_lazy("home")


