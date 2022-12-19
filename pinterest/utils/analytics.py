"""
Analytics Class for Pinterest Python SDK
"""
from __future__ import annotations

from pinterest.utils.validations import AdsEntityType

class AnalyticsUtils():
    """
    Utility class with functions to make model specific analytics api calls.
    """
    @classmethod
    def get_ad_entity_analytics(cls):
        # added as an example placeholder
        pass


class AnalyticsResponse():
    """
    AnalyticsResponse model
    """
    def __init__(
        self,
        entity_type:str,
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
        return self._entity_type

    @property
    def fields(self) -> list[str]:
        return self._fields

    @property
    def raw_response(self) -> dict:
        return self._raw_response

    def __str__(self) -> str:
        return f"{self.raw_response}"
