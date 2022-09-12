from rest_framework import serializers
from .models import Hotel

class HotelListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Hotel
        fields = ['id', 'name']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
        }


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'description', 'check_in', 'check_out',
                  'num_rooms', 'stars', 'address', 'latitude', 'longitude']