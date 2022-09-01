from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

# Create your models here.
class Booking_Details(models.Model):
    sender_name = models.CharField(max_length=400)
    sender_address = models.CharField(max_length=400)
    sender_phone = PhoneNumberField()
    sender_email = models.EmailField(max_length = 254)
    collection_date = models.DateField()
    #ItemesColllected
    time_slot = models.TimeField()
    boxes = models.IntegerField()
    drums = models.IntegerField()
    odd_parcels_items = models.CharField(max_length=400)
    #insert_image = models.ImageField #Todo
    #Receivers Information
    receiver_name = models.CharField(max_length=400)
    receiver_address = models.CharField(max_length=400)
    receiver_phone = PhoneNumberField()
    receiver_email = models.EmailField(max_length = 254)

    def __str__(self):
        return self.sender_name
    def get_absolute_url(self):
        return reverse("booking_detail", kwargs={"pk": self.pk})


