from accounts.models import CustomUser
from trips.models import Trip
from django_filters import rest_framework as filters


class TripFilter(filters.FilterSet):
    class Meta:
        model = Trip
        fields = [
            'id', 'pick_up_address', 'drop_off_address', 'status', 'driver', 'rider', 'created', 'updated',
        ]
