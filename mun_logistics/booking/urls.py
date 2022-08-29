from django.urls import path
from .views import BookingListView

urlpattens = [
    path("",BookingListView.as_view(), name ="home")
]