from django.contrib import admin
from . models import Sernder_Details
# Register your models here.

class Sender_DetailsAdmin(admin.ModelAdmin):
    list_display= ('sender_name', 'sender_phone', 'receiver_name', 'receiver_phone')
    

admin.site.register(Sernder_Details, Sender_DetailsAdmin)
#admin.site.register(Items_Collected)
#admin.site.register(Receiver_Details)