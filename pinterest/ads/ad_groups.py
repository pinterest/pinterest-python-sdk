"""
High level module class for AdGroup object
"""
from __future__ import annotations

from datetime import date

from openapi_generated.pinterest_client.model.conversion_report_attribution_type import ConversionReportAttributionType

from openapi_generated.pinterest_client.model.ads_analytics_targeting_type import AdsAnalyticsTargetingType

from openapi_generated.pinterest_client.api.ad_groups_api import AdGroupsApi

from openapi_generated.pinterest_client.model.action_type import ActionType
from openapi_generated.pinterest_client.model.budget_type import BudgetType
from openapi_generated.pinterest_client.model.ad_group_response import AdGroupResponse
from openapi_generated.pinterest_client.model.ad_group_create_request import AdGroupCreateRequest
from openapi_generated.pinterest_client.model.ad_group_update_request import AdGroupUpdateRequest

from pinterest.client import PinterestSDKClient
from pinterest.utils.base_model import PinterestBaseModel
from pinterest.ads.ads import Ad
from pinterest.utils.bookmark import Bookmark
from pinterest.utils.analytics import AnalyticsResponse, AnalyticsUtils


class AdGroup(PinterestBaseModel):
    # pylint: disable=too-few-public-methods,too-many-locals,too-many-arguments,duplicate-code
    """
    AdGroup model used to view, create, update its attributes and list its different entities.
    """

    def __init__(
        self,
        ad_account_id:str,
        ad_group_id:str,
        client=None,
        **kwargs
        ) -> None:
        """
        Initialize an AdGroup object.

        Args:
            ad_account_id (str): AdGroup's Ad Account ID.
            ad_group_id (str): AdGroup ID, must be associated with the Ad Account ID provided in the path.
            client (_type_, optional): PinterestSDKClient Object. Defaults to default_api_client.
        """
        self._name = None
        self._status = None
        self._budget_in_micro_currency = None
        self._bid_in_micro_currency = None
        self._bid_strategy_type = None
        self._budget_type = None
        self._start_time = None
        self._end_time = None
        self._targeting_spec = None
        self._lifetime_frequency_cap = None
        self._tracking_urls = None
        self._auto_targeting_enabled = None
        self._placement_group = None
        self._pacing_delivery_type = None
        self._campaign_id = None
        self._billable_event = None
        self._id = None
        self._ad_account_id = None
        self._created_time = None
        self._updated_time = None
        self._type = None
        self._conversion_learning_mode_type = None
        self._summary_status = None
        self._feed_profile_id = None
        self._dca_assets = None

        PinterestBaseModel.__init__(
            self,
            _id=str(ad_group_id),
            generated_api=AdGroupsApi,
            generated_api_get_fn="ad_groups_get",
            generated_api_get_fn_args={"ad_account_id": ad_account_id, "ad_group_id": ad_group_id},
            model_attribute_types = AdGroupResponse.openapi_types,
            client=client,
        )
        self._ad_account_id = str(ad_account_id)
        self._populate_fields(**kwargs)

    @property
    def name(self) -> str:
        #pylint: disable=missing-function-docstring
        return self._name

    @property
    def status(self) -> str:
        #pylint: disable=missing-function-docstring
        return self._status

    @property
    def budget_in_micro_currency(self) -> int:
        #pylint: disable=missing-function-docstring
        return self._budget_in_micro_currency

    @property
    def bid_in_micro_currency(self) -> int:
        #pylint: disable=missing-function-docstring
        return self._bid_in_micro_currency

    @property
    def bid_strategy_type(self) -> str:
        #pylint: disable=missing-function-docstring
        return self._bid_strategy_type

    @property
    def budget_type(self) -> BudgetType:
        #pylint: disable=missing-function-docstring
        return self._budget_type

    @property
    def start_time(self) -> int:
        #pylint: disable=missing-function-docstring
        return self._start_time

    @property
    def end_time(self) -> int:
        #pylint: disable=missing-function-docstring
        return self._end_time

    @property
    def targeting_spec(self) -> dict:
        #pylint: disable=missing-function-docstring
        return self._targeting_spec

    @property
    def lifetime_frequency_cap(self) -> int:
        #pylint: disable=missing-function-docstring
        return self._lifetime_frequency_cap

    @property
    def tracking_urls(self) -> dict:
        #pylint: disable=missing-function-docstring
        return self._tracking_urls

    @property
    def auto_targeting_enabled(self) -> bool:
        #pylint: disable=missing-function-docstring
        return self._auto_targeting_enabled

    @property
    def placement_group(self) -> str:
        #pylint: disable=missing-function-docstring
        return self._placement_group

    @property
    def pacing_delivery_type(self) -> str:
        #pylint: disable=missing-function-docstring
        return self._pacing_delivery_type

    @property
    def campaign_id(self) -> str:
        #pylint: disable=missing-function-docstring
        return self._campaign_id

    @property
    def billable_event(self) -> ActionType:
        #pylint: disable=missing-function-docstring
        return self._billable_event

    @property
    def id(self) -> str:
        #pylint: disable=missing-function-docstring
        return self._id

    @property
    def ad_account_id(self) -> str:
        #pylint: disable=missing-function-docstring
        return self._ad_account_id

    @property
    def created_time(self) -> int:
        #pylint: disable=missing-function-docstring
        return self._created_time

    @property
    def updated_time(self) -> int:
        #pylint: disable=missing-function-docstring
        return self._updated_time

    @property
    def type(self) -> str:
        #pylint: disable=missing-function-docstring
        return self._type

    @property
    def conversion_learning_mode_type(self) -> str:
        #pylint: disable=missing-function-docstring
        return self._conversion_learning_mode_type

    @property
    def summary_status(self) -> str:
        #pylint: disable=missing-function-docstring
        return self._summary_status

    @property
    def feed_profile_id(self) -> str:
        #pylint: disable=missing-function-docstring
        return self._feed_profile_id

    @property
    def dca_assets(self):
        #pylint: disable=missing-function-docstring
        return self._dca_assets


    @classmethod
    def create(
        cls,
        ad_account_id:str,
        name:str,
        campaign_id:str,
        billable_event:str,
        budget_in_micro_currency:int = None,
        bid_in_micro_currency:int = None,
        start_time:int = None,
        end_time:int = None,
        tracking_url:str = None,
        auto_targeting_enabled:bool = None,
        client:PinterestSDKClient = None,
        **kwargs
    ) -> AdGroup:
        """
        Create a new ad group. All ads in a given ad group will
        have the same budget, bid, run dates, targeting, and placement (search,
        browse, other). For more information, <a href=\"https://help.pinterest.com/
        en/business/article/campaign-structure\"
        target=\"_blank\"> click here</a>.</p><strong>Note:</strong>

        - 'bid_in_micro_currency'

        and 'budget_in_micro_currency' should be expressed in microcurrency amounts
        based on the currency field set in the advertiser's profile.<p/>

        <p>Microcurrency
        is used to track very small transactions, based on the currency set in the
        advertiser\u2019s profile.</p>

        <p>A microcurrency unit is 10^(-6) of the
        standard unit of currency selected in the advertiser\u2019s profile.</p>


        <p><strong>Equivalency equations</strong>, using dollars as an example currency:</p>


        <ul>

        <li>$1 = 1,000,000 microdollars</li>

        <li>1 microdollar = $0.000001</li>

        </ul>

        <p><strong>To convert between currency and microcurrency</strong>,
        using dollars as an example currency:</p>

        <ul>

        <li>To convert dollars
        to microdollars, mutiply dollars by 1,000,000</li>

        <li>To convert microdollars
        to dollars, divide microdollars by 1,000,000</li>

        </ul>

        - Ad groups belong

        to ad campaigns. Some types of campaigns (e.g. budget optimization) have
        limits on the number of ad groups they can hold. If you exceed those limits,
        you will get an error message.

        Args:
            ad_account_id (str): Campaign's Ad Account ID.
            name (str): Ad Group name.
            campaign_id (str): Campaign ID of the ad group.
            billable_event (str): Ad group billable event type.
                        Enum: "CLICKTHROUGH" "IMPRESSION" "VIDEO_V_50_MRC" "BILLABLE_ENGAGEMENT"
            budget_in_micro_currency (int, optional): Budget in micro currency. This field is **REQUIRED**
                        for non-CBO (campaign budget optimization) campaigns.  A CBO campaign automatically
                        generates ad group budgets from its campaign budget to maximize campaign
                        outcome. A CBO campaign is limited to 70 or less ad groups. Defaults to None.
            bid_in_micro_currency (int, optional): Bid price in micro currency. This field is **REQUIRED**
                        for the following campaign objective_type/billable_event combinations: AWARENESS/IMPRESSION,
                        CONSIDERATION/CLICKTHROUGH, CATALOG_SALES/CLICKTHROUGH, VIDEO_VIEW/VIDEO_V_50_MRC.
                        Defaults to None.
            start_time (int, optional): Campaign start time. Unix timestamp in seconds. Only used
                        for Campaign Budget Optimization (CBO) campaigns. Defaults to None.
            end_time (int, optional): Campaign end time. Unix timestamp in seconds. Only used for
                        Campaign Budget Optimization (CBO) campaigns. Defaults to None.
            tracking_url (str, optional): Third-party tracking URLs.<br> Python <dict> with the format:
                        {"<a href="https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event">Tracking
                        event enum</a>":[URL string array],...}<br> For example: {"impression":
                        ["URL1", "URL2"], "click": ["URL1", "URL2", "URL3"]}.<br>Up to three tracking
                        URLs are supported for each event type. Tracking URLs set at the ad group
                        or ad level can override those set at the campaign level.
                        Pass in an empty object - {} - to remove tracking URLs.<br><br> For more
                        information, see \
                        <a href="https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking"
                        target="_blank">Third-party and dynamic tracking</a>. Defaults to None.
            auto_targeting_enabled (bool, optional): Enable auto-targeting for ad group. Also known as
                        <a href="https://help.pinterest.com/en/business/article/expanded-targeting"
                        target="_blank">"expanded targeting"</a>. Defaults to None.
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Defaults to default_api_client.

        Returns:
            AdGroup: AdGroup Object
        """
        response = cls._create(
            params={
                "ad_account_id": str(ad_account_id),
                "ad_group_create_request": [
                    AdGroupCreateRequest(
                        ad_account_id=str(ad_account_id),
                        name=name,
                        campaign_id=str(campaign_id),
                        billable_event=ActionType(billable_event),
                        budget_in_micro_currency=budget_in_micro_currency,
                        bid_in_micro_currency=bid_in_micro_currency,
                        start_time=start_time,
                        end_time=end_time,
                        tracking_url=tracking_url,
                        auto_targeting_enabled=auto_targeting_enabled,
                        **kwargs
                    )
                ]
            },
            api=AdGroupsApi,
            create_fn=AdGroupsApi.ad_groups_create,
            map_fn=lambda obj: obj.items[0].data
        )
        return cls(
            ad_account_id=response.ad_account_id,
            ad_group_id=response.id,
            client=cls._get_client(client)
        )

    def update_fields(self, **kwargs) -> bool:
        """
        Update adgroup fields using any arguments

        Returns:
            bool: if adgroup fields were updated successfully
        """
        if "billable_event" in kwargs:
            kwargs["billable_event"] = ActionType(kwargs["billable_event"])
        if "budget_type" in kwargs:
            kwargs["budget_type"] = BudgetType(kwargs["budget_type"])
        return self._update(
            params={
                "ad_account_id": self._ad_account_id,
                "ad_group_update_request": [
                    AdGroupUpdateRequest(
                        id=self._id,
                        **kwargs
                    )
                ]
            },
            api=AdGroupsApi,
            update_fn=AdGroupsApi.ad_groups_update,
            **kwargs
        )

    @classmethod
    def get_all(
        cls,
        ad_account_id : str,
        campaign_ids : list[str] = None,
        ad_group_ids : list[str] = None,
        entity_statuses : list[str] = None,
        page_size : int = None,
        order : str = "ASCENDING",
        bookmark : str = None,
        client : PinterestSDKClient = None,
        **kwargs
    ) -> tuple[list[AdGroup], Bookmark]:
        """
        List ad groups based on provided campaign IDs or ad group IDs.(campaign_ids or ad_group_ids).
        <p/> <strong>Note:</strong><p/> Provide only campaign_id or ad_group_id. Do not provide both.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        Args:
            ad_account_id (str): _description_
            campaign_ids (list[str], optional): _description_. Defaults to None.
            ad_group_ids (list[str], optional): _description_. Defaults to None.
            page_size (int, optional): _description_. Defaults to None.
            order (str, optional): _description_. Defaults to "ASCENDING".
            bookmark (str, optional): _description_. Defaults to None.
            client (PinterestSDKClient, optional): _description_. Defaults to default_api_client.

        Returns:
            tuple[list[AdGroup], Bookmark]: _description_
        """
        params = {"ad_account_id": ad_account_id}

        if ad_group_ids:
            kwargs["ad_group_ids"] = [",".join(ad_group_ids)]
        if campaign_ids:
            kwargs['campaign_ids'] = [",".join(campaign_ids)]
        if entity_statuses:
            kwargs["entity_statuses"] = entity_statuses

        def _map_function(obj):
            return AdGroup(
                ad_account_id=ad_account_id,
                ad_group_id=obj.get('id'),
                client=client,
                _model_data=obj
            )

        return cls._list(
            params=params,
            page_size=page_size,
            order=order,
            bookmark=bookmark,
            api=AdGroupsApi,
            list_fn=AdGroupsApi.ad_groups_list,
            map_fn=_map_function,
            client=client,
            **kwargs
        )

    def list_ads(
        self,
        ad_ids : list[str] = None,
        entity_statuses : list[str] = None,
        page_size : int = None,
        order : str = "ASCENDING",
        bookmark : str = None,
        **kwargs
    ) -> tuple[list[Ad], Bookmark]:
        """
        Get list of ads under current AdGroup with specified arguments

        Args:
            ad_ids (list[str], optional): List of Ad IDs
            entity_statuses (list[str], optional): Possible Entity Statuses "ACTIVE", "PAUSED" or "ARCHIVED". Defaults
                                                to None.
            page_size (int[1..100], optional): Maximum number of items to include in a single page of the response.
                                    See documentation on Pagination for more information. Defaults to None which will
                                    return all campaigns.
            order (str, optional): The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
                                Note that higher-value IDs are associated with more-recently added items. Defaults to
                                "ASCENDING".
            bookmark (str, optional): Cursor used to fetch the next page of items. Defaults to None.

        Returns:
            list[Ad]: List of Ads
            Bookmark: Bookmark object
        """
        return Ad.get_all(
            ad_account_id=self._ad_account_id,
            ad_ids=ad_ids,
            entity_statuses=entity_statuses,
            page_size=page_size,
            order=order,
            bookmark=bookmark,
            client=self._client,
            **kwargs
        )

    def enable_auto_targeting(self):
        """
        Enable auto-targeting for ad group. Also known as <a
        href='https://help.pinterest.com/en/business/article/expanded-targeting'>"expanded targeting"</a>.

        Returns:
            bool: true if ad group enable auto_targeting_enabled
        """
        return self.update_fields(auto_targeting_enabled=True)

    def disable_auto_targeting(self):
        """
        Disable auto-targeting for ad group. Also known as <a
        href='https://help.pinterest.com/en/business/article/expanded-targeting'>"expanded targeting"</a>.

        Returns:
            bool: true if ad group disable auto_targeting_enabled
        """
        return self.update_fields(auto_targeting_enabled=False)

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
        Get targeting analytics for one or more ad groups. For the requested ad group(s) and metrics, the response will
        include the requested metric information (e.g. SPEND_IN_DOLLAR) for the requested target type
        (e.g. "age_bucket") for applicable values (e.g. "45-49").

            - The token's user_account must either be the Owner of the specified ad account, or have one of the
            necessary roles granted to them via Business Access: Admin, Analyst, Campaign Manager.


        Args:
            start_date (date): Metric report start date (UTC). Format: YYYY-MM-DD
            end_date (date): Metric report end date (UTC). Format: YYYY-MM-DD
            targeting_types (list[str]): Example: targeting_types=APPTYPE
                Targeting type breakdowns for the report. The reporting per targeting type is independent from
                each other.
            columns (list[str]): Example: columns=SPEND_IN_DOLLAR
                Columns to retrieve, encoded as a comma-separated string. NOTE: Any metrics defined as MICRO_DOLLARS
                returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 -
                one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's
                currency.

                For example, if the advertiser's currency is GBP (British pound sterling), all MICRO_DOLLARS fields will
                be in GBP microunits (1/1,000,000 British pound).

                If a column has no value, it may not be returned

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
                Number of days to use as the conversion attribution window for an engagement action. Engagements include
                saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics.
                Prior conversion tags use their defined attribution windows. If not specified, defaults to 30 days.
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
        kwargs['ad_group_ids'] = [self.id]
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

        return AnalyticsUtils.get_ad_entity_analytics(
            params=kwargs,
            api=AdGroupsApi,
            analytics_fn=AdGroupsApi.ad_groups_targeting_analytics_get,
            ad_entity=AdGroup,
            client=self._client
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
        Get analytics for the specified ad groups in the specified ad_account_id, filtered by the specified options.
        - The token's user_account must either be the Owner of the specified ad account, or have one of the necessary
        roles granted to them via Business Access: Admin, Analyst, Campaign Manager.
        Args:
            start_date (date): Metric report start date (UTC). Format: YYYY-MM-DD
            end_date (date): Metric report end date (UTC). Format: YYYY-MM-DD
            columns (list[str]): Columns to retrieve, encoded as a comma-separated string. NOTE: Any metrics defined as
                MICRO_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000,
                or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of
                the advertiser's currency.For example, if the advertiser's currency is GBP (British pound sterling),
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
                Number of days to use as the conversion attribution window for an engagement action. Engagements include
                saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics.
                Prior conversion tags use their defined attribution windows. If not specified, defaults to 30 days.
            engagement_window_days (int, optional): Default: 30
                Enum: 1 7 30 60
                Number of days to use as the conversion attribution window for an engagement action. Engagements include
                saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics.
                Prior conversion tags use their defined attribution windows. If not specified, defaults to 30 days.
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
        Returns:
            AnalyticsResponse: AnalyticsResponse object.
        """
        kwargs['ad_group_ids'] = [self.id]
        kwargs['start_date'] = start_date
        kwargs['end_date'] = end_date
        kwargs['columns'] = columns
        kwargs['granularity'] = granularity
        kwargs['click_window_days'] = click_window_days
        kwargs['engagement_window_days'] = engagement_window_days
        kwargs['view_window_days'] = view_window_days
        kwargs['conversion_report_time'] = conversion_report_time

        return AnalyticsUtils.get_ad_entity_analytics(
            params=kwargs,
            api=AdGroupsApi,
            analytics_fn=AdGroupsApi.ad_groups_analytics,
            ad_entity=AdGroupsApi,
            client=self._client
        )
