"""
Test Board Model

*NOTE*: Do not forget to delete board after the test.
"""
import time
from unittest import skip
from unittest.mock import patch
from parameterized import parameterized

from openapi_generated.pinterest_client.exceptions import NotFoundException

from pinterest.organic.boards import Board
from pinterest.organic.boards import BoardSection
from pinterest.organic.pins import Pin

from integration_tests.base_test import BaseTestCase
from integration_tests.config import DEFAULT_BOARD_ID, DEFAULT_BOARD_NAME

class TestGetBoard(BaseTestCase):
    """
    Test intializing Board model
    """
    def test_get_board_success(self):
        """
        Test getting an existing Campaign successfully
        """
        board = Board(
            board_id=DEFAULT_BOARD_ID,
            client=self.test_client,
        )

        assert board
        assert board.id == DEFAULT_BOARD_ID
        assert board.name == DEFAULT_BOARD_NAME

    def test_get_board_failure_invalid_board_id(self):
        """
        Test getting a Board failure due to invalid board id
        """
        non_existant_board_id = "123123123123"
        board_arguments = dict(
            board_id=non_existant_board_id,
            client=self.test_client,
        )

        with self.assertRaises(NotFoundException):
            Board(**board_arguments)


class TestCreateAndDeleteBoard(BaseTestCase):
    """
    Test creating and deleting Board Model
    """
    def test_create_and_delete_board_success(self):
        """
        Test creating a new Board and deleting the Board successfully
        """
        board = Board.create(
            name="SDK Test Create Board",
            description="SDK Test Board Description",
            privacy="PUBLIC",
            client=self.test_client
        )

        assert board
        assert board.name == "SDK Test Create Board"

        self.board_utils.delete_board(board_id=board.id)

        with self.assertRaises(NotFoundException):
            Board(
                board_id=board.id,
                client=self.test_client
                )


class TestBoardUpdateFields(BaseTestCase):
    """
    Test updating the fields of a Board Model.
    """
    def test_update_board_fields_success(self):
        """
        Test updating the description and privacy of the board successfully.
        """
        old_description, new_description = "Description before update", "Description after update"
        old_privacy, new_privacy = "PUBLIC", "SECRET"

        board = self.board_utils.create_new_board(
            description=old_description,
            privacy=old_privacy
        )

        assert board.description == old_description
        assert board.privacy == old_privacy

        board.update_fields(
            description=new_description,
            privacy=new_privacy
        )
        self.board_utils.delete_board(board_id=board.id)

        assert board.description == new_description
        assert board.privacy == new_privacy

    def test_update_board_fields_failure_invalid_field_value(self):
        """
        Test updating the name of the board with invalid/existing board name value.
        """
        board = self.board_utils.create_new_board()

        assert board

        existing_board_name = DEFAULT_BOARD_NAME

        with self.assertRaisesRegex(Exception, "Could not edit board"):
            board.update_fields(
                name=existing_board_name
            )
        self.board_utils.delete_board(board_id=board.id)

class TestChangeBoardPrivacy(BaseTestCase):
    """
    Test changing the privacy of a Board Model.
    """
    @parameterized.expand(
        [
            ('SECRET', 'PUBLIC', 'make_public'),
            ('PUBLIC', 'SECRET', 'make_secret')
        ]
    )
    def test_change_board_privacy_success(self, old_privacy, new_privacy, make_privacy_fn):
        """
        Test making a secret board public successfully
        and
        Test making a public board secret successfully
        """
        board = self.board_utils.create_new_board(privacy=old_privacy)

        assert board
        assert board.privacy == old_privacy

        update_status = getattr(board, make_privacy_fn)()
        self.board_utils.delete_board(board_id=board.id)

        assert update_status
        assert board.privacy == new_privacy

