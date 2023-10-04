"""
Test Ad Model
"""
from datetime import date
from datetime import timedelta
from unittest.mock import DEFAULT
from parameterized import parameterized

from pinterest.ads.ads import Ad

from openapi_generated.pinterest_client.exceptions import ApiException
from openapi_generated.pinterest_client.exceptions import ApiValueError
from openapi_generated.pinterest_client.exceptions import NotFoundException
from openapi_generated.pinterest_client.model.entity_status import EntityStatus

from integration_tests.base_test import BaseTestCase
from integration_tests.config import DEFAULT_PIN_ID
from integration_tests.config import DEFAULT_AD_ACCOUNT_ID
from integration_tests.config import DEFAULT_AD_ID
from integration_tests.config import DEFAULT_AD_GROUP_ID


class TestCreateAd(BaseTestCase):
    """
    Test creating Ad model
    """

    def test_create_ad_success(self):
        """
        Test create ad success
        """
        ad = Ad.create(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_group_id=DEFAULT_AD_GROUP_ID,
            creative_type="IDEA",
            pin_id=DEFAULT_PIN_ID,
            name="Test_create_ad",
            status="PAUSED",
            is_pin_deleted=False,
            is_removable=False,
            client=self.test_client,
        )
        assert ad
        assert getattr(ad, "_id")
        assert getattr(ad, "_name") == "Test_create_ad"

    def test_create_ad_failure_without_creative_type(self):
        """
        Test create ad fail without creative type
        """
        ad_arguments = dict(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_group_id=DEFAULT_AD_GROUP_ID,
            pin_id=DEFAULT_PIN_ID,
            name="Test_create_ad",
            status="ACTIVE",
            client=self.test_client,
        )

        with self.assertRaises(TypeError):
            Ad.create(**ad_arguments)

    def test_create_ad_failure_with_incorrect_creative_type(self):
        """
        Test create ad fail with incorrect creative type
        """
        ad_arguments = dict(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_group_id=DEFAULT_AD_GROUP_ID,
            creative_type="NOT",
            pin_id=DEFAULT_PIN_ID,
            name="Test_create_ad",
            status="ACTIVE",
            client=self.test_client,
        )

        with self.assertRaises(ApiValueError):
            Ad.create(**ad_arguments)

class TestGetAd(BaseTestCase):
    """
    Test getting Ad model
    """
    def test_get_ad_success(self):
        """
        Test get ad success
        """
        ad = Ad(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_id=DEFAULT_AD_ID,
            client=self.test_client,
        )

        assert ad
        assert getattr(ad, "_id") == DEFAULT_AD_ID

    def test_get_ad_fail_with_invalid_id(self):
        """
        Test get ad with invalid id
        """
        non_existant_ad_id="123321"
        ad_arguments = dict(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_id=non_existant_ad_id,
            client=self.test_client,
        )

        with self.assertRaises(NotFoundException):
            Ad(**ad_arguments)


class TestGetListAd(BaseTestCase):
    """
    Test get all Ad model
    """
    def test_get_all_success(self):
        """
        Test get all ads successfully
        """
        NUMBER_OF_NEW_ADS = 3
        new_ad_ids = list(
            getattr(self.ad_utils.create_new_ad(),"_id") for _ in range(NUMBER_OF_NEW_ADS)
        )

        ads, _ = Ad.get_all(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_ids=new_ad_ids,
        )
        assert len(ads) == NUMBER_OF_NEW_ADS

    def test_get_all_with_invalid_ids_fail(self):
        """
        Test get all with invalid IDs fail
        """
        INVALID_AD_IDS = ["11111111", "222222222"]
        get_list_dict = dict(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_ids=INVALID_AD_IDS
        )

        with self.assertRaises(TypeError):
            Ad.get_all(get_list_dict)


class TestUpdateAds(BaseTestCase):
    """
    Test update Ad model
    """
    def test_update_ad_success(self):
        """
        Test update Ads successfully
        """
        ad = Ad(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_id=DEFAULT_AD_ID,
            client=self.test_client,
        )

        new_name = "NEW_AD_NAME"
        new_status = "PAUSED"

        ad.update_fields(
            name=new_name,
            status=new_status
        )

        assert ad
        assert getattr(ad, "_name") == new_name
        assert getattr(ad, "_status") == EntityStatus(new_status)

