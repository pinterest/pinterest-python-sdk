"""
Test Pin Model
"""

from unittest import TestCase
from unittest.mock import patch

from pinterest.client import PinterestSDKClient

from pinterest.generated.client.model.pin import Pin as GeneratedPin

from pinterest.organic.pins import Pin

class TestGetPin(TestCase):
    """
    Test Pin model and its higher level functions
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        PinterestSDKClient.set_default_access_token("test_token")
        self.test_pin_id = "111111111111"

    @patch('pinterest.organic.pins.PinsApi.pins_get')
    def test_create_pins_model_using_existing_pin(self, pins_get_mock):
        """
        Test if a Pin model/object is created successfully with correct pin_id
        """
        pins_get_mock.return_value = GeneratedPin(
            title="SDK Test Pin",
            description="SDK Test Pin Description",
            )

        pin_response = Pin(
            pin_id=self.test_pin_id,
        )

        assert pin_response
        assert pin_response.title == "SDK Test Pin"
