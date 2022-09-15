from django.urls import path
from .views import HotelListProv, HotelCreate, HotelDetailProv, HotelDeleteProv

urlpatterns = [
    path('hotels-list/', HotelListProv.as_view()),
    path('hotels/', HotelCreate.as_view()),
    path('hotels/<id>/', HotelDetailProv.as_view()),
    path('hotels-delete/<id>/', HotelDeleteProv.as_view()),
]
