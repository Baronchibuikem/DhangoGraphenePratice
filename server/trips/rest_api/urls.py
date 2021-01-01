from django.contrib import admin
from django.urls import path
from trips.rest_api.views import TripView

app_name = 'taxiapp'

urlpatterns = [
    path('', TripView.as_view({'get': 'list'}), name="trip_list"),
    path('<uuid:trip_id>/',
         TripView.as_view({'get': 'retrieve'}), name='trip_detail')
]

# from django.contrib import admin
# from django.urls import path
# from trips.views import TripView, TripDetailView

# app_name = 'taxiapp'

# urlpatterns = [
#     path('', TripView.as_view(), name="trip_list"),
#     path('<uuid:trip_id>/', TripDetailView.as_view(), name='trip_detail')
# ]
