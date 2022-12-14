# Generated by Django 4.1 on 2022-08-28 09:45

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sernder_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=400)),
                ('sender_address', models.CharField(max_length=400)),
                ('sender_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('sender_email', models.EmailField(max_length=254)),
                ('collection_date', models.DateField()),
                ('time_slot', models.TimeField()),
                ('boxes', models.IntegerField()),
                ('drums', models.IntegerField()),
                ('odd_parcels_items', models.CharField(max_length=400)),
                ('receiver_name', models.CharField(max_length=400)),
                ('receiver_address', models.CharField(max_length=400)),
                ('receiver_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('receiver_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
