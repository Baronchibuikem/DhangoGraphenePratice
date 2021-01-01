import graphene
from accounts.graphql_api import queries, mutations


class Query(queries.Query, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_user = mutations.CreateUser.Field()
