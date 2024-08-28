"""
Ads high level model
"""
from __future__ import annotations

from openapi_generated.pinterest_client.api.ads_api import AdsApi

from openapi_generated.pinterest_client.model.ad_response import AdResponse
from openapi_generated.pinterest_client.model.ad_create_request import AdCreateRequest
from openapi_generated.pinterest_client.model.creative_type import CreativeType
from openapi_generated.pinterest_client.model.entity_status import EntityStatus
from openapi_generated.pinterest_client.model.ad_update_request import AdUpdateRequest

from pinterest.client import PinterestSDKClient
from pinterest.utils.base_model import PinterestBaseModel
from pinterest.utils.bookmark import Bookmark


class Ad(PinterestBaseModel):
    # pylint: disable=R0903,duplicate-code,R0902
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
        self._ad_group_id = None
        self._android_deep_link = None
        self._carousel_android_deep_links = None
        self._carousel_destination_urls = None
        self._carousel_ios_deep_links = None
        self._click_tracking_url = None
        self._creative_type = None
        self._destination_url = None
        self._ios_deep_link = None
        self._is_pin_deleted = None
        self._is_removable = None
        self._name = None
        self._pin_id = None
        self._status = None
        self._tracking_urls = None
        self._view_tracking_url = None
        self._ad_account_id = None
        self._campaign_id = None
        self._collection_items_destination_url_template = None
        self._created_time = None
        self._id = None
        self._rejected_reasons = None
        self._rejection_labels = None
        self._review_status = None
        self._type = None
        self._updated_time = None
        self._summary_status = None
        self._grid_click_type = None
        self._customizable_cta_type = None
        self._lead_form_id = None
        self._quiz_pin_data = None

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

    @property
    def ad_group_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._ad_group_id

    @property
    def android_deep_link(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._android_deep_link

    @property
    def carousel_android_deep_links(self) -> list[str]:
        # pylint: disable=missing-function-docstring
        return self._carousel_android_deep_links

    @property
    def carousel_destination_urls(self) -> list[str]:
        # pylint: disable=missing-function-docstring
        return self._carousel_destination_urls

    @property
    def carousel_ios_deep_links(self) -> list[str]:
        # pylint: disable=missing-function-docstring
        return self._carousel_ios_deep_links

    @property
    def click_tracking_url(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._click_tracking_url

    @property
    def creative_type(self) -> CreativeType:
        # pylint: disable=missing-function-docstring
        return self._creative_type

    @property
    def destination_url(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._destination_url

    @property
    def ios_deep_link(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._ios_deep_link

    @property
    def is_pin_deleted(self) -> bool:
        # pylint: disable=missing-function-docstring
        return self._is_pin_deleted

    @property
    def is_removable(self) -> bool:
        # pylint: disable=missing-function-docstring
        return self._is_removable

    @property
    def name(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._name

    @property
    def pin_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._pin_id

    @property
    def status(self) -> EntityStatus:
        # pylint: disable=missing-function-docstring
        return self._status

    @property
    def tracking_urls(self) -> dict:
        # pylint: disable=missing-function-docstring
        return self._tracking_urls

    @property
    def view_tracking_url(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._view_tracking_url

    @property
    def ad_account_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._ad_account_id

    @property
    def campaign_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._campaign_id

    @property
    def collection_items_destination_url_template(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._collection_items_destination_url_template

    @property
    def created_time(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._created_time

    @property
    def id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._id

    @property
    def rejected_reasons(self) -> list[str]:
        # pylint: disable=missing-function-docstring
        return self._rejected_reasons

    @property
    def rejection_labels(self) -> list[str]:
        # pylint: disable=missing-function-docstring
        return self._rejection_labels

    @property
    def review_status(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._review_status

    @property
    def type(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._type

    @property
    def updated_time(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._updated_time

    @property
    def summary_status(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._summary_status

    @property
    def grid_click_type(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._grid_click_type

    @property
    def customizable_cta_type(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._customizable_cta_type

    @property
    def lead_form_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._lead_form_id

    @property
    def quiz_pin_data(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._quiz_pin_data

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
        response = cls._create(
            params={
                "ad_account_id": str(ad_account_id),
                "ad_create_request": [
                    AdCreateRequest(
                        ad_account_id=str(ad_account_id),
                        ad_group_id=str(ad_group_id),
                        creative_type=CreativeType(creative_type),
                        pin_id=str(pin_id),
                        status=EntityStatus(status),
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
                    )
                ]
            },
            api=AdsApi,
            create_fn=AdsApi.ads_create,
            map_fn=lambda obj: obj.items[0].data,
            client=cls._get_client(client),
        )
        return cls(
            ad_account_id=response.ad_account_id,
            ad_id=response.id,
            client=cls._get_client(client)
        )

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
    ) -> tuple[list[Ad], Bookmark]:
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
            Bookmark: Bookmark for pagination if present, else None.
        """

        params = {"ad_account_id": ad_account_id}

        if ad_ids:
            kwargs["ad_ids"] = [",".join(ad_ids)]
        if campaign_ids:
            kwargs['campaign_ids'] = [",".join(campaign_ids)]
        if ad_group_ids:
            kwargs["ad_group_ids"] = [",".join(ad_group_ids)]
        if entity_statuses:
            kwargs["entity_statuses"] = entity_statuses

        def _map_function(obj):
            return Ad(
                ad_account_id=ad_account_id,
                ad_id=obj.get('id'),
                client=client,
                _model_data=obj
            )

        return cls._list(
            params=params,
            page_size=page_size,
            order=order,
            bookmark=bookmark,
            api=AdsApi,
            list_fn=AdsApi.ads_list,
            map_fn=_map_function,
            client=client,
            **kwargs
        )

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
        return self._update(
            params={
                "ad_account_id": self._ad_account_id,
                "ad_update_request": [
                    AdUpdateRequest(
                        id=self._id,
                        **kwargs
                    )
                ]
            },
            api=AdsApi,
            update_fn=AdsApi.ads_update,
            **kwargs
        )
