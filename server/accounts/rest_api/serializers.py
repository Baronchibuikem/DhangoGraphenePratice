from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):
    """
    For registering user
    """
    group = serializers.CharField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords must match')
        return data

    def create(self, validated_data):
        group_data = validated_data.pop('group')
        group, _ = Group.objects.get_or_create(name=group_data)
        data = {
            key: value for key, value in validated_data.items()
            if key not in ('password1', 'password2')
        }
        data['password'] = validated_data['password1']
        user = self.Meta.model.objects.create_user(**data)
        user.groups.add(group)
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'password1', "password2",
                  'last_name', 'email', 'group', 'user_id')
        read_only_field = ('id', 'user_id')


class LoginSerializer(TokenObtainPairSerializer):
    """
    For login
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom fields
        user_data = UserSerializer(user).data
        for key, value in user_data.items():
            if key != "id":
                token[key] = value
        return token
