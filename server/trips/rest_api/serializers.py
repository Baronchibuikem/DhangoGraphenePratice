from trips.models import Trip
from rest_framework import serializers


class NestedTripSerializer(serializers.ModelSerializer):
    rider = serializers.ReadOnlyField(source="rider.username")
    driver = serializers.ReadOnlyField(source="driver.username")

    class Meta:
        model = Trip
        fields = ('id', 'created', 'updated', 'pick_up_address',
                  'drop_off_address', 'status', 'rider', 'driver',)
        depth: 1


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        read_only_fields = ('id', 'created', 'updated',)


class UpdateTripStatusSerializer(serializers.ModelSerializer):
    status = serializers.CharField()

    class Meta:
        model = Trip
        fields = ("id", "status",)

    def update(self, instance, validated_data):
        status_field = validated_data.get('status')
        if status_field == "ACCEPTED":
            instance.status = "ACCEPTED"
            instance.save()
        elif status_field == "STARTED":
            instance.status == "STARTED"
            instance.save()
        elif status_field == "COMPLETED":
            instance.status == "COMPLETED"
            instance.save()
        else:
            instance.status == "REQUESTED"
            instance.save()
        return instance
