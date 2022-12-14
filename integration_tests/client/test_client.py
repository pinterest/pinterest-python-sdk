import os
import time
from unittest import mock
from unittest.mock import patch

from pinterest.utils.refresh_access_token import get_new_access_token

from pinterest import config

from pinterest.generated.client.exceptions import UnauthorizedException

from pinterest.organic.boards import Board
from pinterest.client import PinterestSDKClient
from integration_tests.base_test import BaseTestCase


class ClientTest(BaseTestCase):

    def test_bad_setup_default_access_token(self):
        sample_access_token = 'test_token'
        PinterestSDKClient.set_default_access_token(sample_access_token)
        with self.assertRaises(UnauthorizedException):
            Board.get_all()

    def test_create_custom_client_with_refresh_token(self):
        client = PinterestSDKClient.create_client_with_refresh_token(
            refresh_token=config.PINTEREST_REFRESH_ACCESS_TOKEN,
            app_id=config.PINTEREST_APP_ID,
            app_secret=config.PINTEREST_APP_SECRET
        )
        self.assertIsNotNone(Board.get_all(client=client))

    def test_client_custom_client_with_access_token(self):
        access_token = get_new_access_token(
            app_id=config.PINTEREST_APP_ID,
            app_secret=config.PINTEREST_APP_SECRET,
            refresh_access_token=config.PINTEREST_REFRESH_ACCESS_TOKEN,
            host=config.PINTEREST_API_URI,
        )
        client = PinterestSDKClient.create_client_with_token(access_token=access_token)
        self.assertIsNotNone(Board.get_all(client=client))

    def test_good_setup_default_access_token(self):

        bad_access_token = 'test_token'
        PinterestSDKClient.set_default_access_token(bad_access_token)
        with self.assertRaises(UnauthorizedException):
            Board.get_all()

        good_access_token = get_new_access_token(
            app_id=config.PINTEREST_APP_ID,
            app_secret=config.PINTEREST_APP_SECRET,
            refresh_access_token=config.PINTEREST_REFRESH_ACCESS_TOKEN,
            host=config.PINTEREST_API_URI,
        )
        PinterestSDKClient.set_default_access_token(access_token=good_access_token)
        self.assertIsNotNone(Board.get_all())









