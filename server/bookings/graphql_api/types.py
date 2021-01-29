import graphene
from graphene_django import DjangoObjectType
from bookings.models import Car, Passenger, Trip


class TripType(DjangoObjectType):
    first_name =  graphene.String()
    last_name = graphene.String()
    phone_number = graphene.Int()
    travelling_to = graphene.String()
    travelling_from =  graphene.String()
    next_of_kin_name = graphene.String()
    next_of_kin_number = graphene.String()
    travel_date = graphene.Date()
    amount_paid = graphene.Int()

    class Meta:
        model = Trip


class CarType(DjangoObjectType):
    car_name = graphene.String()
    car_model = graphene.String()
    car_assigned_number = graphene.Int()
    car_plate_number = graphene.String()
    car_going_from = graphene.String()
    car_going_to = graphene.String()
    car_status = graphene.String()
    car_assigned_driver = graphene.String()

    class Meta:
        model = Car


class PassengerType(DjangoObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    phone_number = graphene.String()
    travelling_from = graphene.String()
    travelling_to = graphene.String()
    next_of_kin_name = graphene.String()
    next_of_kin_number = graphene.String()
    travel_date = graphene.Date()
    amount_paid = graphene.Int()
    assigned_car = graphene.String()

    class Meta:
        model = Passenger
    
    