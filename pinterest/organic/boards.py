"""
Board Class for Pinterest Python SDK
"""
from __future__ import annotations

from datetime import datetime

from openapi_generated.pinterest_client.api.boards_api import BoardsApi
from openapi_generated.pinterest_client.model.board import Board as GeneratedBoard
from openapi_generated.pinterest_client.model.board_update import BoardUpdate

from openapi_generated.pinterest_client.model.board_section import BoardSection as GeneratedBoardSection

from pinterest.organic.pins import Pin

from pinterest.client import PinterestSDKClient
from pinterest.utils.base_model import PinterestBaseModel
from pinterest.utils.error_handling import verify_api_response
from pinterest.utils.sdk_exceptions import SdkException
from pinterest.utils.bookmark import Bookmark

class BoardSection(PinterestBaseModel):
    """
    Board Section model used as a helper model for `BOARD`
    """
    def __init__(
        self,
        board_section_id:str,
        name:str,
        ) -> None:
        """
        Initialize a Board Section object.

        Args:
            board_section_id (str): Unique identifier of a board section.
            name (str): Name for the board section.
        """
        self._id = board_section_id
        self._name = name

    @property
    def id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._id

    @property
    def name(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._name

    @classmethod
    def create(
        cls,
        board_id:str,
        name:str,
        client:PinterestSDKClient=None,
    ) -> BoardSection:
        """
        Class method to help create a board section.

        Args:
            board_id (str): Unique identifier of a board.
            name (str): Name for the board section.
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Uses the default client, if not provided.

        Returns:
            BoardSection: The created board section.
        """
        if not client:
            client = cls._get_client()

        api_response = BoardsApi(client).board_sections_create(
            board_id=board_id,
            board_section=GeneratedBoardSection(
                name=name
            )
        )
        verify_api_response(api_response)

        return BoardSection(board_section_id=getattr(api_response, "id"), name=getattr(api_response, "name"))


    @classmethod
    def get_all(
        cls,
        board_id:str,
        page_size:int = None,
        bookmark:str = None,
        client:PinterestSDKClient = None,
        **kwargs
    ) -> tuple[list[BoardSection], Bookmark]:
        """
        List board sections in a given board id.


        Args:
            board_id (str, optional): Unique identifier of a board.
            page_size (int[1..100], optional): Maximum number of items to include in a single page of the response.
                                    See documentation on Pagination for more information. Defaults to None which will
                                    return default page size campaigns.
            bookmark (str, optional): Cursor used to fetch the next page of items. Defaults to None.
            client (PinterestSDKClient, optional): _description_. Defaults to None.

        Keyword Args:
            Any valid keyword arguments or query parameters for endpoint.

        Returns:
            list[BoardSection]: List of BoardSection Objects
            Bookmark: Bookmark for pagination if present, else None.
        """
        params = {"board_id": board_id}

        def _map_function(obj):
            return BoardSection(
                board_section_id=obj.get('id'),
                name=obj.get('name'),
            )

        return cls._list(
            params=params,
            page_size=page_size,
            bookmark=bookmark,
            api=BoardsApi,
            list_fn=BoardsApi.board_sections_list,
            map_fn=_map_function,
            client=client,
            **kwargs
        )

    @classmethod
    def update(
        cls,
        board_id:str,
        board_section_id:str,
        name:str,
        client:PinterestSDKClient=None,
    ) -> BoardSection:
        """
        Class method to help update a board section.

        Args:
            board_id (str): Unique identifier of a board.
            board_section_id (str): Unique identifier of a board section.
            name (str): Name for the board section.
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Uses the default client, if not provided.

        Returns:
            BoardSection: The updated board section.
        """
        if not client:
            client = cls._get_client()

        api_response = BoardsApi(client).board_sections_update(
            board_id=board_id,
            section_id=board_section_id,
            board_section=GeneratedBoardSection(
                name=name
            )
        )
        verify_api_response(api_response)

        return BoardSection(board_section_id=getattr(api_response, "id"), name=getattr(api_response, "name"))

    @classmethod
    def delete(
        cls,
        board_id:str,
        board_section_id:str,
        client:PinterestSDKClient=None,
    ) -> None:
        """
        Class method to help delete a board section.

        Args:
            board_id (str): Unique identifier of a board.
            board_section_id (str): Unique identifier of a board section.
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Uses the default client, if not provided.

        Returns:
            None
        """
        if not client:
            client = cls._get_client()

        api_response = BoardsApi(client).board_sections_delete(
            board_id=board_id,
            section_id=board_section_id,
        )
        verify_api_response(api_response)


class Board(PinterestBaseModel):
    """
    Board model used to view, create, update its attributes and list its different entities.
    """
    def __init__(
        self,
        board_id:str,
        client:PinterestSDKClient=None,
        **kwargs
        ) -> None:
        """
        Initialize a Board object.

        Args:
            board_id (str): Unique identifier of a board.
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Uses the default client, if not provided.
        """
        self._id = None
        self._name = None
        self._description = None
        self._owner = None
        self._privacy = None
        self._board_pins_modified_at = None
        self._pin_count = None
        self._created_at = None
        self._media = None
        self._collaborator_count = None
        self._follower_count = None

        PinterestBaseModel.__init__(
            self,
            _id=str(board_id),
            generated_api=BoardsApi,
            generated_api_get_fn="boards_get",
            generated_api_get_fn_args={"board_id": board_id},
            model_attribute_types = GeneratedBoard.openapi_types,
            client=client,
            )

        self._populate_fields(**kwargs)

    @property
    def id(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._id

    @property
    def name(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._name

    @property
    def description(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._description

    @property
    def owner(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._owner

    @property
    def privacy(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._privacy

    @property
    def board_pins_modified_at(self) -> datetime:
        # pylint: disable=missing-function-docstring
        return self._board_pins_modified_at

    @property
    def pin_count(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._pin_count

    @property
    def created_at(self) -> datetime:
        # pylint: disable=missing-function-docstring
        return self._created_at

    @property
    def media(self) -> str:
        # pylint: disable=missing-function-docstring
        return self._media

    @property
    def collaborator_count(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._collaborator_count

    @property
    def follower_count(self) -> int:
        # pylint: disable=missing-function-docstring
        return self._follower_count

    def __repr__(self):
        return f"{self.__class__.__name__}(board_id={self._id})"

    @classmethod
    def create(
        cls,
        name:str,
        description:str = None,
        privacy:str = "PUBLIC",
        client:PinterestSDKClient = None,
        **kwargs
    ) -> Board:
        """
        Create a board owned by the "operation user_account".

        - By default, the "operation user_account" is the token user_account.

        Args:
            name (str): Board name.
            description (str, optional): Board description. Defaults to None.
            privacy (str, optional): Enum: `"PUBLIC"`, `"PROTECTED"`, `"SECRET"`. Defaults to "PUBLIC".
            client (PinterestSDKClient, optional): PinterestSDKClient Object, uses the default client, if not provided.

        Keyword Args:
            Any valid keyword arguments or query parameters for endpoint.

        Returns:
            Board: Board object
        """

        if not client:
            client = cls._get_client()

        api_response = BoardsApi(client).boards_create(
            board=GeneratedBoard(
                name=name,
                description=description,
                privacy=privacy,
                **kwargs
            )
        )
        verify_api_response(api_response)

        return Board(board_id=getattr(api_response, "id"), client=client)

    @classmethod
    def delete(
        cls,
        board_id:str,
        client:PinterestSDKClient = None
    ) -> bool:
        """
        Delete a board owned by the "operation user_account".

        - By default, the "operation user_account" is the token user_account.

        Args:
            board_id (str): Unique identifier of a board.
            client (PinterestSDKClient, optional): PinterestSDKClient Object. Uses the default client, if not provided.

        Returns:
            bool: If the board was deleted successfully.
        """
        if not client:
            client = cls._get_client()

        api_response = BoardsApi(client).boards_delete(
            board_id=board_id
        )
        verify_api_response(api_response)

        return True

    @classmethod
    def get_all(
        cls,
        privacy:str = None,
        page_size:int = None,
        bookmark:str = None,
        client:PinterestSDKClient = None,
        **kwargs
    ) -> tuple[list[Board], Bookmark]:
        """
        Get a list of the boards owned by the "operation user_account" + group boards where this
        account is a collaborator

        Optional: Specify a privacy type (public, protected, or secret) to indicate which boards to return.

        - If no privacy is specified, all boards that can be returned (based on the scopes of the token and ad_account
        role if applicable) will be returned.


        Args:
            privacy (str, optional):  Enum: `"PUBLIC"`, `"PROTECTED"`, `"SECRET"`. Defaults to "PUBLIC".
            page_size (int[1..100], optional): Maximum number of items to include in a single page of the response.
                                    See documentation on Pagination for more information. Defaults to None which will
                                    return default page size campaigns.
            bookmark (str, optional): Cursor used to fetch the next page of items. Defaults to None.
            client (PinterestSDKClient, optional): _description_. Defaults to None.

        Keyword Args:
            Any valid keyword arguments or query parameters for endpoint.

        Returns:
            list[Board]: List of Board Objects
            Bookmark: Bookmark for pagination if present, else None.
        """
        params = {}

        if privacy:
            kwargs['privacy'] = privacy

        def _map_function(obj):
            return Board(
                board_id=obj.get('id'),
                client=client,
                _model_data=obj
            )

        return cls._list(
            params=params,
            page_size=page_size,
            bookmark=bookmark,
            api=BoardsApi,
            list_fn=BoardsApi.boards_list,
            map_fn=_map_function,
            client=client,
            **kwargs
        )

    def update_fields(self, **kwargs) -> bool:
        """
        Update the board fields using any attributes.

        Keyword Args:
            Any valid campaign fields with valid values

        Returns:
            bool: If board fields were successfully updated
        """
        api_response = self._generated_api.boards_update(
            board_id=self.id,
            board_update=BoardUpdate(
                **kwargs
                )
            )
        verify_api_response(api_response)

        self._populate_fields()

        for arg, value in kwargs.items():
            if getattr(self, f'{arg}') != value:
                SdkException(reason=f"Update Failed. Expected {arg} is {value}"
                + f" Actual value is {getattr(self, f'{arg}')}")

        return True

    def make_public(self) -> bool:
        """
        Change the privacy of the board to `PUBLIC`.

        Returns:
            bool: If the board was successfully made public.
        """
        return self.update_fields(privacy='PUBLIC')

    def make_secret(self) -> bool:
        """
        Change the privacy of the board to `SECRET`.

        Returns:
            bool: If the board was successfully made secret.
        """
        return self.update_fields(privacy='SECRET')

    def create_section(self, name:str) -> BoardSection:
        """
        Create a board section on a board owned by the "operation user_account" - or on a group board
        that has been shared with this account.

        - By default, the "operation user_account" is the token user_account.

        Args:
            name (str): Name for the board section.

        Returns:
            BoardSection: The created board section.
        """
        return BoardSection.create(
            board_id=self.id,
            name=name,
            client=self._client
        )

    def update_section(self, section_id:str, name:str) -> BoardSection:
        """
        Update a board section on a board owned by the "operation user_account" - or on a group board
        that has been shared with this account.

        - By default, the "operation user_account" is the token user_account.

        Args:
            section_id (str): Unique identifier of a board section.
            name (str): Name for the board section.

        Returns:
            BoardSection: The created board section.
        """
        return BoardSection.update(
            board_id=self.id,
            board_section_id=section_id,
            name=name,
            client=self._client
        )

    def delete_section(self, section_id:str) -> None:
        """
        Delete a board section on a board owned by the "operation user_account" - or on a group board
        that has been shared with this account.

        - By default, the "operation user_account" is the token user_account.

        Args:
            section_id (str): Unique identifier of a board section.

        Returns:
            None
        """
        return BoardSection.delete(
            board_id=self.id,
            board_section_id=section_id,
            client=self._client
        )

    def list_sections(
        self,
        page_size:int = None,
        bookmark:str = None,
        **kwargs
    ) -> tuple[list[BoardSection], Bookmark]:
        """
        Get a list of all board sections from a board owned by the "operation user_account" - or a group board that has
        been shared with this account.

        By default, the "operation user_account" is the token user_account.


        Args:
            page_size (int[1..100], optional): Maximum number of items to include in a single page of the response.
                                    See documentation on Pagination for more information. Defaults to None which will
                                    return default page size campaigns.
            bookmark (str, optional): Cursor used to fetch the next page of items. Defaults to None.

        Keyword Args:
            Any valid keyword arguments or query parameters for endpoint.

        Returns:
            list[BoardSection]: List of BoardSection Objects
            Bookmark: Bookmark for pagination if present, else None.
        """
        return BoardSection.get_all(
            board_id=self.id,
            page_size=page_size,
            bookmark=bookmark,
            client=self._client,
            **kwargs
        )

    def list_pins(
        self,
        section_id:str = None,
        page_size:int = None,
        bookmark:str = None,
    ) -> tuple[list[Pin], Bookmark]:
        """
        Get a list of the Pins on a board owned by the "operation user_account" - or on a group board that has been
        shared with this account.

        - By default, the "operation user_account" is the token user_account.

        Args:
            section_id (str, optional): Unique identifier of a board section. If not passed in, all pins under
                                        the board will be listed.
            page_size (int[1..100], optional): Maximum number of items to include in a single page of the response.
                                    See documentation on Pagination for more information. Defaults to None which will
                                    return default page size campaigns.
            bookmark (str, optional): Cursor used to fetch the next page of items. Defaults to None.

        Keyword Args:
            Any valid keyword arguments or query parameters for endpoint.

        Returns:
            list[Pin]: List of Pin Objects
            Bookmark: Bookmark for pagination if present, else None.
        """
        params = {"board_id": self.id}

        if section_id:
            params["section_id"] = section_id

        def _map_function(obj):
            return Pin(
                pin_id=obj.get('id'),
                client=self._client,
                _model_data=obj
            )

        return self._list(
            params=params,
            page_size=page_size,
            bookmark=bookmark,
            api=BoardsApi,
            list_fn=BoardsApi.boards_list_pins if not section_id else BoardsApi.board_sections_list_pins,
            map_fn=_map_function,
            bookmark_model_cls=self,
            bookmark_model_fn=self.list_pins,
            client=self._client,
        )