class TestGetAnalytics(BaseTestCase):
    """
    Test getting Ad analytics
    """
    DAYS_BACK = 2
    FURTHEST_DAYS_BACK_HOUR = 7  # Futhest allowed days back for granularity HOUR
    FURTHEST_DAYS_BACK_NOT_HOUR = 90  # Futhest allowed days back for any granularity but HOUR

    @parameterized.expand(
        [
            ("granularity_total","TOTAL"),
            ("granularity_day", "DAY"),
            ("granularity_hour", "HOUR"),
            ("granularity_week", "WEEK"),
            ("granularity_month", "MONTH"),
        ]
    )
    def test_get_ad_analytics_success(self, name, granularity):
        
        analytics_info_dict = {
            'ad_account_id': DEFAULT_AD_ACCOUNT_ID,
            'start_date': date.today() - timedelta(self.DAYS_BACK),
            'end_date': date.today(),
            'columns': ["ADVERTISER_ID","PIN_PROMOTION_ID","SPEND_IN_DOLLAR"],
            'granularity': granularity,
        }
        ad = Ad(
            ad_account_id=analytics_info_dict.pop('ad_account_id'),
            ad_id=DEFAULT_AD_ID,
            client=self.test_client,
        )
        
        ad_analytics = ad.get_analytics(**analytics_info_dict)
        self.assertIsNotNone(ad_analytics)
        self.assertIsNotNone(ad_analytics.raw_response)
        analytics_response = ad_analytics.raw_response.get('value')
        for dict_item in analytics_response:
            for column in analytics_info_dict.get('columns'):
                self.assertIn(column, dict_item)
            if granularity != 'TOTAL':
                self.assertIn('DATE', dict_item)

    @parameterized.expand(
        [
            ("granularity_total","TOTAL", FURTHEST_DAYS_BACK_NOT_HOUR + 1),
            ("granularity_day", "DAY", FURTHEST_DAYS_BACK_NOT_HOUR + 1),
            ("granularity_hour", "HOUR", FURTHEST_DAYS_BACK_HOUR + 1),
            ("granularity_week", "WEEK", FURTHEST_DAYS_BACK_NOT_HOUR + 1),
            ("granularity_month", "MONTH", FURTHEST_DAYS_BACK_NOT_HOUR + 1),
        ]
    )
    def test_get_analytics_fail(self, name, granularity, days_back):
        analytics_info_dict = {
            'ad_account_id': DEFAULT_AD_ACCOUNT_ID,
            'start_date': date.today() - timedelta(days_back),
            'end_date': date.today(),
            'columns': ["ADVERTISER_ID","PIN_PROMOTION_ID","SPEND_IN_DOLLAR"],
            'granularity': granularity,
        }
        ad = Ad(
            ad_account_id=analytics_info_dict.pop('ad_account_id'),
            ad_id=DEFAULT_AD_ID,
            client=self.test_client,
        )
        with self.assertRaises(ApiException):
            ad.get_analytics(**analytics_info_dict)


class TestGetTargetingAnalytics(BaseTestCase):
    """
    Test getting targeting analytics
    """
    DAYS_BACK = 2
    FURTHEST_DAYS_BACK_HOUR = 7  # Futhest allowed days back for granularity HOUR
    FURTHEST_DAYS_BACK_NOT_HOUR = 90  # Futhest allowed days back for any granularity but HOUR

    @parameterized.expand(
        [
            ("granularity_total","TOTAL"),
            ("granularity_day", "DAY"),
            ("granularity_week", "WEEK"),
            ("granularity_month", "MONTH"),
        ]
    )
    def test_get_ad_targeting_analytics_success(self, name, granularity):
        analytics_info_dict = {
            'ad_account_id': DEFAULT_AD_ACCOUNT_ID,
            'start_date': date.today() - timedelta(self.DAYS_BACK),
            'end_date': date.today(),
            'targeting_types':["GENDER"],
            'columns': ["SPEND_IN_MICRO_DOLLAR","SPEND_IN_DOLLAR", "TOTAL_ENGAGEMENT"],
            'granularity': granularity,
        }
        ad = Ad(
            ad_account_id=analytics_info_dict.pop('ad_account_id'),
            ad_id=DEFAULT_AD_ID,
            client=self.test_client,
        )
        ad_analytics = ad.get_targeting_analytics(**analytics_info_dict)
        self.assertIsNotNone(ad_analytics)
        self.assertIsNotNone(ad_analytics.raw_response)
        analytics_response = ad_analytics.raw_response.get('data')
        for dict_item in analytics_response:
            self.assertIsNotNone(dict_item.get('metrics'))
            for column in analytics_info_dict.get('columns'):
                self.assertIn(column, dict_item.get('metrics'))
            if granularity != 'TOTAL':
                self.assertIn('DATE', dict_item.get('metrics'))
    
    @parameterized.expand(
        [
            ("granularity_total","TOTAL", FURTHEST_DAYS_BACK_NOT_HOUR + 1),
            ("granularity_day", "DAY", FURTHEST_DAYS_BACK_NOT_HOUR + 1),
            ("granularity_hour", "HOUR", FURTHEST_DAYS_BACK_HOUR + 1),
            ("granularity_week", "WEEK", FURTHEST_DAYS_BACK_NOT_HOUR + 1),
            ("granularity_month", "MONTH", FURTHEST_DAYS_BACK_NOT_HOUR + 1),
        ]
    )
    def test_get_ad_targeting_analytics_fail(self, name, granularity, days_back):
        analytics_info_dict = {
            'ad_account_id': DEFAULT_AD_ACCOUNT_ID,
            'start_date': date.today() - timedelta(days_back),
            'end_date': date.today(),
            'targeting_types':["GENDER"],
            'columns': ["SPEND_IN_MICRO_DOLLAR","SPEND_IN_DOLLAR", "TOTAL_ENGAGEMENT"],
            'granularity': granularity,
        }
        ad = Ad(
            ad_account_id=analytics_info_dict.pop('ad_account_id'),
            ad_id=DEFAULT_AD_ID,
            client=self.test_client,
        )
        with self.assertRaises(ApiException):
            ad.get_targeting_analytics(**analytics_info_dict)
