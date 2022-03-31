from rest_framework import serializers
from .models import Review
from hotelapp.models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    class Meta:
        model = Review
        fields = "__all__"
