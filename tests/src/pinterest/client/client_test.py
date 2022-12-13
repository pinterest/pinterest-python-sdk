import os
from unittest import mock
from unittest.mock import patch
import unittest
import subprocess

from pinterest.client import PinterestSDKClient


class ClientTest(unittest.TestCase):

    def test_set_default_access_token(self):
        os.unsetenv("PINTEREST_ACCESS_TOKEN")
        sample_access_token = 'test_token'
        PinterestSDKClient.set_default_access_token(sample_access_token)
        client = PinterestSDKClient.create_default_client()
        self.assertEqual(sample_access_token, client.configuration.access_token)

    @mock.patch.dict(
        os.environ,
        {
            "PINTEREST_REFRESH_ACCESS_TOKEN": "test_refresh_token",
            "PINTEREST_APP_ID": "test_app_id",
            "PINTEREST_APP_SECRET": "test_app_secret",
         },
        clear=True
    )
    @patch('dotenv.load_dotenv')
    def test_set_default_refresh_token(self, load_dotenv_mock):
        load_dotenv_mock.return_value = None

        refresh_token = 'refresh_token'
        app_id = '12345'
        app_secret = '123456asdfg'

        from pinterest.config import PINTEREST_REFRESH_ACCESS_TOKEN
        from pinterest.config import PINTEREST_APP_ID
        from pinterest.config import PINTEREST_APP_SECRET
        self.assertNotEqual(refresh_token, PINTEREST_REFRESH_ACCESS_TOKEN)
        self.assertNotEqual(app_id, PINTEREST_APP_ID)
        self.assertNotEqual(app_secret, PINTEREST_APP_SECRET)

        PinterestSDKClient.set_default_refresh_token(
            refresh_token=refresh_token,
            app_id=app_id,
            app_secret=app_secret
        )

        from pinterest.config import PINTEREST_REFRESH_ACCESS_TOKEN
        from pinterest.config import PINTEREST_APP_ID
        from pinterest.config import PINTEREST_APP_SECRET
        self.assertEqual(refresh_token, PINTEREST_REFRESH_ACCESS_TOKEN)
        self.assertEqual(app_id, PINTEREST_APP_ID)
        self.assertEqual(app_secret, PINTEREST_APP_SECRET)
