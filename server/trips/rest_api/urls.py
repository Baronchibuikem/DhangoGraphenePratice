from django.contrib import admin
from django.urls import path
from trips.rest_api.views import TripView, UpdateTripView


# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

app_name = 'taxiapp'

# router.register(r'update', UpdateTripView, basename="update-trip")

urlpatterns = [
    path('', TripView.as_view({'get': 'list'}), name="trip_list"),
    path('update/<uuid:trip_id>/', UpdateTripView.as_view(), name="update"),
    path('<uuid:trip_id>/',
         TripView.as_view({'get': 'retrieve'}), name='trip_detail'),
]
