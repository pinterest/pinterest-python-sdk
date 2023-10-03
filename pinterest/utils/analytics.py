"""
Analytics Class for Pinterest Python SDK
"""
from __future__ import annotations
from typing import Callable

from pinterest.utils.base_model import PinterestBaseModel

from pinterest.client import PinterestSDKClient


class AnalyticsUtils:
    """
    Utility class with functions to make model specific analytics api calls.
    """
    @classmethod
    def get_entity_analytics(
        cls,
        params: list,
        api: type,
        analytics_fn: Callable,
        entity: PinterestBaseModel,
        client: PinterestSDKClient = None,
        **kwargs
    ) -> AnalyticsResponse:
        """
        Helper function used to get ad entity analytics.
        Args:
            params (list): List of params
            api (type):
            analytics_fn (Callable):
            entity (PinterestBaseModel):
            client (PinterestSDKClient, optional):
        Returns:
            AnalyticsResponse:
        """

        return AnalyticsResponse(
            entity_type=entity,
            fields=params.get('columns', []),
            raw_response=getattr(api(client), analytics_fn.__name__)(**params, **kwargs)
        )


class AnalyticsResponse():
    """
    AnalyticsResponse model
    """
    def __init__(
        self,
        entity_type:PinterestBaseModel,
        fields:list[str],
        raw_response:dict,
        ) -> None:
        """
        Initialize an Ads Analytics object.
        Args:
            entity_type (PinterestBaseModel): Entity Type identifier. Enum: ad_account, campaign, ad_group, ad.
            fields (list[str]): _description_
            raw_response (dict): _description_
        """
        self._entity_type = entity_type.__name__.lower()
        self._fields = fields
        self._raw_response = raw_response

    @property
    def entity_type(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._entity_type

    @property
    def fields(self) -> list[str]:
        # pylint: disable=missing-function-docstring
        return self._fields

    @property
    def raw_response(self) -> dict:
        # pylint: disable=missing-function-docstring
        return self._raw_response

    def __str__(self) -> str:
        return f"{self.raw_response}"
