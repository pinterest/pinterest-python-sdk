"""
Conversion Class for Pinterest Python SDK
"""
from __future__ import annotations

from openapi_generated.pinterest_client.api.conversion_tags_api import ConversionTagsApi
from openapi_generated.pinterest_client.model.entity_status import EntityStatus
from openapi_generated.pinterest_client.model.conversion_tag_type import ConversionTagType
from openapi_generated.pinterest_client.model.conversion_tag_create import ConversionTagCreate
from openapi_generated.pinterest_client.model.conversion_tag_configs import ConversionTagConfigs
from openapi_generated.pinterest_client.model.conversion_tag_response import ConversionTagResponse
from openapi_generated.pinterest_client.model.conversion_event_response import ConversionEventResponse
from openapi_generated.pinterest_client.model.enhanced_match_status_type import EnhancedMatchStatusType

from pinterest.client import PinterestSDKClient
from pinterest.utils.bookmark import Bookmark
from pinterest.utils.base_model import PinterestBaseModel
from pinterest.utils.error_handling import verify_api_response

class ConversionTag(PinterestBaseModel):
    # pylint: disable=too-few-public-methods, too-many-arguments, duplicate-code
    """
    Conversion Tag model used to view, create, update its attributes and list its different entities
    """
    def __init__(
        self,
        ad_account_id : str,
        conversion_tag_id : str,
        client : PinterestSDKClient = None,
        **kwargs
    ) -> None:
        """
        Initialize Conversion Tag Object.

        Args:
            ad_account_id (str): ConversionTag's Ad Account ID
            conversion_tag_id (str): ConversionTag ID, must be associated with Ad Account ID provided
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Uses the default client, if not provided.
        """
        self._id = None
        self._ad_account_id = None
        self._code_snippet =  None
        self._enhanced_match_status = None
        self._last_fired_time_ms = None
        self._name = None
        self._status = None
        self._version = None
        self._configs = None

        PinterestBaseModel.__init__(
            self,
            _id = str(conversion_tag_id),
            generated_api = ConversionTagsApi,
            generated_api_get_fn = "conversion_tags_get",
            generated_api_get_fn_args={"ad_account_id": ad_account_id, "conversion_tag_id": conversion_tag_id},
            model_attribute_types = ConversionTagResponse.openapi_types,
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
    def code_snippet(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._code_snippet

    @property
    def enhanced_match_status(self) -> EnhancedMatchStatusType:
        # pylint: disable=missing-function-docstring
        return self._enhanced_match_status

    @property
    def last_fired_time_ms(self) -> float:
        # pylint: disable=missing-function-docstring
        return self._last_fired_time_ms

    @property
    def name(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._name

    @property
    def status(self) -> EntityStatus:
        # pylint: disable=missing-function-docstring
        return self._status

    @property
    def version(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._version

    @property
    def configs(self) -> ConversionTagConfigs:
        # pylint: disable=missing-function-docstring
        return self._configs

    @classmethod
    def create(
        cls,
        ad_account_id : str,
        name : str,
        aem_enabled : bool = None,
        md_frequency : float = None,
        aem_fnln_enabled : bool = None,
        aem_ph_enabled : bool = None,
        aem_ge_enabled : bool = None,
        aem_db_enabled : bool = None,
        aem_loc_enabled : bool = None,
        client:PinterestSDKClient = None,
        **kwargs
    ) -> ConversionTag:
        # pylint: disable=too-many-locals,too-many-arguments
        """
        Create a conversion tag, also known as\
        <a href=\"https://help.pinterest.com/en/business/article/set-up-the-pinterest-tag\"\\
        target=\"_blank\">Pinterest tag</a>
        with the option to enable enhance match.<p/>

        The Pinterest Tag tracks actions people take on the ad account\u2019\
        s website after they view the ad account's ad on Pinterest. The advertiser\
        needs to customize this tag to track conversions.<p/>

        For more information,\
        see:<p/>

        <a class=\"reference external\" \
        href=\"https://help.pinterest.com/en/business/article/set-up-the-pinterest-tag\"\
        >Set up the Pinterest tag</a><p/>

        <a class=\"reference external\" href=\"\
        https://developers.pinterest.com/docs/conversions/pinterest-tag/\">Pinterest\
        Tag</a><p/>

        <a class=\"reference external\" href=\"https://developers.pinterest.com/docs/conversions/enhanced-match/\"\
        >Enhanced match</a>"

        Args:
            ad_account_id (str): ConversionTag's Ad Account ID
            name (str): ConversionTag name
            aem_enabled (bool=False, Nullable): Whether Automatic Enhanced Match email is enabled. See\
            Enhanced match for more information.

            md_frequency (float=1.0, Nullable): Metadata ingestion frequency.
            aem_fnln_enabled (bool=False, Nullable): Whether Automatic Enhanced Match name is enabled. See\
            Enhanced match for more information.

            aem_ph_enabled (bool=False, Nullable): Whether Automatic Enhanced Match phone is enabled. See\
            Enhanced match for more information.

            aem_ge_enabled (bool=False, Nullable): Whether Automatic Enhanced Match gender is enabled. See\
            Enhanced match for more information.

            aem_db_enabled (bool=False, Nullable): Whether Automatic Enhanced Match birthdate is enabled. See\
            Enhanced match for more information.

            aem_loc_enabled (bool=False, Nullable): Whether Automatic Enhanced Match location is enabled. See\
            Enhanced match for more information.

        Returns:
            ConversionTag: ConversionTag Object
        """
        response = cls._create(
            params = {
                "ad_account_id" : str(ad_account_id),
                "conversion_tag_create" : ConversionTagCreate(
                    name = name,
                    aem_enabled = aem_enabled,
                    md_frequency = md_frequency,
                    aem_fnln_enabled = aem_fnln_enabled,
                    aem_ph_enabled = aem_ph_enabled,
                    aem_ge_enabled = aem_ge_enabled,
                    aem_db_enabled = aem_db_enabled,
                    aem_loc_enabled = aem_loc_enabled,
                    **kwargs
                )
            },
            api = ConversionTagsApi,
            create_fn = ConversionTagsApi.conversion_tags_create,
            map_fn = lambda obj : obj,
            client=cls._get_client(client),
        )


        return cls(
            ad_account_id = response.ad_account_id,
            conversion_tag_id = response.id,
            client = cls._get_client(client),
        )

    @classmethod
    def get_all(
        cls,
        ad_account_id : str,
        filter_deleted : bool = False,
        client : PinterestSDKClient = None,
        **kwargs,
    ) -> list[ConversionTag]:
        """
        Get a list of ConversionTag, filter by specified arguments

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            filter_deleted (bool=False, optional): Filter out deleted tags.
            client (_type_, optional): PinterestSDKClient Object. Uses the default client, if not provided.

        Returns:
            list[ConversionTag]: List of ConversionTags
        """
        params = {"ad_account_id" : str(ad_account_id), "filter_deleted": filter_deleted}

        def _map_function(obj):
            return ConversionTag(
                ad_account_id = str(ad_account_id),
                conversion_tag_id = obj.get('id'),
                client = client,
                _model_data = obj.to_dict()
            )

        return cls._list(
            params = params,
            api = ConversionTagsApi,
            list_fn = ConversionTagsApi.conversion_tags_list,
            map_fn = _map_function,
            client = client,
            **kwargs,
        )[0] #This method doesn't have bookmark

    @classmethod
    def get_page_visit_conversion_tag_events(
        cls,
        ad_account_id : str,
        page_size : int = None,
        order : str = "ASCENDING",
        bookmark : str = None,
        client : PinterestSDKClient = None,
        **kwargs
    ) -> tuple[list[ConversionEventResponse], Bookmark]:
        """
        Get page visit conversion tag events for an ad account.

        Args:
            ad_account (str): Ad Account ID
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Uses the default client, if not provided.

        Returns:
            list[ConversionEventResponse]: List of ConversionTagEvent
        """
        params = {"ad_account_id" : str(ad_account_id)}

        def _map_function(obj):
            return ConversionEventResponse(
                conversion_event = ConversionTagType(obj.get("conversion_event")),
                conversion_tag_id = str(obj.get("conversion_tag_id")),
                ad_account_id = str(obj.get("ad_account_id")),
                created_time = int(obj.get("created_time")),
            )

        return cls._list(
            params = params,
            page_size = page_size,
            order = order,
            bookmark = bookmark,
            api = ConversionTagsApi,
            list_fn = ConversionTagsApi.page_visit_conversion_tags_get,
            map_fn = _map_function,
            client = client,
            **kwargs,
        )

    @classmethod
    def get_ocpm_eligible_conversion_tag_events(
        cls,
        ad_account_id : str,
        client : PinterestSDKClient = None,
        **kwargs
    ) -> tuple[str, list[ConversionEventResponse]]:
        """
        Get OCPM eligible conversion tag events for an Ad Account.

        Args:
            ad_account_id (str): Ad Account ID
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Uses the default client, if not provided.

        Returns:
            list[ConversionEventResponse]: List of ConversionTagEvent
        """
        api_response = ConversionTagsApi(api_client=cls._get_client(client)).ocpm_eligible_conversion_tags_get(
            ad_account_id = str(ad_account_id),
            **kwargs,
        )

        verify_api_response(api_response)

        # Convert to dict to get the property name
        dict_response = api_response.to_dict()
        if len(dict_response) == 0:
            return None, None

        property_name = list(dict_response.keys())[0]

        # Access through $api_response to get original types of conversion tag events
        conversion_tag_events = api_response[property_name]

        return property_name, conversion_tag_events
