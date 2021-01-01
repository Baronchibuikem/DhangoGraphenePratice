import graphene
import graphql_jwt
from accounts.graphql_api.schema import Query as account_query, Mutation as account_mutation


class AccountQuery(account_query, graphene.ObjectType):
    pass


class AccountMutation(account_mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=AccountQuery, mutation=AccountMutation)
