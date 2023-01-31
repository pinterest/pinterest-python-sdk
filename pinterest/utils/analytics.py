"""
Analytics Class for Pinterest Python SDK
"""
from __future__ import annotations
from typing import Callable

from pinterest.utils.validations import AdsEntityType
from pinterest.utils.base_model import PinterestBaseModel
<<<<<<< HEAD
=======

from pinterest.client import PinterestSDKClient

>>>>>>> c09fda9 (Ad Account `get_analytics` (#40))

from pinterest.client import PinterestSDKClient


class AnalyticsUtils:
    """
    Utility class with functions to make model specific analytics api calls.
    """
    @classmethod
<<<<<<< HEAD
<<<<<<< HEAD
    def get_entity_analytics(
        cls,
        params: list,
        api: type,
        analytics_fn: Callable,
        entity: PinterestBaseModel,
        client: PinterestSDKClient = None,
=======
    def get_ad_entity_analytics(
=======
    def get_entity_analytics(
>>>>>>> aa63ab6 (Add get pin analytic (#73))
        cls,
        params: list,
        api: type,
        analytics_fn: Callable,
<<<<<<< HEAD
        ad_entity: PinterestBaseModel,
        client:PinterestSDKClient = None,
>>>>>>> c09fda9 (Ad Account `get_analytics` (#40))
=======
        entity: PinterestBaseModel,
        client: PinterestSDKClient = None,
>>>>>>> aa63ab6 (Add get pin analytic (#73))
        **kwargs
    ) -> AnalyticsResponse:
        """
        Helper function used to get ad entity analytics.
        Args:
            params (list): List of params
            api (type):
            analytics_fn (Callable):
<<<<<<< HEAD
<<<<<<< HEAD
            entity (PinterestBaseModel):
=======
            ad_entity (PinterestBaseModel):
>>>>>>> c09fda9 (Ad Account `get_analytics` (#40))
=======
            entity (PinterestBaseModel):
>>>>>>> aa63ab6 (Add get pin analytic (#73))
            client (PinterestSDKClient, optional):
        Returns:
            AnalyticsResponse:
        """

        return AnalyticsResponse(
<<<<<<< HEAD
<<<<<<< HEAD
            entity_type=entity,
            fields=params.get('columns', []),
=======
            entity_type=ad_entity,
            fields=params.get('columns'),
>>>>>>> c09fda9 (Ad Account `get_analytics` (#40))
=======
            entity_type=entity,
            fields=params.get('columns', []),
>>>>>>> aa63ab6 (Add get pin analytic (#73))
            raw_response=getattr(api(client), analytics_fn)(**params, **kwargs)
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
            entity_type (str): Entity Type identifier. Enum: ad_account, campaign, ad_group, ad.
            fields (list[str]): _description_
            raw_response (dict): _description_
        """
        self._entity_type = AdsEntityType(entity_type).name
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