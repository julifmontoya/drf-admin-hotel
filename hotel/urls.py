from django.urls import path
from .views import HotelListProv, HotelCreate, HotelDetailProv, HotelDeleteProv

urlpatterns = [
    path('affiliate/hotels-list/', HotelListProv.as_view()),
    path('affiliate/hotels/', HotelCreate.as_view()),
    path('affiliate/hotels/<id>/', HotelDetailProv.as_view()),
    path('affiliate/hotels-delete/<id>/', HotelDeleteProv.as_view()),
]
