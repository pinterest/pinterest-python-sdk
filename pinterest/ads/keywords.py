"""
High level module class for Keyword object
"""
from __future__ import annotations

from openapi_generated.pinterest_client.api.keywords_api import KeywordsApi
from openapi_generated.pinterest_client.model.match_type import MatchType
from openapi_generated.pinterest_client.model.keywords_common import KeywordsCommon
from openapi_generated.pinterest_client.model.keywords_request import KeywordsRequest
from openapi_generated.pinterest_client.model.keyword import Keyword as GeneratedKeyword
from openapi_generated.pinterest_client.model.match_type_response import MatchTypeResponse
from openapi_generated.pinterest_client.model.keyword_update_body import KeywordUpdateBody
from openapi_generated.pinterest_client.model.keyword_update import KeywordUpdate

from pinterest.client import PinterestSDKClient
from pinterest.utils.sdk_exceptions import SdkException
from pinterest.utils.base_model import PinterestBaseModel


class Keyword(PinterestBaseModel):
    # pylint: disable=too-few-public-methods,too-many-locals,too-many-arguments
    """
    High level model class to manage keywords
    """
    def __init__(self, ad_account_id, keyword_id, client=None, **kwargs):

        self._match_type = None
        self._value = None
        self._archived = None
        self._id = None
        self._parent_id = None
        self._parent_type = None
        self._type = None
        self._bid = None

        PinterestBaseModel.__init__(
            self,
            _id=str(keyword_id),
            generated_api=KeywordsApi,
            generated_api_get_fn="",
            generated_api_get_fn_args={},
            model_attribute_types=GeneratedKeyword.openapi_types,
            client=client,
            )
        self._ad_account_id = str(ad_account_id)
        self._populate_fields(**kwargs)

    @property
    def match_type(self) -> MatchTypeResponse:
        # pylint: disable=missing-function-docstring
        return self._match_type

    @property
    def value(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._value

    @property
    def archived(self) -> bool:
        # pylint: disable=missing-function-docstring
        return self._archived

    @property
    def id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._id

    @property
    def parent_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._parent_id

    @property
    def parent_type(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._parent_type

    @property
    def type(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._type

    @property
    def bid(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._bid

    @classmethod
    def create(
        cls,
        ad_account_id : str,
        parent_id : str,
        value : str,
        bid: int = None,
        match_type : str = None,
        client: PinterestSDKClient = None,
        **kwargs
    ) -> Keyword:
        # pylint: disable=too-many-locals,too-many-arguments
        """
        Create keywords for follow entity types (advertiser, campaign, ad group or ad).

        NOTE:
        - Advertisers campaigns can only be assigned keywords with excluding ('_NEGATIVE').
        - All keyword match types are available for ad groups.

        Args:
            ad_account_id (str): Ad Account ID
            parent_id (str): Keyword parent entity ID (advertiser, campaign, ad group)
            bid (float): Keyword custom bid
            match_type (str): Keyword match type, ENUM: "BOARD", "PHRASE", "EXACT", "EXACT_NEGATIVE",
                    "PHRASE_NEGATIVE", null
            value (str): Keyword value(120 chars max)

        Returns:
            Keyword: Keyword Object
        """
        # pylint: disable=line-too-long

        def map_fn(obj):
            if len(obj.keywords) == 0:
                raise SdkException(
                    status=f"Fail with error: {obj.errors[0].error_messages}",
                    )
            return obj.keywords[0]

        keyword = KeywordsCommon(
            match_type=MatchTypeResponse(match_type),
            value=value,
            bid=bid,
            **kwargs
        )

        response = cls._create(
            params={
                "ad_account_id": str(ad_account_id),
                "keywords_request": KeywordsRequest(
                    keywords=[keyword],
                    parent_id=str(parent_id),
                ),
            },
            api=KeywordsApi,
            create_fn=KeywordsApi.keywords_create,
            map_fn=map_fn,
            client=cls._get_client(client),
        )

        return cls(
            ad_account_id=ad_account_id,
            keyword_id=response.id,
            client=cls._get_client(client),
            _model_data=response.to_dict()
        )

    @classmethod
    def get_all(
        cls,
        ad_account_id: str,
        page_size: int = None,
        bookmark : str = None,
        client: PinterestSDKClient = None,
        **kwargs
    ) -> tuple[list[Keyword], str]:
        """
        Get a list of keywords bases on the filters provided.

        NOTE:
        - Advertisers campaigns can only be assigned keywords with excluding ('_NEGATIVE').
        - All keyword match types are available for ad groups.

        Args:
            ad_account_id (str): Ad Account ID.
            page_size (int[1..100], optional): Maximum number of items to include in a single page of the response.
                                    See documentation on Pagination for more information. Defaults to None which will
                                    return all campaigns.
            bookmark (str, optional): Cursor used to fetch the next page of items. Defaults to None.
            client (PinterestSDKClient, optional): Defaults to the default api client.

        Returns:
            list[Keyword]: List of Keyword Objects
            str: Bookmark for paginations if present, else None.
        """
        params = {"ad_account_id": ad_account_id}

        if "match_type" in kwargs:
            kwargs["match_type"] = MatchType(kwargs["match_type"])

        def _map_function(obj):
            return Keyword(
                ad_account_id=ad_account_id,
                keyword_id=obj.get('id'),
                client=client,
                _model_data=obj,
            )

        return cls._list(
            params=params,
            page_size=page_size,
            bookmark=bookmark,
            api=KeywordsApi,
            list_fn=KeywordsApi.keywords_get,
            map_fn=_map_function,
            client=client,
            **kwargs
        )

    def update_fields(self, **kwargs) -> bool:
        """Update keyword fields using any attributes

        Keyword Args:
            Any valid keyword fields with valid values

        Returns:
            bool: if keyword fields were successfully updated
        """
        # TODO(dfana@): replace this method logic with PinterestBaseModel._update, right now is not supported this logic
        api_response = self._generated_api.keywords_update(
            ad_account_id=self._ad_account_id,
            keyword_update_body=KeywordUpdateBody(
                keywords=[KeywordUpdate(
                    id=self._id,
                    **kwargs
                )]
            )
        )

        assert isinstance(api_response.keywords[0], GeneratedKeyword)
        self._populate_fields(_model_data=api_response.keywords[0].to_dict())

        return True