class TestBoardSectionOperations(BaseTestCase):
    """
    Test different operations with BoardSection using a Board Model.
    """
    def test_create_new_board_section_success(self):
        """
        Test creating a new board section under a board model successfully.
        """
        board = self.board_utils.create_new_board(name="Create Board Section Test")

        assert board

        new_section_name = "SDK Test Create Section"
        new_section = board.create_section(name=new_section_name)

        self.board_utils.delete_board(board_id=board.id)

        assert new_section.id
        assert new_section.name == new_section_name

    def test_update_board_section_success(self):
        """
        Test updating an existing board section under a board model successfully.
        """
        board = self.board_utils.create_new_board(name="Update Board Section Test")

        assert board

        new_section_name = "SDK Test Create Section"
        new_section = board.create_section(name=new_section_name)

        assert new_section.name == new_section_name

        updated_section_name = "SDK Test Update Section"
        updated_section = board.update_section(section_id=new_section.id, name=updated_section_name)

        self.board_utils.delete_board(board_id=board.id)

        assert new_section.id == updated_section.id
        assert updated_section.name == updated_section_name

    def test_delete_board_section_success(self):
        """
        Test deleting an existing board section under a board model successfully.
        """
        board = self.board_utils.create_new_board(name="Delete Board Section Test")
        assert board

        board_section_name = "SDK Test Delete Section"
        board_section = board.create_section(name=board_section_name)
        assert board_section

        board.delete_section(section_id=board_section.id)
        self.board_utils.delete_board(board_id=board.id)


class TestGetAllBoards(BaseTestCase):
    """
    Test Get All Boards class method
    """
    @skip(reason="Board creation happens after get_all() due to lag")
    @patch('pinterest.organic.boards.BoardsApi.boards_get')
    def test_get_all_boards(self, boards_get_mock):
        """
        Test if all boards are returned
        """
        NUMBER_OF_BOARDS_TO_CREATE = 3
        created_board_ids = set(
            getattr(self.board_utils.create_new_board(name=f"GET ALL Board Test #{num}"), 'id')
            for num in range(NUMBER_OF_BOARDS_TO_CREATE)
        )

        assert len(created_board_ids) == NUMBER_OF_BOARDS_TO_CREATE

        #TODO: Find a better solution to the lag between api executing the command and python moving to next command
        time.sleep(1.5)
        boards_list, _ = Board.get_all()

        # delete organic data from prod
        for board in boards_list:
            if board.id in created_board_ids:
                self.board_utils.delete_board(board.id)

        assert boards_get_mock.call_count - 1 == NUMBER_OF_BOARDS_TO_CREATE
        assert len(created_board_ids) <= len(boards_list)

        for board in boards_list:
            if board.id in created_board_ids:
                assert isinstance(board, Board)
                created_board_ids.remove(board.id)

        assert len(created_board_ids) == 0

class TestGetAllBoardSections(BaseTestCase):
    """
    Test Get All Board Sections class method
    """
    def test_get_all_board_sections(self):
        """
        Test if all board sections are returned
        """
        new_board = self.board_utils.create_new_board(name="GET ALL BOARD SECTIONS TEST BOARD")

        NUMBER_OF_BOARD_SECTIONS_TO_CREATE = 3
        created_board_section_ids = set(
            getattr(new_board.create_section(name=f"GET ALL BOARD SECTION Test #{num}"), 'id')
            for num in range(NUMBER_OF_BOARD_SECTIONS_TO_CREATE)
        )

        assert len(created_board_section_ids) == NUMBER_OF_BOARD_SECTIONS_TO_CREATE

        board_sections_list, _ = BoardSection.get_all(board_id=new_board.id)

        # delete organic data from prod
        for board_section in board_sections_list:
            new_board.delete_section(board_section.id)
        self.board_utils.delete_board(new_board.id)

        assert len(created_board_section_ids) == len(board_sections_list)

        for board_section in board_sections_list:
            if board_section.id in created_board_section_ids:
                assert isinstance(board_section, BoardSection)
                created_board_section_ids.remove(board_section.id)

        assert len(created_board_section_ids) == 0


