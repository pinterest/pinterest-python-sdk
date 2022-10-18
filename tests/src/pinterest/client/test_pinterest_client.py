"""
PinterestClientTest tests
"""
import unittest


class PinterestClientTest(unittest.TestCase):
    """
    PinterestClientTest tests
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from pinterest.client import default_sdk_client
        self._default_api_client = default_sdk_client

    def test_instance(self):
        """
        test_instance
        """
        from pinterest.client import default_sdk_client as _default_api_client

        self.assertEqual(id(self._default_api_client), id(_default_api_client))
        self.assertEqual(self._default_api_client, _default_api_client)
        self.assertEqual(self._default_api_client.configuration.host, _default_api_client.configuration.host)
        self.assertEqual(
            self._default_api_client.configuration.access_token,
            _default_api_client.configuration.access_token
        )
