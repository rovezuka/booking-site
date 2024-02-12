from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import Item, Reservation
from .serializers import ItemSerializer, ReservationSerializer


# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
        queryset = Item.objects.all()
        serializer_class = ItemSerializer


class ReservationView(ListCreateAPIView):
        queryset = Reservation.objects.all()
        serializer_class = ReservationSerializer

        def create(self, request, *args, **kwargs):
                response = super().create(request, *args, **kwargs)
                item_id = request.data.get('item')
                if item_id:
                        item = Item.objects.get(id=item_id)
                        item.quantity -= self.queryset.num
                        item_serializer = ItemSerializer(item)
                        item.serializer.quantity = item.quantity - self.queryset.num
                        item_serializer.save()
                return response

