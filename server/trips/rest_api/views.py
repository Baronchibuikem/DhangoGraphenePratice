from django.shortcuts import render
from rest_framework import status, generics, permissions, viewsets
from trips.models import Trip
from accounts.models import CustomUser
from trips.filters import TripFilter
from trips.rest_api.serializers import NestedTripSerializer, UpdateTripStatusSerializer
from django.db.models import Q
from rest_framework.response import Response


class TripView(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'
    lookup_url_kwarg = 'trip_id'
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NestedTripSerializer

    def get_queryset(self):
        user = self.request.user
        print(self.request)
        if user.is_authenticated and user.group == 'Driver':
            # return Trip.objects.filter(
            #     Q(status=Trip.REQUESTED) | Q(driver=user)
            # )
            return Trip.objects.filter(driver=user)

        if user.group == 'Rider':
            return Trip.objects.filter(rider=user)
        return Trip.objects.none()


class UpdateTripView(generics.UpdateAPIView):
    """
    For updating the status of a trip
    """
    lookup_field = 'id'
    lookup_url_kwarg = 'trip_id'
    queryset = Trip.objects.all()
    serializer_class = UpdateTripStatusSerializer
