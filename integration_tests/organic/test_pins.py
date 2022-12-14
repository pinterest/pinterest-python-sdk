"""
Test Pin Model

*NOTE*: Do not forget to delete pin after the test.
"""
from parameterized import parameterized

from pinterest.generated.client.exceptions import NotFoundException

from pinterest.organic.pins import Pin

from integration_tests.base_test import BaseTestCase
from integration_tests.config import DEFAULT_PIN_ID
from integration_tests.config import DEFAULT_BOARD_ID
from integration_tests.config import DEFAULT_BOARD_SECTION_ID

class TestGetPin(BaseTestCase):
    """
    Test class for getting Pin
    """
    @parameterized.expand(
        [
            ({
                'description': 'PIN is PUBLIC',
                'pin_id': DEFAULT_PIN_ID,
                'ad_account_id': None,
            },),
            ({
                'description': 'PIN in PROTECTED BOARD',
                'pin_id': DEFAULT_PIN_ID,
                'ad_account_id': None,
            },)
        ]
    )
    def test_get_public_and_private_pin_success(self, pin_info_dict):
        """
        Test getting and initializing a PUBLIC pin using pin_id
        and
        Test getting and initializing a pin inside a PROTECTED board using pin_id and ad_account_id
        """
        pin = Pin(pin_id=pin_info_dict.get('pin_id'), ad_acount_id=pin_info_dict.get('ad_account_id'))

        assert pin
        assert pin.id == pin_info_dict.get('pin_id')


class TestCreateAndDeletePin(BaseTestCase):
    """
    Test creating and deleting Pin Model
    """
    def test_create_and_delete_pin_success(self):
        """
        Test creating a new Pin and deleting the Pin successfully
        """
        pin = Pin.create(
            board_id=DEFAULT_BOARD_ID,
            title="SDK Test Pin",
            description="SDK Test Pin Description",
            media_source={
                "source_type": "image_url",
                "content_type": "image/jpeg",
                "data": "string",
                'url':'https://i.pinimg.com/564x/28/75/e9/2875e94f8055227e72d514b837adb271.jpg'
                },
            client=self.test_client
        )

        assert pin
        assert pin.title == "SDK Test Pin"

        self.pin_utils.delete_pin(pin_id=pin.id)

        with self.assertRaises(NotFoundException):
            Pin(
                pin_id=pin.id,
                client=self.test_client
                )


class TestSavePin(BaseTestCase):
    """
    Test saving a pin
    """
    @parameterized.expand(
        [
            ({
                # Save to board
                'board_id': DEFAULT_BOARD_ID,
            },),
            ({
                # Save to board section
                'board_id': DEFAULT_BOARD_ID,
                'board_section_id': DEFAULT_BOARD_SECTION_ID,
            },)
        ]
    )
    def test_save_pin_success(self, pin_save_kwargs):
        """
        Test saving pin with default args, board_id and board_section_id
        """
        pin = self.pin_utils.create_new_pin(title="Test Saving Pin")
        assert pin

        pin.save(**pin_save_kwargs)

        if pin_save_kwargs.get('board_id'):
            assert pin.board_id == pin_save_kwargs.get('board_id')

        if pin_save_kwargs.get('board_section_id'):
            assert pin.board_section_id == pin_save_kwargs.get('board_section_id')

        self.pin_utils.delete_pin(pin_id=pin.id)
        with self.assertRaises(NotFoundException):
            Pin(
                pin_id=pin.id,
                client=self.test_client
                )
