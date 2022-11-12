"""
Ads high level model
"""
from __future__ import annotations

from pinterest.generated.client.api.ads_api import AdsApi

from pinterest.generated.client.model.ad_response import AdResponse
from pinterest.generated.client.model.ad_create_request import AdCreateRequest
from pinterest.generated.client.model.creative_type import CreativeType
from pinterest.generated.client.model.entity_status import EntityStatus
from pinterest.generated.client.model.ad_update_request import AdUpdateRequest

from pinterest.client import PinterestSDKClient
from pinterest.utils.error_handling import verify_api_response
from pinterest.utils.base_model import PinterestBaseModel

class Ad(PinterestBaseModel):
    # pylint: disable=R0903,duplicate-code
    """
    Ad model used to view, create, update its attributes
    """
    def __init__(
        self,
        ad_account_id:str,
        ad_id:str,
        client:PinterestSDKClient=None,
        **kwargs
        ) -> None:
        """
        Initialize an Ad object.

        Args:
            ad_account_id (str): Ad's Ad Account ID.
            ad_id (str): Ad ID, must be associated with the Ad Account ID provided in the path.
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Defaults to default_api_client.
        """
        PinterestBaseModel.__init__(
            self,
            _id=str(ad_id),
            generated_api=AdsApi,
            generated_api_get_fn="ads_get",
            generated_api_get_fn_args={"ad_account_id": ad_account_id, "ad_id": ad_id},
            model_attribute_types = AdResponse.openapi_types,
            client=client,
        )
        self._ad_account_id = str(ad_account_id)
        self._populate_fields(**kwargs)

    @classmethod
    def create(cls,
               ad_account_id:str,
               ad_group_id:str,
               creative_type:str,
               pin_id:str,
               is_pin_deleted:bool = False,
               is_removable:bool = True,
               status:str = "ACTIVE",
               android_deep_link:str = None,
               carousel_android_deep_links:list[str] = None,
               carousel_destination_urls:list[str] = None,
               carousel_ios_deep_links:list[str] = None,
               click_tracking_url:str = None,
               destination_url:str = None,
               ios_deep_link:str = None,
               name:str = None,
               tracking_urls:dict = None,
               view_tracking_url:str = None,
               client:PinterestSDKClient = None,
               **kwargs
               ) -> Ad:
        # pylint: disable=too-many-locals,too-many-arguments
        """
        Create a new ad. Request must contain ad_group_id, creative_type, and the source Pin pin_id.

        Args:
            ad_account_id (str): Campaign's Ad Account ID.
            ad_group_id (str): ID of the ad group that contains the ad.
            creative_type (str): Ad creative type enum. Enum: `"REGULAR"` `"VIDEO"` `"SHOPPING"`
                        `"CAROUSEL"` `"MAX_VIDEO"` `"SHOP_THE_PIN"` `"IDEA"`
            pin_id (str): ID of the pin used to make the ad.
            status (str): Entity status of the ad. Enum: `"ACTIVE"` `"PAUSED"` `"ARCHIVED"`
            is_pin_deleted (bool): Is original pin deleted?
            is_removable (bool): Is pin repinnable?
            android_deep_link (str, optional): Deep link URL for Android devices. Not currently
                        available. Using this field will generate an error. Defaults to None.
            carousel_android_deep_links (list[str], optional): List of deep links for the carousel pin on
                        Android. Defaults to None.
            carousel_destination_urls (list[str], optional): List of destination URLs for the carousel
                        pin to promote. Defaults to None.
            carousel_ios_deep_links (list[str], optional): List of deep links for the carousel pin on iOS.
                        Defaults to None.
            click_tracking_url (str, optional): Tracking url for the ad clicks. Defaults to None.
            destination_url (str, optional): Destination URL. Defaults to None.
            ios_deep_link (str, optional): Deep link URL for iOS devices. Not currently available. Using
                        this field will generate an error.Defaults to None.
            name (str, optional): Name of the ad - 255 chars max.
                        Defaults to None.
            tracking_urls (dict, optional): Third-party tracking URLs.<br> Python <dict> with the format:
                        {"<a href="https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event">Tracking
                        event enum</a>":[URL string array],...}<br> For example: {"impression":
                        ["URL1", "URL2"], "click": ["URL1", "URL2", "URL3"]}.<br>Up to three tracking
                        URLs are supported for each event type. Tracking URLs set at the ad group
                        or ad level can override those set at the campaign level.
                        Pass in an empty object - {} - to remove tracking URLs.<br><br> For more
                        information, see \
                        <a href="https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking"
                        target="_blank">Third-party and dynamic tracking</a>. Defaults to None.
            view_tracking_url (str, optional): Tracking URL for ad impressions. Defaults to None.
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Defaults to default_api_client.

        Returns:
            Ad: The newly created Ad.
        """
        # pylint: disable=too-many-arguments

        creative_type=CreativeType(creative_type)
        status=EntityStatus(status)

        if not client:
            client = cls._get_client()

        api_response = AdsApi(client).ads_create(
            ad_account_id=str(ad_account_id),
            ad_create_request=[AdCreateRequest(
                ad_account_id=str(ad_account_id),
                ad_group_id=str(ad_group_id),
                creative_type=creative_type,
                pin_id=str(pin_id),
                status=status,
                is_pin_deleted=is_pin_deleted,
                is_removable=is_removable,
                android_deep_link=android_deep_link,
                carousel_android_deep_links=carousel_android_deep_links,
                carousel_destination_urls=carousel_destination_urls,
                carousel_ios_deep_links=carousel_ios_deep_links,
                click_tracking_url=click_tracking_url,
                destination_url=destination_url,
                ios_deep_link=ios_deep_link,
                name=name,
                tracking_urls=tracking_urls,
                view_tracking_url=view_tracking_url,
                 **kwargs,
            )],
            )
        verify_api_response(api_response)
        ad_data = api_response.items[0].data
        return Ad(ad_account_id=ad_data.ad_account_id, ad_id=ad_data.id, client=client)

    @classmethod
    def get_all(
        cls,
        ad_account_id : str,
        campaign_ids : list[str] = None,
        ad_group_ids : list[str] = None,
        ad_ids : list[str] = None,
        entity_statuses : list[str] = None,
        page_size : int = None,
        order : str = "ASCENDING",
        bookmark : str = None,
        client : PinterestSDKClient = None,
        **kwargs
    ) -> tuple[list[Ad], str]:
        # pylint: disable=too-many-arguments,too-many-locals
        """
        List ads that meet the filters provided:
          - Listed campaign ids or ad group ids or ad ids
          - Listed entity statuses <p/>
        If no filter is provided, all ads in the ad account are returned.

        NOTE:
        Provide only campaign_id or ad_group_id or ad_id. Do not provide more than one type.
        Review status is provided for each ad; if review_status is REJECTED, the rejected_reasons field will
        contain additional information.
        For more, see https://policy.pinterest.com/en/advertising-guidelines Pinterest advertising standards.

        Args:
            ad_account_id (str): Ad Account ID
            campaign_ids (list[str], optional): List of Campaign IDs to use to filter the results
            ad_group_ids (list[str], optional): List of Ad Group IDs to use to filter the results
            ad_ids (list[str], optional): List of Ad IDs to use to filter the results
            entity_statuses (list[str], optional): Possible Entity Statuses "ACTIVE", "PAUSED" or "ARCHIVED". Defaults
                                                to None.
            page_size (int[1..100], optional): Maximum number of items to include in a single page of the response.
                                    See documentation on Pagination for more information. Defaults to None which will
                                    return all campaigns.
            order (str, optional): The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
                                Note that higher-value IDs are associated with more-recently added items. Defaults to
                                "ASCENDING".
            bookmark (str, optional): Cursor used to fetch the next page of items. Defaults to None.
            client (ApiClient): ApiClient Object

        Returns:
            list[Ad]: List of Ad Objects
            str: Bookmark for pagination if present, else None.
        """
        if ad_ids:
            kwargs["ad_ids"] = [",".join(ad_ids)]
        if campaign_ids:
            kwargs['campaign_ids'] = [",".join(campaign_ids)]
        if ad_group_ids:
            kwargs["ad_group_ids"] = [",".join(ad_group_ids)]
        if entity_statuses:
            kwargs["entity_statuses"] = entity_statuses
        if page_size:
            kwargs["page_size"] = page_size
        if order:
            kwargs['order'] = order
        if bookmark:
            kwargs['bookmark'] = bookmark

        raw_ad_list = []
        return_bookmark = None

        if not client:
            client = cls._get_client()

        ads_api = AdsApi(api_client=client)
        api_response = ads_api.ads_list(
            ad_account_id=ad_account_id,
            **kwargs
            )
        verify_api_response(api_response)

        raw_ad_list += api_response.get('items')
        return_bookmark = api_response.get('bookmark')

        if not page_size:
            while return_bookmark:
                kwargs['bookmark'] = return_bookmark
                api_response = ads_api.ads_list(
                    ad_account_id=ad_account_id,
                    **kwargs
                    )
                verify_api_response(api_response)
                raw_ad_list += api_response.get('items')
                return_bookmark = api_response.get('bookmark')

        if len(raw_ad_list) == 0:
            return None, None

        ad_list = [
            Ad(
                ad_account_id=ad_account_id,
                ad_id=ad.get('id'),
                client=client,
                _model_data=ad
                )
            for ad in raw_ad_list
            ]
        return ad_list, return_bookmark

    def update_fields(self, **kwargs) -> bool:
        """
        Update Ad fields suing any arguments

        Returns:
            bool: If Ad fields were updated successfully
        """
        if "creative_type" in kwargs:
            kwargs["creative_type"] = CreativeType(kwargs["creative_type"])
        if "status" in kwargs:
            kwargs["status"] = EntityStatus(kwargs["status"])

        api_response = self._generated_api.ads_update(
            ad_account_id=self._ad_account_id,
            ad_update_request=[AdUpdateRequest(
                id=self._id,
                **kwargs
            )]
         )
        verify_api_response(api_response)

        self._populate_fields()

        for arg, value in kwargs.items():
            if getattr(self, f'_{arg}') != value:
                raise AssertionError(f"Expected {arg} is {value}"
                + f" Actual value is {getattr(self, f'_{arg}')}")

        return True
