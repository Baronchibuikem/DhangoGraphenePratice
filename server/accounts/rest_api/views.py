from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.rest_api.serializers import UserSerializer, LoginSerializer
from accounts.models import CustomUser


class SignUpView(generics.CreateAPIView):
    """
    User Signup view
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LogInView(TokenObtainPairView):
    """
    User Login view
    """
    serializer_class = LoginSerializer


class UsersListView(generics.ListAPIView):
    """
    For getting all the users
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class GetUserById(generics.RetrieveAPIView):
    """
    For fetching a single user
    """
    serializer_class = UserSerializer
    queryset = CustomUser


class GetAllRidersView(generics.ListAPIView):
    """
    For getting all riders
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        user = CustomUser.objects.filter(groups__name="Rider")
        return user


class GetAllDriversView(generics.ListAPIView):
    """
    For getting all drivers
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        user = CustomUser.objects.filter(groups__name="Driver")
        return user
