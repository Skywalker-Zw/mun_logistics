# booking/urls.py
from django.urls import path
from .views import BookingListView, BookingDetailView


urlpatterns = [
    path("booking/<int:pk>/",BookingDetailView.as_view(), name="booking_detail"),
    path("", BookingListView.as_view(), name="home"),
]