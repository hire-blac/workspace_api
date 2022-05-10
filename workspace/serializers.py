from rest_framework import serializers
from .models import Booking, BookedDay, Plan, Space


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = ['id', 'name', 'slug']

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'slug']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'space', 'plan', 'slug']


class BookedDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedDay
        fields = ['id', 'created', 'booking', 'day', 'date_of_day', 'hours', 'starting_time', 'ending_time']
