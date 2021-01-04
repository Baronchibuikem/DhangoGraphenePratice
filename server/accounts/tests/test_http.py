from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from trips.models import Trip
from django.contrib.auth.models import Group
from accounts.models import CustomUser

# for testing file upload
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import Group

import base64
import json

PASSWORD = 'passWorD!#'

# Note that we added a create_user() helper function to help keep our code DRY.


def create_user(username='user@example.com', password=PASSWORD, group__name="rider"):
    group, _ = Group.objects.get_or_create(name=group__name)
    user = get_user_model().objects.create_user(
        username=username, password=password)
    user.groups.add(group)
    user.save()
    return user


# def create_photo_file():
#     data = BytesIO()
#     Image.new('RGB', (100, 100)).save(data, 'PNG')
#     data.seek(0)
#     return SimpleUploadedFile('photo.png', data.getvalue())


class AuthenticationTest(APITestCase):
    def test_user_can_sign_up(self):
        # photo_file = create_photo_file()
        response = self.client.post(reverse('sign_up'), data={
            'username': 'baron',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': PASSWORD,
            'password2': PASSWORD,
            'group': 'rider',
            # 'photo': photo_file,
        })
        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['first_name'], user.first_name)
        self.assertEqual(response.data['last_name'], user.last_name)
        self.assertEqual(response.data['group'], user.group)
        # self.assertIsNotNone(user.photo)

    def test_user_can_login(self):
        user = create_user()
        response = self.client.post(reverse('log_in'), data={
            'username': user.username,
            'password': PASSWORD
        })
        # Parse payload data from access token
        # The JSON Web Token structure consists of a header, a payload, and a signature. The payload is a Base64Url
        # encoded, JSON-serialized object containing data about the user. We leverage the base64 library to decode the
        # payload. (We need to add back the == padding characters that JWT strips out to avoid errors.) Then we use json to
        # parse the JSON string into an object.
        access = response.data['access']
        header, payload, signature = access.split('.')
        decoded_payload = base64.b64decode(f'{payload}==')
        payload_data = json.loads(decoded_payload)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIsNotNone(response.data['refresh'])
        self.assertEqual(payload_data['id'], user.id)
        self.assertEqual(payload_data['username'], user.username)
        self.assertEqual(payload_data['first_name'], user.first_name)
        self.assertEqual(payload_data['last_name'], user.last_name)

    def test_get_all_users(self):
        user_one = create_user("user1", "admin12345", "Driver")
        user_two = create_user("user2", "admin12345", "Rider")

        all_users = [user_one, user_two]

        response = self.client.get(reverse('users'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(all_users))

    def test_get_user_by_id(self):
        user = create_user("user7", "admin12345", "Driver")
        response = self.client.get(user.get_absolute_url())
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(user.id, response.data.get('id'))

    #     def test_user_can_list_trips(self):
    #     trips = [
    #         Trip.objects.create(pick_up_address='A',
    #                             drop_off_address='B', rider=self.user),
    #         Trip.objects.create(pick_up_address='B',
    #                             drop_off_address='C', rider=self.user),
    #         Trip.objects.create(pick_up_address='C', drop_off_address='D')
    #     ]
    #     # response = self.client.get(reverse('trip:trip_list'),
    #     #                            HTTP_AUTHORIZATION=f'Bearer {self.setup()}')
    #     response = self.client.get(reverse('trip:trip_list'))
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)

    # def test_user_can_retrieve_trip_by_id(self):
    #     trip = Trip.objects.create(
    #         pick_up_address='A', drop_off_address='B', rider=self.user)
    #     # response = self.client.get(trip.get_absolute_url(),
    #     #     HTTP_AUTHORIZATION=f'Bearer {self.setup()}'
    #     # )
    #     response = self.client.get(trip.get_absolute_url())
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     self.assertEqual(str(trip.id), response.data.get('id'))
