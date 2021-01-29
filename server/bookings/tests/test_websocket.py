from channels.testing import WebsocketCommunicator
import pytest
from taxiapp import settings
from taxiapp.asgi import application
from channels.layers import get_channel_layer
from django.contrib.auth.models import Group
from django.conf import settings
from channels.db import database_sync_to_async


TEST_CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

# this is decorated with a mark which sets metadata on each of the test methods contained within


async def test_can_connect_to_server(self, settings):
    settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
    communicator = WebsocketCommunicator(
        application=application,
        path='/taxiapp/'
    )
    connected, _ = await communicator.connect()
    message = {
        'type': "echo.message",
        'data': 'This is a test message'
    }
    await communicator.send_json_to(message)
    response = await communicator.receive_json_from()
    assert response == message
    await communicator.disconnect()


async def test_can_send_and_receive_broadcast_messages(self, settings):
    settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
    communicator = WebsocketCommunicator(
        application=application,
        path='/taxi/'
    )
    connected, _ = await communicator.connect()
    message = {
        'type': 'echo.message',
        'data': 'This is a test message.',
    }
    channel_layer = get_channel_layer()
    await channel_layer.group_send('test', message=message)
    response = await communicator.receive_json_from()
    assert response == message
    await communicator.disconnect()


async def test_cannot_connect_to_socket(self, settings):
    settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
    communicator = WebsocketCommunicator(
        application=application,
        path='/taxi/'
    )
    connected, _ = await communicator.connect()
    assert connected is False


@database_sync_to_async
def create_user(username, password, group='rider'):

    # Create user.
    user = get_user_model().objects.create_user(
        username=username,
        password=password
    )
    # Create user group.
    user_group, _ = Group.objects.get_or_create(name=group)  # new
    user.groups.add(user_group)
    user.save()
    # Create access token.
    access = AccessToken.for_user(user)
    return user, access


async def test_request_trip(self, settings):
    settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
    user, access = await create_user(
        'test.user@example.com', 'pAssw0rd', 'rider'
    )
    communicator = WebsocketCommunicator(
        application=application,
        path=f'/taxi/?token={access}'
    )
    connected, _ = await communicator.connect()
    await communicator.send_json_to({
        'type': 'create.trip',
        'data': {
            'pick_up_address': '123 Main Street',
            'drop_off_address': '456 Piney Road',
            'rider': user.id,
        },
    })
    response = await communicator.receive_json_from()
    response_data = response.get('data')
    assert response_data['id'] is not None
    assert response_data['pick_up_address'] == '123 Main Street'
    assert response_data['drop_off_address'] == '456 Piney Road'
    assert response_data['status'] == 'REQUESTED'
    assert response_data['rider']['username'] == user.username
    assert response_data['driver'] is None
    await communicator.disconnect()
