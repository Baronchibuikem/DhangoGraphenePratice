from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from trips.models import Trip
from accounts.models import CustomUser
from trips.rest_api.serializers import TripSerializer
from django.contrib.auth.models import Group


import base64
import json


PASSWORD = 'passWorD!#'


# Note that we added a create_user() helper function to help keep our code DRY.
def create_user(username='use@example.com', password=PASSWORD, group_name="rider"):
    group, _ = Group.objects.get_or_create(name=group_name)
    user = get_user_model().objects.create_user(
        username=username, password=password)
    user.groups.add(group)
    user.save()
    return user


class HttpTripTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        # response = self.client.post(reverse('log_in'), data={
        #     'username': user.username,
        #     'password': PASSWORD
        # })
        # access = response.data['access']
        # return access
        self.client.login(username=self.user.username, password=PASSWORD)

    def test_user_can_list_trips(self):
        trips = [
            Trip.objects.create(pick_up_address='A',
                                drop_off_address='B', rider=self.user),
            Trip.objects.create(pick_up_address='B',
                                drop_off_address='C', rider=self.user),
            Trip.objects.create(pick_up_address='C', drop_off_address='D')
        ]
        # response = self.client.get(reverse('trip:trip_list'),
        #                            HTTP_AUTHORIZATION=f'Bearer {self.setup()}')
        response = self.client.get(reverse('trip:trip_list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_user_can_retrieve_trip_by_id(self):
        trip = Trip.objects.create(
            pick_up_address='A', drop_off_address='B', rider=self.user)
        # response = self.client.get(trip.get_absolute_url(),
        #     HTTP_AUTHORIZATION=f'Bearer {self.setup()}'
        # )
        response = self.client.get(trip.get_absolute_url())
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(str(trip.id), response.data.get('id'))
