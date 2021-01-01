import graphene
import graphql_jwt
from graphene_django.rest_framework.mutation import SerializerMutation

from accounts.rest_api.serializers import UserSerializer


class CreateUser(SerializerMutation):
    """ 
    For registering a user into the database
    """
    class Meta:
        serializer_class = UserSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'
