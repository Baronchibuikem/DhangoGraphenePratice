from django.contrib import admin
from bookings.models import Car, Trip, Passenger

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_model', 'car_assigned_number', 'car_plate_number',
                    'car_going_from', 'car_going_to', 'car_status', 'car_assigned_driver',)


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display=('car_assigned', 'departing_from', 'departing_to', 'departure_date', 'departure_time',)



@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'travelling_to', 'travelling_from',
                    'next_of_kin_name', 'next_of_kin_number', 'travel_date', 'amount_paid', "assigned_car")