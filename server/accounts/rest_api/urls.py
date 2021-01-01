from accounts.rest_api.views import (SignUpView, LogInView, UsersListView, GetAllRidersView, GetAllDriversView,
                                     GetUserById)
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', SignUpView.as_view(), name="sign_up"),
    path('login/', LogInView.as_view(), name="log_in"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('users/', UsersListView.as_view(), name="users"),
    path("all-riders/", GetAllRidersView.as_view(), name="all-riders"),
    path("all-drivers/", GetAllDriversView.as_view(), name="all-drivers"),
    path("user/<int:pk>/", GetUserById.as_view(), name="single-user")
]
