import graphene
from bookings.graphql_api import queries


class Query(queries.Query, graphene.ObjectType):
    pass