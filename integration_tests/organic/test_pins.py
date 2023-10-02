"""
Test Pin Model

*NOTE*: Do not forget to delete pin after the test.
"""
from datetime import date
from datetime import timedelta
from parameterized import parameterized

from openapi_generated.pinterest_client.exceptions import NotFoundException
from openapi_generated.pinterest_client.exceptions import ApiException

from pinterest.organic.pins import Pin

from integration_tests.base_test import BaseTestCase
from integration_tests.config import DEFAULT_PIN_ID
from integration_tests.config import DEFAULT_BOARD_ID
from integration_tests.config import DEFAULT_AD_ACCOUNT_ID
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
                'ad_account_id': DEFAULT_AD_ACCOUNT_ID,
            },),
            ({
                'description': 'PIN in PROTECTED BOARD',
                'pin_id': DEFAULT_PIN_ID,
                'ad_account_id': DEFAULT_AD_ACCOUNT_ID,
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
            ad_account_id = DEFAULT_AD_ACCOUNT_ID,
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
        assert pin.title == "Test Saving Pin"

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

class TestGetAnalytics(BaseTestCase):
    """
    Test getting a Pin analytics
    """
    DAYS_BACK = 4
    EXPECTED_NUM_OF_DAILY_METRICS = DAYS_BACK + 1
    DAYS_BACK_OUT_OF_RANGE = 91
    METRIC_TYPES = "IMPRESSION,OUTBOUND_CLICK,PIN_CLICK,SAVE,SAVE_RATE,TOTAL_COMMENTS,TOTAL_REACTIONS"

    def validate_raw_response(self, raw_response):
        self.assertIsNotNone(raw_response)
        self.assertIsNotNone(raw_response.get('all'))
        self.assertIsNotNone(raw_response.get('all').get('daily_metrics'))
        self.assertIsNotNone(raw_response.get('all').get('lifetime_metrics'))
        self.assertIsNotNone(raw_response.get('all').get('summary_metrics'))
        self.assertEqual(len(raw_response.get('all').get('daily_metrics')), self.EXPECTED_NUM_OF_DAILY_METRICS)
        for metric in self.METRIC_TYPES.split(','):
            self.assertIn(metric, {**raw_response.get('all').get('summary_metrics'),**raw_response.get('all').get('lifetime_metrics')})


    def test_get_analytics_success(self):
        """
        Test request the Pin analitycs
        """
        analytics_info_dict = {
            'pin_id': DEFAULT_PIN_ID,
            'start_date': date.today() - timedelta(self.DAYS_BACK),
            'end_date': date.today(),
            'metric_types': ["IMPRESSION,OUTBOUND_CLICK,PIN_CLICK,SAVE,SAVE_RATE,TOTAL_COMMENTS,TOTAL_REACTIONS"],
        }
        pin = Pin(pin_id=analytics_info_dict.pop('pin_id'))
        analytics = pin.get_analytics(**analytics_info_dict)
        self.assertIsNotNone(analytics)
        self.validate_raw_response(analytics.raw_response)

    def test_get_analytics_failure(self):
        """Test request the Pin analytics from before 90 days ago. 
        """
        analytics_info_dict = {
            'pin_id': DEFAULT_PIN_ID,
            'start_date': date.today() - timedelta(self.DAYS_BACK_OUT_OF_RANGE),
            'end_date': date.today(),
            'metric_types': ["IMPRESSION,OUTBOUND_CLICK,PIN_CLICK,SAVE,SAVE_RATE,TOTAL_COMMENTS,TOTAL_REACTIONS"],
        }
        pin = Pin(pin_id=analytics_info_dict.pop('pin_id'))
        with self.assertRaises(ApiException):
            pin.get_analytics(**analytics_info_dict)