from rest_framework import serializers
from .models import Flight, Booking

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'destination', 'time', 'price',]

class ListSerializerBooking(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['flight', 'date', 'id',]