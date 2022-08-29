from telnetlib import SE
from turtle import home
from django.shortcuts import render 
from django.views.generic import ListView
from .models import Sernder_Details

# Create your views here.
class BookingListView(ListView):
    model = Sernder_Details
    template_name = home.html
    