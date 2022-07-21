import datetime

from django.utils import timezone

from .models import Booking, Flight
from django.http import HttpResponse
from .serialzers import ListSerializer, ListSerializerBooking
from rest_framework.generics import ListAPIView


class showFlights(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ListSerializer

class upcomingBooking(ListAPIView):

    queryset = Booking.objects.all().filter(date__gt= timezone.now())
    serializer_class = ListSerializerBooking