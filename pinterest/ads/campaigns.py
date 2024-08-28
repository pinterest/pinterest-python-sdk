"""
Campaign Class for Pinterest Python SDK
"""
from __future__ import annotations

from openapi_generated.pinterest_client.api.campaigns_api import CampaignsApi

from openapi_generated.pinterest_client.model.campaign_response import CampaignResponse
from openapi_generated.pinterest_client.model.campaign_create_request import CampaignCreateRequest
from openapi_generated.pinterest_client.model.campaign_update_request import CampaignUpdateRequest

from openapi_generated.pinterest_client.model.objective_type import ObjectiveType

from pinterest.ads.ad_groups import AdGroup
from pinterest.client import PinterestSDKClient
from pinterest.utils.error_handling import verify_api_response
from pinterest.utils.base_model import PinterestBaseModel
from pinterest.utils.bookmark import Bookmark


class Campaign(PinterestBaseModel):

    """
    Campaign model used to view, create, update its attributes and list its different entities.
    """
    def __init__(
        self,
        ad_account_id:str,
        campaign_id:str,
        client:PinterestSDKClient=None,
        **kwargs
        ) -> None:
        """
        Initialize a Campaign object.

        Args:
            ad_account_id (str): Campaign's Ad Account ID.
            campaign_id (str): Campaign ID, must be associated with the Ad Account ID provided in the path.
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Uses the default client, if not provided.
        """

        self._id = None
        self._ad_account_id = None
        self._name = None
        self._status = None
        self._lifetime_spend_cap = None
        self._daily_spend_cap = None
        self._order_line_id = None
        self._tracking_urls = None
        self._start_time = None
        self._end_time = None
        self._objective_type = None
        self._created_time = None
        self._updated_time = None
        self._type = None
        self._is_flexible_daily_budgets = None
        self._is_campaign_budget_optimization = None
        self._summary_status = None

        PinterestBaseModel.__init__(
            self,
            _id=str(campaign_id),
            generated_api=CampaignsApi,
            generated_api_get_fn="campaigns_get",
            generated_api_get_fn_args={"ad_account_id": ad_account_id, "campaign_id": campaign_id},
            model_attribute_types = CampaignResponse.openapi_types,
            client=client,
            )
        self._ad_account_id = str(ad_account_id)
        self._populate_fields(**kwargs)

    @property
    def id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._id

    @property
    def ad_account_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._ad_account_id

    @property
    def name(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._name

    @property
    def status(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._status

    @property
    def lifetime_spend_cap(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._lifetime_spend_cap

    @property
    def daily_spend_cap(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._daily_spend_cap

    @property
    def order_line_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._order_line_id

    @property
    def tracking_urls(self) -> dict:
        # pylint: disable=missing-function-docstring
        return self._tracking_urls

    @property
    def start_time(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._start_time

    @property
    def end_time(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._end_time

    @property
    def objective_type(self) -> ObjectiveType:
        # pylint: disable=missing-function-docstring
        return self._objective_type

    @property
    def created_time(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._created_time

    @property
    def updated_time(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._updated_time

    @property
    def type(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._type

    @property
    def is_flexible_daily_budgets(self) -> bool:
        # pylint: disable=missing-function-docstring
        return self._is_flexible_daily_budgets

    @property
    def is_campaign_budget_optimization(self) -> bool:
        # pylint: disable=missing-function-docstring
        return self._is_campaign_budget_optimization

    @property
    def summary_status(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._summary_status


    @classmethod
    def create(
        cls,
        ad_account_id:str,
        name:str,
        objective_type:str,
        status:str = 'ACTIVE',
        lifetime_spend_cap:int = None,
        daily_spend_cap:int = None,
        order_line_id:int = None,
        tracking_urls:str = None,
        start_time:int = None,
        end_time:int = None,
        is_campaign_budget_optimization:bool = False,
        is_flexible_daily_budgets:bool = False,
        default_ad_group_budget_in_micro_currency:int = None,
        is_automated_campaign:bool = False,
        client:PinterestSDKClient = None,
        **kwargs
    ) -> Campaign:
        # pylint: disable=too-many-locals,too-many-arguments,duplicate-code
        """
        Create a new campaign. Every campaign has its own campaign_id\
        and houses one or more ad groups, which contain one or more ads.

        For more,\
        see <a href=\"https://help.pinterest.com/en/business/article/set-up-your-campaign/\">
        Set up your campaign</a>. <p/>

        <strong>Note:</strong>

        - The values for\
        'lifetime_spend_cap' and 'daily_spend_cap' are microcurrency amounts based\
        on the currency field set in the advertiser's profile. (e.g. USD) <p/>

        <p>Microcurrency is used to track very small transactions, based on the currency\
         set in the advertiser\u2019s profile.</p>

        <p>A microcurrency unit is 10^(-6)\
         of the standard unit of currency selected in the advertiser\u2019s profile.</p>

        <p><strong>Equivalency equations</strong>, using dollars as an example currency:</p>

        <ul>

        <li>$1 = 1,000,000 microdollars</li>

        <li>1 microdollar = $0.000001</li>

        </ul>

        <p><strong>To convert between currency and microcurrency</strong>,\
        using dollars as an example currency:</p>

        <ul>

        <li>To convert dollars\
        to microdollars, mutiply dollars by 1,000,000</li>

        <li>To convert microdollars\
        to dollars, divide microdollars by 1,000,000</li>

        </ul>

        Args:
            ad_account_id (str): Campaign's Ad Account ID.
            name (str): Campaign name.
            objective_type (ObjectiveType): Campaign objective type. Enum: `"AWARENESS"`, `"CONSIDERATION"`,
                                            `"VIDEO_VIEW"`, `"WEB_CONVERSION"`, `"CATALOG_SALES"`, `"WEB_SESSIONS"`
            status (str, optional): _description_. Defaults to 'ACTIVE'.
            lifetime_spend_cap (int, optional): Campaign total spending cap. Defaults to None.
            daily_spend_cap (int, optional): Campaign daily spending cap. Defaults to None.
            order_line_id (int, optional): Order line ID that appears on the invoice.
                                           Defaults to None.
            tracking_urls (str, optional): Third-party tracking URLs.<br> Python <dict> with the format:
                        {"<a href="https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event">Tracking
                        event enum</a>":[URL string array],...}<br> For example: {"impression":
                        ["URL1", "URL2"], "click": ["URL1", "URL2", "URL3"]}.<br>Up to three tracking
                        URLs are supported for each event type. Tracking URLs set at the ad group
                        or ad level can override those set at the campaign level.
                        Pass in an empty object - {} - to remove tracking URLs.<br><br> For more
                        information, see \
                        <a href="https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking"
                        target="_blank">Third-party and dynamic tracking</a>. Defaults to None.
            start_time (int, optional): Campaign start time. Unix timestamp in seconds. Only used
                                        for Campaign Budget Optimization (CBO) campaigns. Defaults to None.
            end_time (int, optional): Campaign end time. Unix timestamp in seconds. Only used for
                                      Campaign Budget Optimization (CBO) campaigns. Defaults to None.
            is_campaign_budget_optimization (bool, optional): Determines if a campaign automatically
                                generate ad-group level budgets given a campaign budget to maximize
                                campaign outcome. When transitioning from non-cbo to cbo, all
                                previous child ad group budget will be cleared. Defaults to False.
            is_flexible_daily_budgets (bool, optional): Determines if a campaign has flexible
                                daily budgets setup. Defaults to False.
            default_ad_group_budget_in_micro_currency (int, optional): When transitioning from
                                campaign budget optimization to non-campaign budget optimization,
                                the default_ad_group_budget_in_micro_currency will propagate to
                                each child ad groups daily budget. Unit is micro currency
                                of the associated advertiser account. Defaults to None.
            is_automated_campaign (bool, optional): Specifies whether the campaign was created
                                in the automated campaign flow. Defaults to False.
            client (PinterestSDKClient, optional): PinterestSDKClient Object, uses the default client, if not provided.

        Keyword Args:
            Any valid keyword arguments or query parameters for endpoint.

        Returns:
             Campaign: Campaign Object
        """
        response = cls._create(
            params={
                "ad_account_id": str(ad_account_id),
                "campaign_create_request": [
                    CampaignCreateRequest(
                        ad_account_id=str(ad_account_id),
                        name=name,
                        objective_type=ObjectiveType(objective_type),
                        status=status,
                        lifetime_spend_cap=lifetime_spend_cap,
                        daily_spend_cap=daily_spend_cap,
                        order_line_id=order_line_id,
                        tracking_urls=tracking_urls,
                        start_time=start_time,
                        end_time=end_time,
                        is_campaign_budget_optimization=is_campaign_budget_optimization,
                        is_flexible_daily_budgets=is_flexible_daily_budgets,
                        default_ad_group_budget_in_micro_currency=default_ad_group_budget_in_micro_currency,
                        is_automated_campaign=is_automated_campaign,
                        **kwargs
                    )
                ]
            },
            api=CampaignsApi,
            create_fn=CampaignsApi.campaigns_create,
            map_fn=lambda obj: obj.items[0].data,
            client=cls._get_client(client),
        )

        return cls(
            ad_account_id=response.ad_account_id,
            campaign_id=response.id,
            client=cls._get_client(client)
        )

    @classmethod
    def get_all(
        cls,
        ad_account_id:str,
        campaign_ids:list[str] = None,
        entity_statuses:list[str] = None,
        page_size:int = None,
        order:str = "ASCENDING",
        bookmark:str = None,
        client:PinterestSDKClient = None,
        **kwargs
    ) -> tuple[list[Campaign], Bookmark]:
        # pylint: disable=too-many-arguments
        # pylint: disable=fixme
        """
        Get a list of the campaigns in the AdAccount, filtered by the specified arguments

        Args:
            ad_account_id (str): Campaign's Ad Account ID.
            campaign_ids (list[str], optional): List of Campaign Ids to use to filter the results. Defaults to None.
            entity_statuses (list[str], optional): Possible Entity Statuses "ACTIVE", "PAUSED" or "ARCHIVED". Defaults
                                                to None.
            page_size (int[1..100], optional): Maximum number of items to include in a single page of the response.
                                    See documentation on Pagination for more information. Defaults to None which will
                                    return default page size campaigns.
            order (str, optional): The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
                                Note that higher-value IDs are associated with more-recently added items. Defaults to
                                "ASCENDING".
            bookmark (str, optional): Cursor used to fetch the next page of items. Defaults to None.
            client (PinterestSDKClient): PinterestSDKClient Object

        Keyword Args:
            Any valid keyword arguments or query parameters for endpoint.

        Returns:
            list[Campaign]: List of Campaign Objects
            Bookmark: Bookmark for pagination if present, else None.
        """
        params = {"ad_account_id": ad_account_id}

        if campaign_ids:
            kwargs['campaign_ids'] = [",".join(campaign_ids)] # TODO:Change to only campaign_ids once v5 spec updated
        if entity_statuses:
            kwargs['entity_statuses'] = entity_statuses

        def _map_function(obj):
            return Campaign(
                ad_account_id=ad_account_id,
                campaign_id=obj.get('id'),
                client=client,
                _model_data=obj
            )

        return cls._list(
            params=params,
            page_size=page_size,
            order=order,
            bookmark=bookmark,
            api=CampaignsApi,
            list_fn=CampaignsApi.campaigns_list,
            map_fn=_map_function,
            client=client,
            **kwargs
        )

    def set_lifetime_budget(self, new_spend_cap:int) -> bool:
        """
        Set new life time spend cap budget for the campaign.

        Args:
            new_spend_cap (int): The new campaign total spending cap.

        Returns:
            bool: If the lifetime budget was changed successfully
        """
        api_response = self._generated_api.campaigns_update(
            ad_account_id=self._ad_account_id,
            campaign_update_request=CampaignUpdateRequest(
                id=self._id,
                ad_account_id=self._ad_account_id,
                lifetime_spend_cap=new_spend_cap
                )
            )
        verify_api_response(api_response)

        self._populate_fields()

        return getattr(self, '_lifetime_spend_cap') == new_spend_cap

    def set_daily_budget(self, new_spend_cap:int) -> bool:
        """
        Set new daily spend cap budget for the campaign.

        Args:
            new_spend_cap (int): The new campaign daily spending cap.

        Returns:
            bool: If the daily budget was changed successfully
        """
        api_response = self._generated_api.campaigns_update(
            ad_account_id=self._ad_account_id,
            campaign_update_request=[CampaignUpdateRequest(
                id=self._id,
                ad_account_id=self._ad_account_id,
                daily_spend_cap=new_spend_cap
                )]
            )
        verify_api_response(api_response)

        self._populate_fields()

        return getattr(self, '_daily_spend_cap') == new_spend_cap

    def get_lifetime_budget(self) -> float:
        """
        Get the current life time spend cap budget of the campaign.

        Returns:
            float: Current life time spend cap budget
        """
        return getattr(self, '_lifetime_spend_cap')

    def get_daily_budget(self) -> float:
        """
        Get the current daily spend cap budget of the campaign.

        Returns:
            float: Current daily spend cap budget
        """
        return getattr(self, '_daily_spend_cap')

    def _change_status(self, new_status:str) -> bool:
        """
        Helper function to change status of campaign to `new_status`

        Args:
            new_status (str): New status for campaign

        Returns:
            bool: If campaign status got changed to `new_status` successfully.
        """

        if self._status == new_status:
            print(f"Campaign is already {new_status}")
            return False

        api_response = self._generated_api.campaigns_update(
            ad_account_id=self._ad_account_id,
            campaign_update_request=[CampaignUpdateRequest(
                id=self._id,
                ad_account_id=self._ad_account_id,
                status=new_status)]
            )

        verify_api_response(api_response)
        self._populate_fields()

        return getattr(self, '_status') == new_status

    def pause(self) -> bool:
        """
        Pause an active or archived campaign

        Returns:
            bool: If campaign status was successfully changed to 'PAUSED'
        """
        return self._change_status('PAUSED')

    def activate(self) -> bool:
        """
        Activate a paused or archived campaign

        Returns:
            bool: If campaign status was successfully changed to 'ACTIVE'
        """
        return self._change_status('ACTIVE')

    def archive(self) -> bool:
        """
        Archive an active or paused campaign

        Returns:
            bool: If campaign status was successfully changed to 'ARCHIVED'
        """
        return self._change_status('ARCHIVED')

    def update_fields(self, **kwargs) -> bool:
        """
        Update the campaign fields using any attributes.

        Keyword Args:
            Any valid campaign fields with valid values

        Returns:
            bool: If campaign fields were successfully updated
        """
        return self._update(
            params={
                "ad_account_id": self._ad_account_id,
                "campaign_update_request": [
                    CampaignUpdateRequest(
                        id=self._id,
                        ad_account_id=self._ad_account_id,
                        **kwargs
                    )
                ]
            },
            api=CampaignsApi,
            update_fn=CampaignsApi.campaigns_update,
            **kwargs
        )

    def list_ad_groups(
        self,
        page_size: int = 25,
        order: str = "ASCENDING",
        bookmark: str = None,
        entity_statuses: list[str] = None,
        **kwargs
        ) -> tuple(list[AdGroup], Bookmark):
        """
        List ad groups directed related to campaign.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        Args:
            page_size (int, optional): _description_. Defaults to None.
            order (str, optional): _description_. Defaults to "ASCENDING".
            bookmark (str, optional): _description_. Defaults to None.
            entity_statuses (str, optional): _description_. Defaults to None.
        Returns:
            tuple[list[AdGroup], Bookmark]: _description_
        """

        return AdGroup.get_all(
            ad_account_id=self._ad_account_id, campaign_ids=[self._id],
            entity_statuses=entity_statuses, page_size=page_size,
            order=order, bookmark=bookmark,
            **kwargs
        )
