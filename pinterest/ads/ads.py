"""
Ads high level model
"""
from __future__ import annotations

<<<<<<< HEAD
from datetime import date

from openapi_generated.pinterest_client.model.ads_analytics_targeting_type import AdsAnalyticsTargetingType
from openapi_generated.pinterest_client.model.conversion_report_attribution_type import ConversionReportAttributionType
from openapi_generated.pinterest_client.api.ads_api import AdsApi
=======
from openapi_generated.pinterest_client.api.ads_api import AdsApi

>>>>>>> d1f7acc (Change generated client package name and version (#52))
from openapi_generated.pinterest_client.model.ad_response import AdResponse
from openapi_generated.pinterest_client.model.ad_create_request import AdCreateRequest
from openapi_generated.pinterest_client.model.creative_type import CreativeType
from openapi_generated.pinterest_client.model.entity_status import EntityStatus
from openapi_generated.pinterest_client.model.ad_update_request import AdUpdateRequest

from pinterest.client import PinterestSDKClient
from pinterest.utils.base_model import PinterestBaseModel
from pinterest.utils.bookmark import Bookmark
from pinterest.utils.analytics import AnalyticsResponse, AnalyticsUtils


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
        PinterestBaseModel.__init__(
            self,
            _id=str(ad_id),
            generated_api=AdsApi,
            generated_api_get_fn="ads_get",
            generated_api_get_fn_args={"ad_account_id": ad_account_id, "ad_id": ad_id},
            model_attribute_types = AdResponse.openapi_types,
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
            map_fn=lambda obj: obj.items[0].data
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

    def get_analytics(
        self,
        start_date: date,
        end_date: date,
        columns: list[str],
        granularity: str,
        click_window_days: int = 30,
        engagement_window_days: int = 30,
        view_window_days: int = 1,
        conversion_report_time: str = "TIME_OF_AD_ACTION",
        **kwargs
    ) -> AnalyticsResponse:
        """
        Get analytics for the specified ads in the specified ad_account_id, filtered by the specified options.

        - The token's user_account must either be the Owner of the specified ad account, or have one of the necessary
        roles granted to them via Business Access: Admin, Analyst, Campaign Manager.


        Args:
            start_date (date): Metric report start date (UTC). Format: YYYY-MM-DD.
            end_date (date): Metric report end date (UTC). Format: YYYY-MM-DD.
            columns (list[str]): Columns to retrieve, encoded as a comma-separated string. NOTE: Any metrics defined as
                MICRO_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000,
                or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of
                the advertiser's currency.For example, if the advertiser's currency is GBP (British pound sterling),
                all MICRO_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).If a column has no value,
                it may not be returned
            granularity (str): Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"
                TOTAL - metrics are aggregated over the specified date range.
                DAY - metrics are broken down daily.
                HOUR - metrics are broken down hourly.
                WEEKLY - metrics are broken down weekly.
                MONTHLY - metrics are broken down monthly
            click_window_days (int, optional):
                Default: 30
                Enum: 1 7 30 60
                Example: click_window_days=1
                Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest
                Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified,
                defaults to 30 days.
            engagement_window_days (int, optional):
                Default: 30
                Enum: 1 7 30 60
                Number of days to use as the conversion attribution window for an engagement action. Engagements include
                saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics.
                Prior conversion tags use their defined attribution windows. If not specified, defaults to 30 days.
            view_window_days (int, optional):
                Default: 1
                Enum: 1 7 30 60
                Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag
                conversion metrics. Prior conversion tags use their defined attribution windows. If not specified,
                defaults to 1 day.
            conversion_report_time (str, optional):
                Default: "TIME_OF_AD_ACTION"
                Enum: "TIME_OF_AD_ACTION" "TIME_OF_CONVERSION"
                Example: conversion_report_time=TIME_OF_AD_ACTION
                The date by which the conversion metrics returned from this endpoint will be reported. There are two
                dates associated with a conversion event: the date that the user interacted with the ad, and the date
                that the user completed a conversion event.

        Returns:
            AnalyticsResponse: AnalyticsResponse object.
        """
        kwargs['ad_account_id'] = self.ad_account_id
        kwargs['ad_ids'] = [self.id]
        kwargs['start_date'] = start_date
        kwargs['end_date'] = end_date
        kwargs['columns'] = columns
        kwargs['granularity'] = granularity
        kwargs['click_window_days'] = click_window_days
        kwargs['engagement_window_days'] = engagement_window_days
        kwargs['view_window_days'] = view_window_days
        kwargs['conversion_report_time'] = conversion_report_time

        return AnalyticsUtils.get_entity_analytics(
            params=kwargs,
            api=AdsApi,
            analytics_fn=AdsApi.ads_analytics,
            entity=Ad,
            client=self._client
        )

    def get_targeting_analytics(
        self,
        start_date: date,
        end_date: date,
        targeting_types: list[str],
        columns: list[str],
        granularity: str,
        click_window_days: int = 30,
        engagement_window_days: int = 30,
        view_window_days: int = 1,
        conversion_report_time: str = "TIME_OF_AD_ACTION",
        attribution_types: str = None,
        **kwargs
    ) -> AnalyticsResponse:
        """
        Get targeting analytics for one or more ads. For the requested ad(s) and metrics, the response will include the
        requested metric information (e.g. SPEND_IN_DOLLAR) for the requested target type (e.g. "age_bucket") for
        applicable values (e.g. "45-49").
        The token's user_account must either be the Owner of the specified ad account, or have one of the necessary
        roles granted to them via Business Access: Admin, Analyst, Campaign Manager.
        Args:
            start_date (date): Metric report start date (UTC). Format: YYYY-MM-DD
            end_date (date): Metric report end date (UTC). Format: YYYY-MM-DD
            targeting_types (list[str]): Targeting type breakdowns for the report. The reporting per targeting type
                is independent from each other.
            columns (list[str]): Columns to retrieve, encoded as a comma-separated string. NOTE: Any metrics defined as
                MICRO_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000,
                or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of
                the advertiser's currency. For example, if the advertiser's currency is GBP (British pound sterling),
                all MICRO_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound). If a column has no
                value, it may not be returned
            granularity (str): Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"
                TOTAL - metrics are aggregated over the specified date range.
                DAY - metrics are broken down daily.
                HOUR - metrics are broken down hourly.
                WEEKLY - metrics are broken down weekly.
                MONTHLY - metrics are broken down monthly
            click_window_days (int, optional): Default: 30
                Enum: 1 7 30 60
                Example: click_window_days=1
                Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest
                Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified,
                defaults to 30 days.
            engagement_window_days (int, optional): Default: 30
                Enum: 1 7 30 60
                Number of days to use as the conversion attribution window for an engagement action. Engagements
                include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion
                metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to
                30 days.
            view_window_days (int, optional): Default: 1
                Enum: 1 7 30 60
                Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag
                conversion metrics. Prior conversion tags use their defined attribution windows. If not specified,
                defaults to 1 day.
            conversion_report_time (str, optional): Default: "TIME_OF_AD_ACTION"
                Enum: "TIME_OF_AD_ACTION" "TIME_OF_CONVERSION"
                Example: conversion_report_time=TIME_OF_AD_ACTION
                The date by which the conversion metrics returned from this endpoint will be reported. There are two
                dates associated with a conversion event: the date that the user interacted with the ad, and the date
                that the user completed a conversion event.
            attribution_types (str): Enum: "INDIVIDUAL" "HOUSEHOLD"
                Example: attribution_types=INDIVIDUAL
                List of types of attribution for the conversion report
        Returns:
            AnalyticsResponse: AnalyticsResponse object.
        """
        kwargs['ad_account_id'] = self.ad_account_id
        kwargs['ad_ids'] = [self.id]
        kwargs['start_date'] = start_date
        kwargs['end_date'] = end_date
        kwargs['targeting_types'] = [AdsAnalyticsTargetingType(targeting_type) for targeting_type in targeting_types]
        kwargs['columns'] = columns
        kwargs['granularity'] = granularity
        kwargs['click_window_days'] = click_window_days
        kwargs['engagement_window_days'] = engagement_window_days
        kwargs['view_window_days'] = view_window_days
        kwargs['conversion_report_time'] = conversion_report_time

        if attribution_types:
            kwargs['attribution_types'] = ConversionReportAttributionType(attribution_types)

        return AnalyticsUtils.get_entity_analytics(
            params=kwargs,
            api=AdsApi,
            analytics_fn=AdsApi.ad_targeting_analytics_get,
            entity=Ad,
            client=self._client
        )
