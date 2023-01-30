"""
ProductGroupPromotion Class for Pinterest Python SDK
"""
from __future__ import annotations

from openapi_generated.pinterest_client.model.entity_status import EntityStatus
from openapi_generated.pinterest_client.model.creative_type import CreativeType

from openapi_generated.pinterest_client.api.product_group_promotions_api import ProductGroupPromotionsApi
from openapi_generated.pinterest_client.model.product_group_promotion import ProductGroupPromotion  \
    as GeneratedProductGroupPromotion

from pinterest.utils.base_model import PinterestBaseModel


class ProductGroupPromotion(PinterestBaseModel):
    """
    Product Group Promotion model used to create, update its attributes and list its different entities.
    """

    def __init__(
        self,
        ad_account_id:str,
        product_group_promotion_id:str,
        client=None,
        **kwargs
        ) -> None:
        """
        Initialize an object of an ProductGroupPromotion.

        Args:
            ad_account_id (str): Unique identifier of an ad account.
            product_group_promotion_id (str): Unique identifier of a product group promotion.
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Defaults to `default_api_client`.
        """
        self._id = None
        self._ad_group_id = None
        self._type = None
        self._bid_in_micro_currency = None
        self._included = None
        self._definition = None
        self._relative_definition = None
        self._parent_id = None
        self._slideshow_collections_title = None
        self._slideshow_collections_description = None
        self._status = None
        self._tracking_url = None
        self._catalogs_product_group_id = None
        self._catalogs_product_group_name = None
        self._creative_type = None
        self._collections_hero_pin_id = None
        self._collections_hero_destination_url = None
        self._is_mdl = None

        PinterestBaseModel.__init__(
            self,
            _id=str(ad_account_id),
            generated_api=ProductGroupPromotionsApi,
            generated_api_get_fn="ad_accounts_get",
            generated_api_get_fn_args={
                "ad_account_id": ad_account_id,
                "product_group_promotion_id": product_group_promotion_id
                },
            model_attribute_types=GeneratedProductGroupPromotion.openapi_types,
            client=client,
        )
        self._populate_fields(**kwargs)


    @property
    def id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._id
    @property
    def ad_group_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._ad_group_id
    @property
    def type(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._type
    @property
    def bid_in_micro_currency(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._bid_in_micro_currency
    @property
    def included(self) -> bool:
        # pylint: disable=missing-function-docstring
        return self._included
    @property
    def definition(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._definition
    @property
    def relative_definition(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._relative_definition
    @property
    def parent_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._parent_id
    @property
    def slideshow_collections_title(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._slideshow_collections_title
    @property
    def slideshow_collections_description(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._slideshow_collections_description
    @property
    def status(self) -> EntityStatus:
        # pylint: disable=missing-function-docstring
        return self._status
    @property
    def tracking_url(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._tracking_url
    @property
    def catalogs_product_group_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._catalogs_product_group_id
    @property
    def catalogs_product_group_name(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._catalogs_product_group_name
    @property
    def creative_type(self) -> CreativeType:
        # pylint: disable=missing-function-docstring
        return self._creative_type
    @property
    def collections_hero_pin_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._collections_hero_pin_id
    @property
    def collections_hero_destination_url(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._collections_hero_destination_url
    @property
    def is_mdl(self) -> bool:
        # pylint: disable=missing-function-docstring
        return self._is_mdl
