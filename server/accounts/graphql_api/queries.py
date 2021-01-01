import graphene
from accounts.models import CustomUser
from accounts.graphql_api.types import UserType


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.String())
    user = graphene.Field(UserType)
    all_drivers = graphene.List(UserType)
    all_riders = graphene.List(UserType)

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
        "For fetching all drivers"
        try:
            return CustomUser.objects.filter(groups__name="Driver")
        except CustomUser.DoesNotExist:
            return None

    def resolve_all_riders(self, info):
        "For fetching all drivers"
        try:
            return CustomUser.objects.filter(groups__name="Rider")
        except CustomUser.DoesNotExist:
            return None
