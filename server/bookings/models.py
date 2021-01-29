from django.db import models
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class Car(models.Model):

    NOT_LOADING = 'NOT_LOADING'
    LOADING = 'LOADING'
    ENROUTE = 'ENROUTE'
    BROKEN_DOWN = 'BROKEN_DOWN'
    COMPLETED = 'COMPLETED'

    STATUSES = (
        (NOT_LOADING, NOT_LOADING),
        (LOADING, LOADING),
        (ENROUTE, ENROUTE),
        (BROKEN_DOWN, BROKEN_DOWN),
        (COMPLETED, COMPLETED)
    )
    car_name = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    car_assigned_number = models.IntegerField()
    car_plate_number = models.CharField(max_length=20)
    car_going_from = models.CharField(max_length=50)
    car_going_to = models.CharField(max_length=50)
    car_status = models.CharField(max_length=100, choices=STATUSES, default=NOT_LOADING)
    car_assigned_driver = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.car_name


class Trip(models.Model):
    car_assigned = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    departing_from = models.CharField(max_length=50)
    departing_to = models.CharField(max_length=50)
    departure_date = models.DateField()
    departure_time = models.TimeField()

    def __str__(self):
        return self.departing_from


class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    travelling_from = models.CharField(max_length=50)
    travelling_to = models.CharField(max_length=50)
    next_of_kin_name = models.CharField(max_length=100)
    next_of_kin_number = models.CharField(max_length=12)
    travel_date = models.DateField()
    amount_paid = models.IntegerField()
    assigned_car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class SeatNumber(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat_1 = models.BooleanField(default=False)
    seat_2 = models.BooleanField(default=False)
    seat_3 = models.BooleanField(default=False)
    seat_4 = models.BooleanField(default=False)
    seat_5 = models.BooleanField(default=False)
    seat_6 = models.BooleanField(default=False)
    seat_7 = models.BooleanField(default=False)
    seat_8 = models.BooleanField(default=False)
    seat_9 = models.BooleanField(default=False)
    seat_10 = models.BooleanField(default=False)
    seat_11 = models.BooleanField(default=False)
    seat_12 = models.BooleanField(default=False)
    date_booked = models.DateField()
