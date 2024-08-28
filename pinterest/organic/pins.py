"""
Pin Class for Pinterest Python SDK
"""
from __future__ import annotations

from openapi_generated.pinterest_client.api.pins_api import PinsApi
from openapi_generated.pinterest_client.model.pin import Pin as GeneratedPin
from openapi_generated.pinterest_client.model.pin_create import PinCreate as GeneratedPinCreate
from openapi_generated.pinterest_client.model.inline_object1 import InlineObject1

from pinterest.client import PinterestSDKClient
from pinterest.utils.base_model import PinterestBaseModel
from pinterest.utils.error_handling import verify_api_response
from pinterest.utils.bookmark import Bookmark

class Pin(PinterestBaseModel):
    """
    Pin model used to view, create, update its attributes and list its different entities.
    """
    def __init__(
        self,
        pin_id:str,
        ad_account_id:str=None,
        client:PinterestSDKClient=None,
        **kwargs
        ) -> None:
        """
        Initialize or get a Pin owned by the "operation user_account" - or on a group board that
        has been shared with this account.

        By default, the "operation user_account" is the token user_account.
        Optional: Business Access: Specify an ad_account_id (obtained via List ad accounts) to use
        the owner of that ad_account as the "operation user_account". In order to do this, the token
        user_account must have one of the following Business Access roles on the ad_account:

        - For Pins on public or protected boards: Owner, Admin, Analyst, Campaign Manager.
        - For Pins on secret boards: Owner, Admin.

        Args:
            pin_id (str): Unique identifier of a Pin.
            ad_account_id (str, optional): Unique identifier of an ad account. Defaults to None.
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Uses the default client, if not provided.
        """
        self._ad_account_id = None

        self._id = None
        self._created_at = None
        self._link = None
        self._title = None
        self._description = None
        self._dominant_color = None
        self._alt_text = None
        self._board_id = None
        self._board_section_id = None
        self._board_owner = None
        self._media = None
        self._media_source = None
        self._parent_pin_id = None
        self._is_owner = None
        self._pin_metrics = None
        self._has_been_promoted = None
        self._note = None
        self._creative_type = None
        self._is_standard = None

        PinterestBaseModel.__init__(
            self,
            _id=str(pin_id),
            generated_api=PinsApi,
            generated_api_get_fn="pins_get",
            generated_api_get_fn_args={"pin_id": pin_id} \
                                    if not ad_account_id \
                                    else {"pin_id": pin_id, "ad_account_id": ad_account_id},
            model_attribute_types = GeneratedPin.openapi_types,
            client=client,
            )

        self._populate_fields(**kwargs)

    @property
    def id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._id

    @property
    def created_at(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._created_at

    @property
    def link(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._link

    @property
    def title(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._title

    @property
    def description(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._description

    @property
    def dominant_color(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._dominant_color

    @property
    def alt_text(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._alt_text

    @property
    def board_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._board_id

    @property
    def board_section_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._board_section_id

    @property
    def board_owner(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._board_owner

    @property
    def media(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._media

    @property
    def media_source(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._media_source

    @property
    def parent_pin_id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._parent_pin_id

    @property
    def is_owner(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._is_owner

    @property
    def pin_metrics(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._pin_metrics

    @property
    def has_been_promoted(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._has_been_promoted

    @property
    def note(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._note

    @property
    def creative_type(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._creative_type

    @property
    def is_standard(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._is_standard

    def __repr__(self):
        return f"{self.__class__.__name__}(pin_id={self._id}, ad_account_id={self._ad_account_id})"

    @classmethod
    def create(
        cls,
        board_id : str,
        media_source : dict,
        link : str = None,
        title : str = None,
        description : str = None,
        dominant_color : str = None,
        alt_text : str = None,
        board_section_id : str = None,
        parent_pin_id : str = None,
        client : PinterestSDKClient = None,
        **kwargs
    ) -> Pin:
        """
        Create a Pin on a board or board section owned by the "operation user_account".

        Note: If the current "operation user_account" (defined by the access token) has access
        to another user's Ad Accounts via Pinterest Business Access, you can modify your request
        to make use of the current operation_user_account's permissions to those Ad Accounts by
        including the ad_account_id in the path parameters for the request (e.g. .../?ad_account_id=12345&...).

        This function is intended solely for publishing new content created by the user. If you are interested
        in saving content created by others to your Pinterest boards, sometimes called 'curated content', please
        use our Save button (https://developers.pinterest.com/docs/add-ons/save-button) instead. For more tips on
        creating fresh content for Pinterest, review our
        Content App Solutions Guide (https://developers.pinterest.com/docs/solutions/content-apps).

        Learn more (https://developers.pinterest.com/docs/solutions/content-apps/#creatingvideopins) about
        video Pin creation

        Args:
            board_id (str): The board to which this Pin belongs.
            media_source (dict): Pin media source. In format:
                {
                'source_type': (str),
                'content_type': (str),
                'data': (str),
                'url': (str),
                'cover_image_url': (str),
                'media_id': (str),
                }
            link (str, optional): Redirect link of <= 2048 characters. Defaults to None.
            title (str, optional): Title of the pin <= 100 characters. Defaults to None.
            description (str, optional): Description of the pin <= 500 characters. Defaults to None.
            dominant_color (str, optional): Dominant pin color. Hex number, e.g. "#6E7874". Defaults to None.
            alt_text (str, optional): <= 500 characters. Defaults to None.
            board_section_id (str, optional): The board section to which this Pin belongs. Defaults to None.
            parent_pin_id (str, optional): The source pin id if this pin was saved from another pin.
                    Learn more (https://help.pinterest.com/article/save-pins-on-pinterest). Defaults to None.
            client (PinterestSDKClient, optional): PinterestSDKClient Object, uses the default client, if not provided.

        Keyword Args:
            Any valid keyword arguments or query parameters for endpoint.

        Returns:
            Pin: Pin object
        """
        # pylint: disable=too-many-arguments, no-value-for-parameter

        if not client:
            client = cls._get_client()

        api_response = PinsApi(client).pins_create(
            pin_create=GeneratedPinCreate(
                link=link,
                title=title,
                description=description,
                dominant_color=dominant_color,
                alt_text=alt_text,
                board_id=board_id,
                board_section_id=board_section_id,
                media_source=media_source,
                parent_pin_id=parent_pin_id,
            ),
            **kwargs,
        )  # pylint: disable=no-value-for-parameter
        verify_api_response(api_response)

        return Pin(pin_id=getattr(api_response, "id"), client=client)

    @classmethod
    def delete(
        cls,
        pin_id:str,
        client:PinterestSDKClient = None
    ) -> bool:
        """
        Delete a Pin owned by the "operation user_account".

        - By default, the "operation user_account" is the token user_account.

        Args:
            pin_id (str): Unique identifier of a pin.
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Uses the default client, if not provided.

        Returns:
            bool: If the pin was deleted successfully.
        """
        if not client:
            client = cls._get_client()

        api_response = PinsApi(client).pins_delete(
            pin_id=pin_id
        )
        verify_api_response(api_response)

        return True

    def save(
        self,
        board_id:str,
        board_section_id:str = None,
    ) -> None:
        """
        Save a pin on a board or board section owned by the "operation user_account".

        - By default, the "operation user_account" is the token user_account.

        Args:
            board_id (str): Unique identifier of the board to which the pin will be saved. Defaults to None.
            board_section_id (str, optional): Unique identifier of the board section to which the pin will be saved.
                                            Defaults to None.
        """
        inline_object_kwargs = {}
        inline_object_kwargs['board_id'] = board_id
        if board_section_id:
            inline_object_kwargs['board_section_id'] = board_section_id

        api_response = self._generated_api.pins_save(
            pin_id=self.id,
            inline_object1=InlineObject1(**inline_object_kwargs)
        )

        verify_api_response(api_response)

        self._populate_fields(_model_data=api_response.to_dict())

    @classmethod
    def get_all(
        cls,
        pin_filter:str = None,
        include_protected_pins:bool = None,
        pin_type:str = None,
        creative_types:list[str] = None,
        ad_account_id:str = None,
        pin_metrics:bool = None,
        page_size:int = None,
        bookmark:str = None,
        client:PinterestSDKClient = None,
        **kwargs
    ) -> tuple[list[Pin], Bookmark]:
        """
        Get a list of the pins owned by the "operation user_account"

        Args:
            pin_filter (str): Pin filter. [optional]
            include_protected_pins (bool): Specify if return pins from protected boards. [optional]
                if omitted the server will use the default value of False
            pin_type (str): The type of pins to return, currently only enabled for private pins. [optional]
                if omitted the server will use the default value of "PRIVATE"
            creative_types ([str]): Pin creative types filter. </p><strong>Note:</strong> SHOP_THE_PIN has
                been deprecated. Please use COLLECTION instead. [optional]
            ad_account_id (str): Unique identifier of an ad account. [optional]
            pin_metrics (bool): Specify whether to return 90d and lifetime Pin metrics. Total comments
                and total reactions are only available with lifetime Pin metrics. If Pin was created before
                <code>2023-03-20</code> lifetime metrics will only be available for Video and Idea Pin formats.
                Lifetime metrics are available for all Pin formats since then.. [optional] if omitted the server
                will use the default value of False
            page_size (int[1..100], optional): Maximum number of items to include in a single page of the response.
                                    See documentation on Pagination for more information. Defaults to None which will
                                    return default page size campaigns.
            bookmark (str, optional): Cursor used to fetch the next page of items. Defaults to None.
            client (PinterestSDKClient, optional): _description_. Defaults to None.

        Keyword Args:
            Any valid keyword arguments or query parameters for endpoint.

        Returns:
            list[Pin]: List of Pin Objects
            Bookmark: Bookmark for pagination if present, else None.
        """
        params = {}

        if pin_filter:
            kwargs['pin_filter'] = pin_filter
        if include_protected_pins:
            kwargs['include_protected_pins'] = include_protected_pins
        if pin_type:
            kwargs['pin_type'] = pin_type
        if creative_types:
            kwargs['creative_types'] = creative_types
        if ad_account_id:
            kwargs['ad_account_id'] = ad_account_id
        if pin_metrics:
            kwargs['pin_metrics'] = pin_metrics

        def _map_function(obj):
            return Pin(
                pin_id=obj.get('id'),
                client=client,
                _model_data=obj
            )

        return cls._list(
            params=params,
            page_size=page_size,
            bookmark=bookmark,
            api=PinsApi,
            list_fn=PinsApi.pins_list,
            map_fn=_map_function,
            client=client,
            **kwargs
        )
