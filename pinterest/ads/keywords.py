"""
High level module class for Keyword object
"""
from __future__ import annotations

from pinterest.generated.client.api.keywords_api import KeywordsApi
from pinterest.generated.client.model.match_type import MatchType
from pinterest.generated.client.model.keywords_common import KeywordsCommon
from pinterest.generated.client.model.keywords_request import KeywordsRequest
from pinterest.generated.client.model.keyword import Keyword as GeneratedKeyword
from pinterest.generated.client.model.match_type_response import MatchTypeResponse
from pinterest.generated.client.model.keyword_update_body import KeywordUpdateBody
from pinterest.generated.client.model.keyword_update import KeywordUpdate

from pinterest.client import PinterestSDKClient
from pinterest.utils.error_handling import verify_api_response
from pinterest.utils.sdk_exceptions import SdkException
from pinterest.utils.base_model import PinterestBaseModel


class Keyword(PinterestBaseModel):
    # pylint: disable=too-few-public-methods,too-many-locals,too-many-arguments
    """
    High level model class to manage keywords
    """
    def __init__(self, ad_account_id, keyword_id, client=None, **kwargs):
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

        keyword = KeywordsCommon(
            match_type=MatchTypeResponse(match_type),
            value=value,
            bid=bid,
            **kwargs
        )

        if not client:
            client = cls._get_client()

        api_response = KeywordsApi(client).keywords_create(
            ad_account_id=str(ad_account_id),
            keywords_request=KeywordsRequest(
                keywords=[keyword],
                parent_id=str(parent_id),
            ),
        )

        if len(api_response.keywords) == 0:
            raise SdkException(
                status=f"Fail with error: {api_response.errors[0].error_messages}",
                )

        keyword_data = api_response.keywords[0]

        return Keyword(
            ad_account_id=ad_account_id,
            keyword_id=keyword_data.id,
            client=client,
            _model_data=keyword_data.to_dict())

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
        if page_size:
            kwargs["page_size"] = page_size
        if bookmark:
            kwargs['bookmark'] = bookmark
        if "match_type" in kwargs:
            kwargs["match_type"] = MatchType(kwargs["match_type"])

        raw_keywords = []
        return_bookmark = None
        if not client:
            client = cls._get_client()

        keywords_api = KeywordsApi(api_client=client)
        api_response = keywords_api.keywords_get(
            ad_account_id=ad_account_id,
            **kwargs
        )
        verify_api_response(api_response)

        raw_keywords += api_response.get('items')
        return_bookmark = api_response.get('bookmark')

        if not page_size:
            while return_bookmark:
                kwargs["bookmark"] = return_bookmark
                api_response = keywords_api.keywords_get(
                    ad_account_id=ad_account_id,
                    **kwargs
                )
                verify_api_response(api_response)

                raw_keywords += api_response.get('items')
                return_bookmark = api_response.get('bookmark')

        if len(raw_keywords) == 0:
            return None, None

        keywords = [
            Keyword(
                ad_account_id=ad_account_id,
                keyword_id=keyword.get('id'),
                client=client,
                _model_data=keyword,
            )
            for keyword in raw_keywords
        ]

        return keywords, return_bookmark

    def update_fields(self, **kwargs) -> bool:
        """Update keyword fields using any attributes

        Keyword Args:
            Any valid keyword fields with valid values

        Returns:
            bool: if keyword fields were successfully updated
        """
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
