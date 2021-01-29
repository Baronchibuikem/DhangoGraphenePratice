import graphene
from django.contrib.auth import get_user_model
from accounts.graphql_api.types import UserType

CustomUser = get_user_model()

class Query(graphene.ObjectType):
    allUsers = graphene.List(UserType)
    userById = graphene.Field(UserType, id=graphene.String())
    user = graphene.Field(UserType)
    allDrivers = graphene.List(UserType)
    allRegistered_passengers = graphene.List(UserType)

    def resolve_all_users(self, info):
        """
        For fetching all users from the database
        """
        return CustomUser.objects.all()
        # authenticated_user = info.context.user.is_authenticated
        # if not authenticated_user:
        #     return CustomUser.objects.none()
        # else:
        #     return CustomUser.objects.all()

    def resolve_user_by_id(self, info, id):
        """
        For getting a single user by id
        """
        try:
            return CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return None

    def resolve_user(self, info):
        """
        For getting the current logged in user's details
        """
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication Failure")
        return user

    def resolve_all_drivers(self, info):
        "For fetching all users with drivers role"
        try:
            return CustomUser.objects.filter(role__name="driver")
        except CustomUser.DoesNotExist:
            return None

    def resolve_all_registered_passengers(self, info):
        "For fetching all users except for those with drivers role"
        try:
            return CustomUser.objects.exclude(role__name="driver")
        except CustomUser.DoesNotExist:
            return None
