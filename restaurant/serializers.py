from rest_framework import serializers
from .models import Menu, Booking
import bleach

class MenuSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        return bleach.clean(value)
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        return bleach.clean(value)
    class Meta:
        model = Booking
        fields = '__all__'
