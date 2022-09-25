from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from .serializers import HotelListSerializer, HotelSerializer
from .models import Hotel

class HotelListProv(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    permission_classes = ()

class HotelCreate(CreateAPIView):
    serializer_class = HotelSerializer
    permission_classes = ()


class HotelDetailProv(RetrieveUpdateAPIView):
    serializer_class = HotelSerializer  
    queryset = Hotel.objects.all()  
    permission_classes = ()
    lookup_field = 'id'


class HotelDeleteProv(DestroyAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()
    permission_classes = ()
    lookup_field = 'id'
