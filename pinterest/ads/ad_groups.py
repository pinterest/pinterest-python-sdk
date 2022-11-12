"""
High level module class for AdGroup object
"""
from __future__ import annotations

from pinterest.generated.client.api.ad_groups_api import AdGroupsApi

from pinterest.generated.client.model.action_type import ActionType
from pinterest.generated.client.model.budget_type import BudgetType
from pinterest.generated.client.model.ad_group_response import AdGroupResponse
from pinterest.generated.client.model.ad_group_create_request import AdGroupCreateRequest
from pinterest.generated.client.model.ad_group_update_request import AdGroupUpdateRequest

from pinterest.client import PinterestSDKClient
from pinterest.utils.base_model import PinterestBaseModel
from pinterest.utils.error_handling import verify_api_response
from pinterest.ads.ads import Ad


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
        billable_event = ActionType(billable_event)
        if not client:
            client = cls._get_client()

        api_response = AdGroupsApi(client).ad_groups_create(
            ad_account_id=str(ad_account_id),
            ad_group_create_request=[AdGroupCreateRequest(
                ad_account_id = str(ad_account_id),
                name = name,
                campaign_id = str(campaign_id),
                billable_event = billable_event,
                budget_in_micro_currency = budget_in_micro_currency,
                bid_in_micro_currency = bid_in_micro_currency,
                start_time = start_time,
                end_time = end_time,
                tracking_url = tracking_url,
                auto_targeting_enabled = auto_targeting_enabled,
                **kwargs
            )],
        )

        verify_api_response(api_response)
        ad_group_data = api_response.items[0].data

        return AdGroup(ad_account_id=ad_group_data.ad_account_id, ad_group_id=ad_group_data.id, client=client)

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

        api_response = self._generated_api.ad_groups_update(
            ad_account_id=self._ad_account_id,
            ad_group_update_request=[AdGroupUpdateRequest(
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
    ) -> tuple[list[AdGroup], str]:
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
            tuple[list[AdGroup], str]: _description_
        """
        if ad_group_ids:
            kwargs["ad_group_ids"] = [",".join(ad_group_ids)]
        if campaign_ids:
            kwargs['campaign_ids'] = [",".join(campaign_ids)]
        if entity_statuses:
            kwargs["entity_statuses"] = entity_statuses
        if page_size:
            kwargs["page_size"] = page_size
        if order:
            kwargs['order'] = order
        if bookmark:
            kwargs['bookmark'] = bookmark

        raw_ad_group_list = []
        return_bookmark = None
        if not client:
            client = cls._get_client()

        ad_groups_api = AdGroupsApi(api_client=client)
        api_response = ad_groups_api.ad_groups_list(
            ad_account_id=ad_account_id,
            **kwargs
            )
        verify_api_response(api_response)

        raw_ad_group_list += api_response.get('items')
        return_bookmark = api_response.get('bookmark')

        if not page_size:
            while return_bookmark:
                kwargs['bookmark'] = return_bookmark
                api_response = ad_groups_api.ad_groups_list(
                    ad_account_id=ad_account_id,
                    **kwargs
                    )
                verify_api_response(api_response)
                raw_ad_group_list += api_response.get('items')
                return_bookmark = api_response.get('bookmark')

        if len(raw_ad_group_list) == 0:
            return None, None

        ad_group_list = [
            AdGroup(
                ad_account_id=ad_account_id,
                ad_group_id=ad_group.get('id'),
                client=client,
                _model_data=ad_group
                )
            for ad_group in raw_ad_group_list
            ]
        return ad_group_list, return_bookmark

    def list_ads(
        self,
        ad_ids : list[str] = None,
        entity_statuses : list[str] = None,
        page_size : int = None,
        order : str = "ASCENDING",
        bookmark : str = None,
        **kwargs
    ) -> tuple[list[Ad], str]:
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
            tuple[list[Ad], str]: _description_
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
