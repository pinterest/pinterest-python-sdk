"""
High level module class for Audience object
"""
from __future__ import annotations

from openapi_generated.pinterest_client.model.audience_type import AudienceType

from openapi_generated.pinterest_client.api.audiences_api import AudiencesApi

from openapi_generated.pinterest_client.model.audience_create_request import AudienceCreateRequest
from openapi_generated.pinterest_client.model.audience_update_request import AudienceUpdateRequest

from openapi_generated.pinterest_client.model.audience import Audience as GeneratedAudience
from openapi_generated.pinterest_client.model.audience_rule import AudienceRule
from openapi_generated.pinterest_client.model.audience_update_operation_type import AudienceUpdateOperationType
from openapi_generated.pinterest_client.model.objective_type import ObjectiveType

from pinterest.client import PinterestSDKClient
from pinterest.utils.base_model import PinterestBaseModel
from pinterest.utils.bookmark import Bookmark


class Audience(PinterestBaseModel):
    # pylint: disable=too-few-public-methods
    """
    High level model class to manage audiences for an AdAccount
    """
    def __init__(self, ad_account_id, audience_id, client=None, **kwargs):
        self._ad_account_id = None
        self._id = None
        self._name = None
        self._audience_type = None
        self._description = None
        self._rule = None
        self._size = None
        self._status = None
        self._type = None
        self._created_timestamp = None
        self._updated_timestamp = None
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

    @property
    def ad_account_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._ad_account_id

    @property
    def id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._id

    @property
    def name(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._name

    @property
    def audience_type(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._audience_type

    @property
    def description(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._description

    @property
    def rule(self) -> AudienceRule:
        # pylint: disable=missing-function-docstring
        return self._rule

    @property
    def size(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._size

    @property
    def status(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._status

    @property
    def type(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._type

    @property
    def created_timestamp(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._created_timestamp

    @property
    def updated_timestamp(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._updated_timestamp

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
        if 'ad_account_id' not in rule:
            rule['ad_account_id'] = ad_account_id
        if 'objective_type' in rule:
            rule['objective_type'] = ObjectiveType(rule['objective_type'])
        rule = AudienceRule(**rule)

        response = cls._create(
            params={
                "ad_account_id": str(ad_account_id),
                "audience_create_request": AudienceCreateRequest(
                    ad_account_id=str(ad_account_id),
                    name=name,
                    rule=rule,
                    audience_type=audience_type,
                    description=description if description else '',
                    **kwargs
                ),
            },
            api=AudiencesApi,
            create_fn=AudiencesApi.audiences_create,
            client=cls._get_client(client),
        )

        return cls(
            ad_account_id=response.ad_account_id,
            audience_id=response.id,
            client=cls._get_client(client)
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
    ) -> tuple[list[Audience], Bookmark]:
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
            list[Audience]: List of Audience Objects
            Bookmark: Bookmark for pagination if present, else None.
        """

        params = {"ad_account_id": ad_account_id}

        if entity_statuses:
            kwargs["entity_statuses"] = entity_statuses

        def _map_function(obj):
            return Audience(
                ad_account_id=ad_account_id,
                audience_id=obj.get('id'),
                client=client,
                _model_data=obj
            )

        return cls._list(
            params=params,
            page_size=page_size,
            order=order,
            bookmark=bookmark,
            api=AudiencesApi,
            list_fn=AudiencesApi.audiences_list,
            map_fn=_map_function,
            client=client,
            **kwargs
        )

    def update_fields(self, **kwargs):
        """
        Update audience fields

        Keyword Args:
            Any valid audience fields with valid values
        """
        # DO NOT EDIT
        UPDATE_OPERATION_TYPE = AudienceUpdateOperationType("UPDATE")
        return self._update(
            params={
                "ad_account_id": self._ad_account_id,
                "audience_id": self._id,
                "audience_update_request": AudienceUpdateRequest(
                    ad_account_id=self._ad_account_id,
                    operation_type=UPDATE_OPERATION_TYPE,
                    **kwargs
                )
            },
            api=AudiencesApi,
            update_fn=AudiencesApi.audiences_update,
            **kwargs
        )
