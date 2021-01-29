import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
 
User = get_user_model()

class UserType(DjangoObjectType):
    class Meta:
        model = User
        # or you can define it like this
        fields = ("id", "first_name", "last_name",
                  "user_id", 'email', 'username')

    # We are using this to get the group a user belongs to if we are to add groups to our user model instance
    # group = graphene.String()

    # def resolve_group(self, info):
    #     return self.group


