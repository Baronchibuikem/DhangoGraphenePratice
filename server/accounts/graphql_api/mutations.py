import graphene
import graphql_jwt
from graphene_django.rest_framework.mutation import SerializerMutation
from accounts.graphql_api.types import UserType
from django.contrib.auth import get_user_model



class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)