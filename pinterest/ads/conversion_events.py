"""
Conversion Event Class for Pinterest Python SDK
"""
from __future__ import annotations

from openapi_generated.pinterest_client.model.conversion_events import ConversionEvents
from openapi_generated.pinterest_client.api.conversion_events_api import ConversionEventsApi
from openapi_generated.pinterest_client.model.conversion_events_data import ConversionEventsData
from openapi_generated.pinterest_client.model.conversion_events_user_data import ConversionEventsUserData
from openapi_generated.pinterest_client.model.conversion_events_custom_data import ConversionEventsCustomData
from openapi_generated.pinterest_client.model.conversion_api_response_events import ConversionApiResponseEvents

from pinterest.client import PinterestSDKClient
from pinterest.utils.base_model import PinterestBaseModel

class Conversion(PinterestBaseModel):
    # pylint: disable=too-many-locals
    """
    Conversion Event Model used to send conversion events to Pinterest API
    """

    @classmethod
    def create_conversion_event(
        cls,
        event_name : str,
        action_source : str,
        event_time : int,
        event_id : str,
        user_data : dict,
        custom_data : dict,
        event_source_url : str = None,
        partner_name : str = None,
        app_id : str = None,
        app_name : str = None,
        app_version : str = None,
        device_brand : str = None,
        device_carrier : str = None,
        device_model : str = None,
        device_type : str = None,
        os_version : str = None,
        language : str = None,
        **kwargs
    ) -> ConversionEventsData:
        """ Create Conversion Event Data to be sent.

        Args:
            event_name (str): The type of the user event, Enum: "add_to_cart", "checkout", "custom",
                "lead", "page_visit", "search", "signup", "view_category", "watch_video"
            action_source (str): The source indicating where the conversion event occurred, Enum:
                "app_adroid", "app_ios", "web", "offline"
            event_time (int): The time when the event happened. Unix timestamp in seconds
            event_id (str): The unique id string that identifies this event and can be used for deduping
                between events ingested via both the conversion API and Pinterest tracking
            user_data (dict): Object containing customer information data. Note, it is required at least
                one of 1) em, 2) hashed_maids or 3) pair client_ip_address + client_user_agent.
            custom_data (dict): Object containing other custom data.
            event_source_url (str, optional): URL of the web conversion event
            partner_name (str, optional): The third party partner name responsible to send the event to
                Conversion API on behalf of the adverstiser. Only send this field if Pinterest has worked
                directly with you to define a value for partner_name.
            app_id (str, optional): The app store app ID.
            app_name (str, optional): Name of the app.
            app_version (str, optional): Version of the app.
            device_brand (str, optional): Brand of the user device.
            device_carrier (str, optional): User device's model carrier.
            device_model (str, optional): Model of the user device.
            device_type (str, optional): Type of the user device.
            os_version (str, optional): Version of the device operating system.
            language (str, optional): Two-character ISO-639-1 language code indicating the user's language.

        Returns:
            ConversionEventsData: ConversionEventData to be sent
        """
        return ConversionEventsData(
            event_name = event_name,
            action_source = action_source,
            event_time = event_time,
            event_id = event_id,
            user_data = ConversionEventsUserData(**user_data),
            custom_data = ConversionEventsCustomData(**custom_data),
            event_source_url = event_source_url,
            partner_name = partner_name,
            app_id = app_id,
            app_name = app_name,
            app_version = app_version,
            device_brand = device_brand,
            device_carrier = device_carrier,
            device_model = device_model,
            device_type = device_type,
            os_version = os_version,
            language = language,
            **kwargs,
        )

    @classmethod
    def send_conversion_events(
        cls,
        ad_account_id : str,
        conversion_events : list[ConversionEventsData],
        test : bool = False,
        client : PinterestSDKClient = None,
        **kwargs,
    )-> tuple(int, int, list[ConversionApiResponseEvents]):
        """
        Send conversion events to Pinterest API for Conversions.

        Note: Highly recommend to use create_client_with_token (with Conversion Access Token) to create different
        client for this functionality.
        """
        response = ConversionEventsApi(api_client=cls._get_client(client)).events_create(
            ad_account_id = str(ad_account_id),
            conversion_events = ConversionEvents(
                data = conversion_events
                ),
            test = test,
            **kwargs,
        )

        return response
