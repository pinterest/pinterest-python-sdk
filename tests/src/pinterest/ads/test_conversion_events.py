from unittest import TestCase
from unittest.mock import patch

from openapi_generated.pinterest_client.model.conversion_api_response import ConversionApiResponse
from openapi_generated.pinterest_client.model.conversion_api_response_events import ConversionApiResponseEvents

from pinterest.ads.conversion_events import Conversion

class TestConversionEvent(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_ad_account_id = "777777777777"

    @patch('pinterest.ads.conversion_events.ConversionEventsApi.events_create')
    def test_send_conversion_event_success(self, create_mock):
        """
        Test if ConversionEvent can be sent to Pinterest API
        """
        create_mock.return_value = ConversionApiResponse(
            num_events_received = 2,
            num_events_processed = 2,
            events = [
                ConversionApiResponseEvents(
                    status="processed",
                    error_message = "",
                    warning_message = "",
                ),
                ConversionApiResponseEvents(
                    status="processed",
                    error_message = "",
                    warning_message = "",
                )
            ]
        )

        NUMBER_OF_CONVERSION_EVENTS = 2
        raw_user_data = dict(
            em = ["964bbaf162703657e787eb4455197c8b35c18940c75980b0285619fe9b8acec8"] #random hash256
        )
        conversion_events = [
            Conversion.create_conversion_event(
                event_name = "add_to_cart",
                action_source = "app_ios",
                event_time = 1670026573,
                event_id = "eventId0001",
                user_data = raw_user_data,
            )
            for _ in range(NUMBER_OF_CONVERSION_EVENTS)
        ]

        response = Conversion.send_conversion_events(
            ad_account_id = self.test_ad_account_id,
            conversion_events = conversion_events,
            test = True,
        )

        assert response
        assert response.num_events_received == 2
        assert response.num_events_processed == 2
        assert len(response.events) == 2

        assert response.events[0].status == "processed"
        assert response.events[0].error_message == ""
        assert response.events[0].warning_message == ""

        assert response.events[1].status == "processed"
        assert response.events[1].error_message == ""
        assert response.events[1].warning_message == ""