class TestListPinsOnBoardAndBoardSection(BaseTestCase):
    """
    Test Get All Pins
    """
    def test_list_pins_on_board(self):
        """
        Test if all pins on a board are returned
        """
        new_board = self.board_utils.create_new_board(name="GET ALL BOARD PINS TEST BOARD")

        NUMBER_OF_PINS_TO_CREATE = 3

        PIN_CREATION_MEDIA_SOURCES = [
            {
                "source_type": "image_url",
                "content_type": "image/jpeg",
                "data": "string",
                'url':'https://i.pinimg.com/564x/28/75/e9/2875e94f8055227e72d514b837adb271.jpg'
            },
            {
                "source_type": "image_url",
                "content_type": "image/jpeg",
                "data": "string",
                'url':'https://i.picsum.photos/id/13/2500/1667.jpg?hmac=SoX9UoHhN8HyklRA4A3vcCWJMVtiBXUg0W4ljWTor7s'
            },
            {
                "source_type": "image_url",
                "content_type": "image/jpeg",
                "data": "string",
                'url':'https://i.picsum.photos/id/21/3008/2008.jpg?hmac=T8DSVNvP-QldCew7WD4jj_S3mWwxZPqdF0CNPksSko4'
            }
        ]

        created_pin_ids = set(
            getattr(self.pin_utils.create_new_pin(
                board_id=new_board.id,
                title=f"GET ALL PINS TEST #{num}",
                media_source=PIN_CREATION_MEDIA_SOURCES[num]
                ),
                'id'
            )
            for num in range(NUMBER_OF_PINS_TO_CREATE)
        )

        assert len(created_pin_ids) == NUMBER_OF_PINS_TO_CREATE

        pins_list, _ = new_board.list_pins()

        # delete organic data from prod
        for pin in pins_list:
            self.pin_utils.delete_pin(pin.id)
        self.board_utils.delete_board(new_board.id)

        assert len(created_pin_ids) == len(pins_list)

        for pin in pins_list:
            if pin.id in created_pin_ids:
                assert isinstance(pin, Pin)
                created_pin_ids.remove(pin.id)

        assert len(created_pin_ids) == 0

    def test_list_pins_on_board_section(self):
        """
        Test if all pins on a board section are returned
        """
        new_board = self.board_utils.create_new_board(name="GET ALL BOARD SECTION PINS TEST BOARD")
        new_section = new_board.create_section(name="GET ALL PINS FROM BOARD SECTION Test")

        NUMBER_OF_PINS_TO_CREATE = 3
        PIN_CREATION_MEDIA_SOURCES = [
            {
                "source_type": "image_url",
                "content_type": "image/jpeg",
                "data": "string",
                'url':'https://i.pinimg.com/564x/28/75/e9/2875e94f8055227e72d514b837adb271.jpg'
            },
            {
                "source_type": "image_url",
                "content_type": "image/jpeg",
                "data": "string",
                'url':'https://i.picsum.photos/id/13/2500/1667.jpg?hmac=SoX9UoHhN8HyklRA4A3vcCWJMVtiBXUg0W4ljWTor7s'
            },
            {
                "source_type": "image_url",
                "content_type": "image/jpeg",
                "data": "string",
                'url':'https://i.picsum.photos/id/21/3008/2008.jpg?hmac=T8DSVNvP-QldCew7WD4jj_S3mWwxZPqdF0CNPksSko4'
            }
        ]

        created_pin_ids = set(
            getattr(self.pin_utils.create_new_pin(
                board_id=new_board.id,
                board_section_id=new_section.id,
                title=f"GET ALL PINS TEST #{num}",
                media_source=PIN_CREATION_MEDIA_SOURCES[num]
                ),
                'id'
            )
            for num in range(NUMBER_OF_PINS_TO_CREATE)
        )

        assert len(created_pin_ids) == NUMBER_OF_PINS_TO_CREATE

        pins_list, _ = new_board.list_pins(section_id=new_section.id)

        # delete organic data from prod
        for pin in pins_list:
            self.pin_utils.delete_pin(pin.id)
        new_board.delete_section(new_section.id)
        self.board_utils.delete_board(new_board.id)

        assert len(created_pin_ids) == len(pins_list)

        for pin in pins_list:
            if pin.id in created_pin_ids:
                assert isinstance(pin, Pin)
                created_pin_ids.remove(pin.id)

        assert len(created_pin_ids) == 0
