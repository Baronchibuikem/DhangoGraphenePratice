import graphene
from graphene_django import DjangoObjectType
from accounts.models import CustomUser


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name",
                  "user_id", 'email', 'username', "group",)

    group = graphene.String()

    def resolve_group(self, info):
        return self.group
