"""
AdAccount Class for Pinterest Python SDK
"""
from __future__ import annotations
from datetime import date

from pinterest.generated.client.model.country import Country
from pinterest.generated.client.model.ad_account_owner import AdAccountOwner
from pinterest.generated.client.model.currency import Currency

from pinterest.generated.client.api.ad_accounts_api import AdAccountsApi
from pinterest.generated.client.model.ad_account import AdAccount as GeneratedAdAccount
from pinterest.generated.client.model.ad_account_create_request import AdAccountCreateRequest

from pinterest.client import PinterestSDKClient
from pinterest.ads.campaigns import Campaign
from pinterest.ads.audiences import Audience
from pinterest.ads.customer_lists import CustomerList
from pinterest.utils.base_model import PinterestBaseModel
from pinterest.utils.bookmark import Bookmark
from pinterest.utils.analytics import AnalyticsResponse, AnalyticsUtils


class AdAccount(PinterestBaseModel):
    """
    Ad Account model used to create, update its attributes and list its different entities.
    """

    def __init__(
        self,
        ad_account_id:str,
        client=None,
        **kwargs
        ) -> None:
        """
        Initialize an object of an AdAccount.

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Defaults to `default_api_client`.
        """

        self._id = None
        self._name = None
        self._owner = None
        self._country = None
        self._currency = None
        self._permissions = None

        PinterestBaseModel.__init__(
            self,
            _id=str(ad_account_id),
            generated_api=AdAccountsApi,
            generated_api_get_fn="ad_accounts_get",
            generated_api_get_fn_args={"ad_account_id": ad_account_id},
            model_attribute_types=GeneratedAdAccount.openapi_types,
            client=client,
        )
        self._populate_fields(**kwargs)

    @property
    def id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._id

    @property
    def name(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._name

    @property
    def owner(self) -> AdAccountOwner:
        # pylint: disable=missing-function-docstring
        return self._owner

    @property
    def country(self) -> Country:
        # pylint: disable=missing-function-docstring
        return self._country

    @property
    def currency(self) -> Currency:
        # pylint: disable=missing-function-docstring
        return self._currency

    @property
    def permissions(self) -> list[str]:
        # pylint: disable=missing-function-docstring
        return self._permissions

    @classmethod
    def create(
            cls,
            name:str,
            owner_user_id:str,
            country:str,
            client:PinterestSDKClient = None,
            **kwargs
    ) -> AdAccount:
        """
        Create a new ad account. Different ad accounts can support different currencies, payment methods, etc.
        An ad account is needed to create campaigns, ad groups, and ads; other accounts (your employees or partners)
        can be assigned business access and appropriate roles to access an ad account. <p/>
        You can set up up to 50 ad accounts per user. (The user must have a business account to\
            create an ad account.)<p/>
        For more, see <a class="reference external" href=\
            "https://help.pinterest.com/en/business/article/create-an-advertiser-account">\
                Create an advertiser account</a>.

        Args:
            name (str): Ad Account name
            owner_user_id (str): Ad Account's owning user ID
            country (str): Country ID from ISO 3166-1 alpha-2. Example: "US" or "RU".
            client (PinterestSDKClient): PinterestSDKClient Object

        Keyword Args:
            Any valid keyword arguments or query parameters for endpoint.

        Returns:
            AdAccount: AdAccount Object
        """
        response = cls._create(
            params={
                "ad_account_create_request": AdAccountCreateRequest(
                    country=Country(country),
                    name=name,
                    owner_user_id=owner_user_id,
                    **kwargs
                )
            },
            api=AdAccountsApi,
            create_fn=AdAccountsApi.ad_accounts_create,
        )
        return cls(ad_account_id=response.id, client=cls._get_client(client))

    def list_campaigns(
            self,
            campaign_ids:list[str] = None,
            entity_statuses:list[str] = None,
            page_size:int = None,
            order:str = "ASCENDING",
            bookmark:str = None,
            **kwargs
    ) -> tuple[list[Campaign], Bookmark]:
        # pylint: disable=too-many-arguments
        """
        Get a list of the campaigns in the specified <code>ad_account_id</code>, filtered by the specified options.
        - The token's user_account must either be the Owner of the specified ad account, or have one of the necessary\
            roles granted to them via\
                <a href="https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts">\
                    Business Access</a>: Admin, Analyst, Campaign Manager.

        Args:
            campaign_ids (list[str], optional): List of Campaign Ids to use to filter the results. Defaults to None.
            entity_statuses (list[str], optional): Possible Entity Statuses "ACTIVE", "PAUSED" or "ARCHIVED". Defaults
                                                   to None.
            page_size (int[1..100], optional): Maximum number of items to include in a single page of the response.
                                               See documentation on Pagination for more information. Defaults to None
                                               which will return default number of campaigns.
            order (str, optional): The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
                                   Note that higher-value IDs are associated with more-recently added items. Defaults to
                                   "ASCENDING".
            bookmark (str, optional): Cursor used to fetch the next page of items. Defaults to None.

        Keyword Args:
            Any valid keyword arguments or query parameters for endpoint.

        Returns:
            list[Campaign]: List of Campaign Objects
            Bookmark: Bookmark for pagination if present, else None.
        """
        return Campaign.get_all(
            client=self._client,
            ad_account_id=self._id,
            campaign_ids=campaign_ids,
            entity_statuses=entity_statuses,
            page_size=page_size,
            order=order,
            bookmark=bookmark,
            **kwargs
        )

    def list_audiences(
        self,
        entity_statuses:list[str] = None,
        page_size:int = None,
        order:str = "ASCENDING",
        bookmark:str = None,
        **kwargs
    ) -> tuple[list[Audience], Bookmark]:
        # pylint: disable=too-many-arguments
        """
        Get a list of the audiences in the AdAccount, filtered by the specified arguments

        Args:
            entity_statuses (list[str], optional): Possible Entity Statuses "ACTIVE", "PAUSED" or "ARCHIVED". Defaults
                                                   to None.
            page_size (int[1..100], optional): Maximum number of items to include in a single page of the response.
                                               See documentation on Pagination for more information. Defaults to None
                                               which will return default number of audiences.
            order (str, optional): The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
                                   Note that higher-value IDs are associated with more-recently added items. Defaults to
                                   "ASCENDING".
            bookmark (str, optional): Cursor used to fetch the next page of items. Defaults to None.

        Returns:
            list[Audience]: List of Audience Objects
            Bookmark: Bookmark for pagination if present, else None.
        """
        return Audience.get_all(
            client=self._client,
            ad_account_id=self._id,
            entity_statuses=entity_statuses,
            page_size=page_size,
            order=order,
            bookmark=bookmark,
            **kwargs
        )

    def list_customer_lists(
        self,
        page_size: int = None,
        order: str = None,
        bookmark: str = None,
        **kwargs
    ) -> tuple[list[CustomerList], Bookmark]:
        # pylint: disable=too-many-arguments
        """
        Get a list of customer lists in the AdAccount, filtered by the specified arguments

        Args:
            page_size (int[1..100], optional): Maximum number of items to include in a single page of the response.
                                               See documentation on Pagination for more information. Defaults to None
                                               which will return all campaigns.
            order (str, optional): The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
                                   Note that higher-value IDs are associated with more-recently added items. Defaults to
                                   "ASCENDING".
            bookmark (str, optional): Cursor used to fetch the next page of items. Defaults to None.

        Returns:
            list[CustomerList]: List of Audience Objects
            Bookmark: Bookmark for pagination if present, else None.
        """
        return CustomerList.get_all(
            ad_account_id=self._id,
            page_size=page_size,
            order=order,
            bookmark=bookmark,
            client=self._client,
            **kwargs
        )

    def get_analytics(
        self,
        start_date:date,
        end_date:date,
        columns:list[str],
        granularity:str,
        click_window_days:int=30,
        engagement_window_days:int=30,
        view_window_days:int=1,
        conversion_report_time:str="TIME_OF_AD_ACTION",
        **kwargs
    ) -> AnalyticsResponse:
        """
        Get analytics for the specified ad_account_id, filtered by the specified options.

        - The token's user_account must either be the Owner of the specified ad account, or have one of the necessary
        roles granted to them via Business Access: Admin, Analyst, Campaign Manager.

        Args:
            start_date (date): Metric report start date (UTC).
            end_date (date): Metric report end date (UTC).
            columns (list[str]): Columns to retrieve, encoded as a comma-separated string. NOTE: Any metrics defined as
                MICRO_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000,
                or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of
                the advertiser'scurrency. For example, if the advertiser's currency is GBP (British pound sterling), all
                MICRO_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound). If a column has no value,
                it may not be returned
            granularity (str): Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"
                TOTAL - metrics are aggregated over the specified date range.
                DAY - metrics are broken down daily.
                HOUR - metrics are broken down hourly.
                WEEKLY - metrics are broken down weekly.
                MONTHLY - metrics are broken down monthly
            click_window_days (int, optional): Enum: 1 7 30 60. Number of days to use as the conversion attribution
                window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use
                their defined attribution windows.. Defaults to 30.
            engagement_window_days (int, optional): Enum: 1 7 30 60 Number of days to use as the conversion attribution
                window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card
                swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution
                windows. Defaults to 30.
            view_window_days (int, optional): Enum: 1 7 30 60. Number of days to use as the conversion attribution
                window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their
                defined attribution windows. Defaults to 1.
            conversion_report_time (str, optional): Enum: "TIME_OF_AD_ACTION" "TIME_OF_CONVERSION". The date by which
                the conversion metrics returned from this endpoint will be reported. There are two dates associated
                with a conversion event: the date that the user interacted with the ad, and the date that the user
                completed a conversion event. Defaults to "TIME_OF_AD_ACTION".

        Returns:
            AnalyticsResponse: AnalyticsResponse object.
        """
        kwargs['ad_account_id'] = self.id
        kwargs['start_date'] = start_date
        kwargs['end_date'] = end_date
        kwargs['columns'] = columns
        kwargs['granularity'] = granularity
        kwargs['click_window_days'] = click_window_days
        kwargs['engagement_window_days'] = engagement_window_days
        kwargs['view_window_days'] = view_window_days
        kwargs['conversion_report_time'] = conversion_report_time

        ad_account_analytics_response = AnalyticsUtils._get_ad_entity_analytics(
            params=kwargs,
            api=AdAccountsApi,
            analytics_fn=AdAccountsApi.ad_account_analytics,
            ad_entity=AdAccount,
            client=self._client
        )

        return ad_account_analytics_response
