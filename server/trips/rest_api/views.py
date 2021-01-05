from django.shortcuts import render
from rest_framework import status, generics, permissions, viewsets
from trips.models import Trip
from trips.rest_api.serializers import NestedTripSerializer
from django.db.models import Q


class TripView(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'
    lookup_url_kwarg = 'trip_id'
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NestedTripSerializer

    def get_queryset(self):
        user = self.request.user
        print(user.group, "user group")
        if user.group == 'Driver':
            return Trip.objects.filter(
                Q(status=Trip.REQUESTED) | Q(driver=user)
            )
        if user.group == 'Rider':
            return Trip.objects.filter(rider=user)
        return Trip.objects.none()


class UpdateTripView(generics.UpdateAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'trip_id'
    queryset = Trip.objects.all()
    serializer_class = NestedTripSerializer
