import graphene
from bookings.graphql_api.types import CarType, PassengerType, TripType
from bookings.models import Car, Passenger, Trip


class Query(graphene.ObjectType):
    allCars = graphene.List(CarType)


    def resolve_allCars(self, info):
        """
        For fetching all the cars 
        """
        return Car.objects.all()