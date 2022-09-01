from django.contrib import admin
from . models import Booking_Details
# Register your models here.

class Booking_DetailsAdmin(admin.ModelAdmin):
    list_display= ('sender_name', 'sender_phone', 'receiver_name', 'receiver_phone')
    

admin.site.register(Booking_Details, Booking_DetailsAdmin)
