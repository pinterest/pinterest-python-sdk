"""
Provide helper and utility functions for Organic Endpoints Integration Testing
"""
import random

from pinterest.client import PinterestSDKClient

from pinterest.organic.boards import Board
from pinterest.organic.pins import Pin

from integration_tests.config import DEFAULT_BOARD_ID, DEFAULT_PIN_ID


def _merge_default_params_with_params(default_params, params):
    if not params:
        return default_params

    for field, new_value in params.items():
        default_params[field] = new_value

    return default_params


class BoardUtils:
    def __init__(self, client=None):
        self.test_client = client or PinterestSDKClient.create_default_client()
        self.board = Board(board_id=DEFAULT_BOARD_ID, client=client)

    def get_random_board_name(self):
        return "SDK Test Create Board {}".format(random.randint(0, 1000))

    def get_board(self):
        return self.board

    def get_board_id(self):
        return self.board.id

    def get_default_params(self):
        return dict(
            name="SDK Utils Test Board",
            description="SDK Test Board Description",
            privacy="PUBLIC",
            client=self.test_client
        )

    def create_new_board(self, **kwargs):
        return Board.create(**_merge_default_params_with_params(self.get_default_params(), kwargs))

    def delete_board(self, board_id):
        return Board.delete(board_id=board_id, client=self.test_client)


class PinUtils:
    def __init__(self, client=None):
        self.test_client = client or PinterestSDKClient.create_default_client()
        self.pin = Pin(pin_id=DEFAULT_PIN_ID, client=client)

    def get_pin(self):
        return self.pin

    def get_pin_id(self):
        return self.pin.id

    def get_default_params(self):
        return dict(
            board_id=DEFAULT_BOARD_ID,
            title="SDK Test Pin",
            description="SDK Test Pin Description",
            media_source={
                "source_type": "image_url",
                "content_type": "image/jpeg",
                "data": "string",
                'url':'https://i.pinimg.com/564x/28/75/e9/2875e94f8055227e72d514b837adb271.jpg'
                },
            client=self.test_client
        )

    def create_new_pin(self, **kwargs):
        return Pin.create(**_merge_default_params_with_params(self.get_default_params(), kwargs))

    def delete_pin(self, pin_id):
        if pin_id != DEFAULT_PIN_ID: # Make sure default pin is not being deleted
            return Pin.delete(pin_id=pin_id, client=self.test_client)
