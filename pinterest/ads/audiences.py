"""
High level module class for Audience object
"""
from __future__ import annotations


from pinterest.generated.client.api.audiences_api import AudiencesApi

from pinterest.generated.client.model.audience_create_request import AudienceCreateRequest
from pinterest.generated.client.model.audience_update_request import AudienceUpdateRequest

from pinterest.generated.client.model.audience import Audience as GeneratedAudience
from pinterest.generated.client.model.audience_rule import AudienceRule
from pinterest.generated.client.model.audience_type import AudienceType
from pinterest.generated.client.model.audience_update_operation_type import AudienceUpdateOperationType
from pinterest.generated.client.model.objective_type import ObjectiveType

from pinterest.client import PinterestSDKClient
from pinterest.utils.error_handling import verify_api_response
from pinterest.utils.base_model import PinterestBaseModel


class Audience(PinterestBaseModel):
    # pylint: disable=too-few-public-methods
    """
    High level model class to manage audiences for an AdAccount
    """
    def __init__(self, ad_account_id, audience_id, client=None, **kwargs):
        PinterestBaseModel.__init__(
            self,
            _id=str(audience_id),
            generated_api=AudiencesApi,
            generated_api_get_fn="audiences_get",
            generated_api_get_fn_args={"ad_account_id": ad_account_id, "audience_id": audience_id},
            model_attribute_types = GeneratedAudience.openapi_types,
            client=client,
            )
        self._ad_account_id = str(ad_account_id)
        self._populate_fields(**kwargs)

    @classmethod
    def create(
        cls,
        ad_account_id : str,
        name : str,
        rule : dict,
        audience_type : str,
        description : str = None,
        client: PinterestSDKClient = None,
        **kwargs
    ) -> Audience:
        # pylint: disable=too-many-arguments
        # pylint: disable=line-too-long
        """
        Create an audience you can use in targeting for specific ad groups. Targeting combines customer information
        with the ways users interact with Pinterest to help you reach specific groups of users; you can include or
        exclude specific audience_ids when you create an ad group.

        For more information, visit https://help.pinterest.com/en/business/article/audience-targeting.

        Args:
            client (PinterestSDKClient): PinterestSDKClient Object
            ad_account_id (str): Audience's Advertiser or Ad Account ID.
            name (str): Audience name.
            rule (dict): python <dict> defining targeted audience users. The keys and value formats:
                    rule_example_format = {
                    country (str): Valid countries include: "US", "CA", and "GB"
                    customer_list_id (str): Customer list ID. For CUSTOMER_LIST `audience_type`
                    engagement_domain (list[str]): The audience account's verified domain. **Required** for ENGAGEMENT `audience_type`
                    engagement_type (str): Engagement type enum. Optional for ENGAGEMENT `audience_type`. Supported values are `click`, `save`, `closeup`, `comment` and `like`. All engagements are included if this field is not set.
                    event (str): A Pinterest tag event. Optional for VISITOR `audience_type`. Possible values are `pagevisit`, `signup`, `checkout`, `viewcategory`, `search`, `addtocart`, `watchvideo`, `lead`, and `custom`. This field also accepts a partner-defined Pinterest tag event.
                    event_data: **NOT YET SUPPORTED**
                    percentage (int): Percentage should be 1-10. The targeted audience should be this % size across Pinterest.
                    pin_id (list[str]): IDs of engaged organic pins. Optional for ENGAGEMENT `audience_type`. For example, "pin_id:": ["34567"].
                    prefill (bool): Optional for VISITOR `audience_type`. If `true`, the specified rule on existing engagement data is applied to pre-populate the audience. If `false`, the audience is empty at creation time. The default is `true`.
                    retention_days (int): Number of days a Pinterest user remains in the audience. Optional for ENGAGEMENT and VISITOR `audience_type`. Accepted range is 1-540. Defaults to 180 if not specified.
                    seed_id ([str]): Audience ID(s). For ACTALIKE `audience_type`.
                    url ([str]): Optional for ENGAGEMENT or VISITOR `audience_type`. For ENGAGEMENT, it is the engaged pin's URL. For VISITOR, you can use it as a string or a {operator: value} object for filtering visitors based on conversion tag event URLs. Supported operators are [ =, !=, contains, not_contains].<br>Example 1:  "url": "http://www.myonlinestore123.com/view_item/shoe"<br>Example 2: "url": {"contains": "view_item_shoe"}.
                    visitor_source_id (str): The conversion tag ID, or the Pinterest tag ID, that you use on your website. For VISITOR `audience_type`.
                    event_source (dict): Optional for VISITOR. You can use it as a {'=': [value]}. Supported values are: web, mobile, offline.
                    ingestion_source (dict): Optional for VISITOR. You can use it as a {'=': [value]}. Supported values are: tag, mmp, file_upload, conversions_api.
                    engager_type (int): Optional for ENGAGEMENT. Engager type value should be 1-2.
                    campaign_id (list[str]): Campaign ID for engagement audience filter.
                    ad_id (list[str]): Ad ID for engagement audience filter.
                    objective_type (list[str]): Objective for engagement audience filter.
                }
            audience_type (str): Enum ("CUSTOMER_LIST" "VISITOR" "ENGAGEMENT" "ACTALIKE")

        Keyword Args:
            Any valid keyword arguments or query parameters for endpoint.

        Returns:
            Audience: Audience Object
        """

        AudienceType(audience_type)

        if not 'ad_account_id' in rule:
            rule['ad_account_id'] = ad_account_id
        if 'objective_type' in rule:
            rule['objective_type'] = ObjectiveType(rule['objective_type'])
        rule = AudienceRule(**rule)

        if not client:
            client = cls._get_client()

        api_response = AudiencesApi(client).audiences_create(
            ad_account_id=str(ad_account_id),
            audience_create_request=AudienceCreateRequest(
                ad_account_id = str(ad_account_id),
                name = name,
                rule = rule,
                audience_type = audience_type,
                description = description if description else '',
                **kwargs
                ),
            )

        return Audience(
            ad_account_id=api_response.ad_account_id,
            audience_id=api_response.id,
            client=client
            )

    @classmethod
    def get_all(
        cls,
        ad_account_id: str,
        entity_statuses: list[str] = None,
        page_size: int = None,
        order: str = "ASCENDING",
        bookmark: str = None,
        client: PinterestSDKClient = None,
        **kwargs
    ) -> tuple[list[Audience], str]:
        # pylint: disable=too-many-arguments
        # pylint: disable=duplicate-code
        """
        Get a list of the audiences in the AdAccount, filtered by the specified arguments

        Args:
            client (PinterestSDKClient): PinterestSDKClient Object
            ad_account_id (str): Audience's Advertiser ID.
            entity_statuses (list[str], optional): Possible Entity Statuses "ACTIVE", "PAUSED" or "ARCHIVED". Defaults
                                                to None.
            page_size (int[1..100], optional): Maximum number of items to include in a single page of the response.
                                    See documentation on Pagination for more information. Defaults to None which will
                                    return default number of audiences.
            order (str, optional): The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
                                Note that higher-value IDs are associated with more-recently added items. Defaults to
                                "ASCENDING".
            bookmark (str, optional): Cursor used to fetch the next page of items. Defaults to None.

        Keyword Args:
            Any valid keyword arguments or query parameters for endpoint.

        Returns:
            campaign_list (list[Audience]): List of Audience Objects
            bookmark (str): Bookmark for pagination if present, else None.
        """
        if entity_statuses:
            kwargs['entity_statuses'] = entity_statuses
        if page_size:
            kwargs['page_size'] = page_size
        if order:
            kwargs['order'] = order
        if bookmark:
            kwargs['bookmark'] = bookmark

        raw_audience_list = []
        return_bookmark = None

        if not client:
            client = cls._get_client()

        audiences_api = AudiencesApi(api_client=client)
        api_response = audiences_api.audiences_list(
            ad_account_id=ad_account_id,
            **kwargs
            )
        verify_api_response(api_response)

        raw_audience_list += api_response.get('items')
        return_bookmark = api_response.get('bookmark')

        if len(raw_audience_list) == 0:
            return None, None

        audience_list = [
            Audience(
                ad_account_id=ad_account_id,
                audience_id=audience.get('id'),
                client=client,
                _model_data=audience
                )
            for audience in raw_audience_list
            ]
        return audience_list, return_bookmark

    def update_fields(self, **kwargs):
        """
        Update audience fields

        Keyword Args:
            Any valid audience fields with valid values
        """
        UPDATE_OPERATION_TYPE = AudienceUpdateOperationType("UPDATE") # DO NOT EDIT
        api_response = self._generated_api.audiences_update(
            ad_account_id=self._ad_account_id,
            audience_id=self._id,
            audience_update_request=AudienceUpdateRequest(
                ad_account_id=self._ad_account_id,
                operation_type=UPDATE_OPERATION_TYPE,
                **kwargs
            )
        )

        assert isinstance(api_response, GeneratedAudience)
        self._populate_fields()

        for arg, value in kwargs.items():
            if getattr(self, f'_{arg}') != value:
                raise AssertionError(f"Expected {arg} is {value}"
                + f" Actual value is {getattr(self, f'_{arg}')}")

        return True
