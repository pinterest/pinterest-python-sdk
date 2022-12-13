"""
Test Board Model
"""

from unittest import TestCase
from unittest.mock import patch

from pinterest.client import PinterestSDKClient
from pinterest.generated.client.model.board import Board as GeneratedBoard

from pinterest.organic.boards import Board

class TestBoard(TestCase):
    """
    Test Board model and its higher level functions
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        PinterestSDKClient.set_default_access_token("test_token")
        self.test_board_id = "111111111111"

    @patch('pinterest.organic.boards.BoardsApi.boards_get')
    def test_create_board_model_using_existing_board(self, boards_get_mock):
        """
        Test if a Board model/object is created successfully with correct board_id
        """

        boards_get_mock.return_value = GeneratedBoard(
            name="SDK Test Board",
            description="SDK Test Board Description",
            privacy="PUBLIC"
            )

        board_response = Board(
            board_id=self.test_board_id,
        )

        assert board_response
        assert board_response.name == "SDK Test Board"
