# booking/urls.py
from django.urls import path
from .views import BookingListView, BookingDetailView,BookingCreate,BookingUpdate


urlpatterns = [
    path("booking/<int:pk>/",BookingDetailView.as_view(), name="booking_detail"),
    path("bookingcreate/",BookingCreate.as_view(),name="create_booking"),
    path("booking_update/int:pk", BookingUpdate.as_view(), name="update_booking"),
    path("", BookingListView.as_view(), name="home"),
]