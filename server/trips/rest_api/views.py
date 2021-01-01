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
        if user.group == 'driver':
            return Trip.objects.filter(
                Q(status=Trip.REQUESTED) | Q(driver=user)
            )
        if user.group == 'rider':
            return Trip.objects.filter(rider=user)
        return Trip.objects.none()


# class TripView(generics.ListAPIView):
#     serializer_class = NestedTripSerializer
#     # queryset = Trip.objects.all()

#     def get_queryset(self):
#         user = self.request.user
#         if user.group == 'driver':
#             return Trip.objects.filter(
#                  Q(status=Trip.REQUESTED) | Q(driver=user)
#             )
#         if user.group == 'rider':
#             return Trip.objects.filter(rider=user)
#         return Trip.objects.none()

# class TripDetailView(generics.RetrieveAPIView):
#     serializer_class = NestedTripSerializer
#     # queryset = Trip.objects.all()
#     lookup_url_kwarg = "trip_id"

#     def get_queryset(self):
#         user = self.request.user
#         if user.group == 'driver':
#             return Trip.objects.filter(
#                  Q(status=Trip.REQUESTED) | Q(driver=user)
#             )
#         if user.group == 'rider':
#             return Trip.objects.filter(rider=user)
#         return Trip.objects.none()
