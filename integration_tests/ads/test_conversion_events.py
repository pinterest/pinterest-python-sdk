"""
Test Conversion Model
"""
import os as _os
from integration_tests.base_test import BaseTestCase
from integration_tests.config import DEFAULT_AD_ACCOUNT_ID

from pinterest.client import PinterestSDKClient
from pinterest.ads.conversion_events import Conversion

from openapi_generated.pinterest_client.exceptions import ApiException

class TestSendConversionEvent(BaseTestCase):
    """
    Test send Conversion Event
    """

    def test_send_conversion_success(self):
        """
        Test send ConversionEvent successfully
        """
        client = PinterestSDKClient.create_client_with_token(_os.environ.get('CONVERSION_ACCESS_TOKEN'))

        NUMBER_OF_CONVERSION_EVENTS = 2
        raw_user_data = dict(
            em = ["964bbaf162703657e787eb4455197c8b35c18940c75980b0285619fe9b8acec8"] #random hash256
        )
        raw_custom_data = dict()

        conversion_events = [
            Conversion.create_conversion_event(
                event_name = "add_to_cart",
                action_source = "app_ios",
                event_time = 1670026573,
                event_id = "eventId0001",
                user_data = raw_user_data,
                custom_data= raw_custom_data,
            )
            for _ in range(NUMBER_OF_CONVERSION_EVENTS)
        ]

        response = Conversion.send_conversion_events(
            client = client,
            ad_account_id = DEFAULT_AD_ACCOUNT_ID,
            conversion_events = conversion_events,
            test = True,
        )

        assert response
        assert response.num_events_received == 2
        assert response.num_events_processed == 2
        assert len(response.events) == 2

        assert response.events[0].status == "processed"
        assert response.events[0].error_message == ""

        assert response.events[1].status == "processed"
        assert response.events[1].error_message == ""

    def test_send_conversion_fail(self):
        """
        Test send ConversionEvent fail with non-hashed email
        """
        client = PinterestSDKClient.create_client_with_token(_os.environ.get('CONVERSION_ACCESS_TOKEN'))

        NUMBER_OF_CONVERSION_EVENTS = 2
        raw_user_data = dict(
            em = ["test_non_hashed_email@pinterest.com"]
        )
        raw_custom_data = dict()

        conversion_events = [
            Conversion.create_conversion_event(
                event_name = "add_to_cart",
                action_source = "app_ios",
                event_time = 1670026573,
                event_id = "eventId0001",
                user_data = raw_user_data,
                custom_data = raw_custom_data,
            )
            for _ in range(NUMBER_OF_CONVERSION_EVENTS)
        ]

        with self.assertRaises(ApiException):
            Conversion.send_conversion_events(
                client = client,
                ad_account_id = DEFAULT_AD_ACCOUNT_ID,
                conversion_events = conversion_events,
                test = True,
            )


