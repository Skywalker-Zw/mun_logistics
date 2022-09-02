# booking/urls.py
from django.urls import path
from .views import BookingListView, BookingDetailView,BookingCreate


urlpatterns = [
    path("booking/<int:pk>/",BookingDetailView.as_view(), name="booking_detail"),
    path("bookingcreate/",BookingCreate.as_view(),name="create_booking"),
    path("", BookingListView.as_view(), name="home"),
]