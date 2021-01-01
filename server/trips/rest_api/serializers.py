from trips.models import Trip
from rest_framework import serializers


class NestedTripSerializer(serializers.ModelSerializer):
    rider = serializers.ReadOnlyField(source="rider.username")
    driver = serializers.ReadOnlyField(source="driver.username")
    
    class Meta:
        model = Trip
        fields = ('id', 'created', 'updated', 'pick_up_address', 'drop_off_address', 'status', 'rider', 'driver',)
        depth: 1
        
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        read_only_fields = ('id', 'created', 'updated',)