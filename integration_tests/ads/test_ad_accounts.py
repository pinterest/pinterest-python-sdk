"""
Test Ad Account Model
"""
from datetime import date
from datetime import timedelta
from parameterized import parameterized
from unittest.mock import patch

from pinterest.ads.ad_accounts import AdAccount
from pinterest.ads.campaigns import Campaign
from pinterest.ads.audiences import Audience

from integration_tests.base_test import BaseTestCase
from integration_tests.config import OWNER_USER_ID
from integration_tests.config import DEFAULT_AD_ACCOUNT_ID


class TestAdAccount(BaseTestCase):
    """
    Test Ad Account model and its higher level functions
    """
    def test_create_ad_account(self):
        """
        Test creating a new ad_account
        """
        ad_account = AdAccount.create(
            client=self.test_client,
            country="US",
            name="SDK Test Ad Account",
            owner_user_id=OWNER_USER_ID,
        )

        assert ad_account
        assert getattr(ad_account, '_id')
        assert getattr(ad_account, '_name') == "SDK Test Ad Account"

    def test_get_existing_ad_account(self):
        """
        Test if a AdAccount model/object is created successfully with correct account_id
        """
        ad_account = AdAccount(
            ad_account_id=self.ad_account_utils.get_default_ad_account_id(),
            client=self.test_client
            )
        assert ad_account
        assert getattr(ad_account, '_id') == DEFAULT_AD_ACCOUNT_ID


class TestListCampaigns(BaseTestCase):
    """
    Test List Campaigns method for a given Ad Account
    """
    # pylint: disable=duplicate-code
    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_get')
    def test_get_all_campaigns(self, campaigns_get_mock):
        """
        Test if all campaigns are returned for a given Ad Account ID
        """
        NUMBER_OF_CAMPAIGNS_TO_CREATE = 3
        created_campaign_ids = set(
            getattr(self.campaign_utils.create_new_campaign(), '_id') for _ in range(NUMBER_OF_CAMPAIGNS_TO_CREATE)
        )

        assert len(created_campaign_ids) == NUMBER_OF_CAMPAIGNS_TO_CREATE

        ad_account = self.ad_account_utils.get_default_ad_account()
        campaigns_list, _ = ad_account.list_campaigns(
            campaign_ids=list(created_campaign_ids),
        )

        assert campaigns_get_mock.call_count - 1 == NUMBER_OF_CAMPAIGNS_TO_CREATE
        assert len(created_campaign_ids) == len(campaigns_list)

        get_all_campaigns_ids = set()
        for campaign in campaigns_list:
            get_all_campaigns_ids.add(getattr(campaign, '_id'))
            assert isinstance(campaign, Campaign)

        assert created_campaign_ids == get_all_campaigns_ids


class TestListAudiences(BaseTestCase):
    """
    Test List Audiences method for a given Ad Account
    """
    # pylint: disable=duplicate-code
    @patch('pinterest.ads.audiences.AudiencesApi.audiences_get')
    def test_get_all_audiences(self, audiences_get_mock):
        """
        Test if all audiences are returned for a given Ad Account ID
        """
        NUMBER_OF_AUDIENCES_TO_CREATE = 3
        created_audience_ids = set(
            getattr(self.audience_utils.create_new_audience(), '_id') for _ in range(NUMBER_OF_AUDIENCES_TO_CREATE)
        )

        assert len(created_audience_ids) == NUMBER_OF_AUDIENCES_TO_CREATE

        audiences_list, _ = Audience.get_all(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            order="DESCENDING",
            page_size=NUMBER_OF_AUDIENCES_TO_CREATE,
        )

        assert audiences_get_mock.call_count - 1 == NUMBER_OF_AUDIENCES_TO_CREATE
        assert len(created_audience_ids) == len(audiences_list)

        get_all_audiences_ids = set()
        for audience in audiences_list:
            get_all_audiences_ids.add(getattr(audience, '_id'))
            assert isinstance(audience, Audience)

        assert created_audience_ids == get_all_audiences_ids


class TestListCustomerLists(BaseTestCase):
    """
    Test List customer lists from Ad Account
    """
    def test_list_customer_list_success(self):
        """
        Test if Ad Account can lists customer lists
        """
        NUMBER_OF_NEW_CUSTOMER_LISTS = 3
        new_customer_list_ids = set()
        for _ in range(NUMBER_OF_NEW_CUSTOMER_LISTS):
            new_customer_list_ids.add(getattr(self.customer_list_utils.create_new_customer_list(), "_id"))

        assert len(new_customer_list_ids) == NUMBER_OF_NEW_CUSTOMER_LISTS

        ad_account = self.ad_account_utils.get_default_ad_account()
        new_customer_lists, _ = ad_account.list_customer_lists(
            order="DESCENDING",
            page_size=NUMBER_OF_NEW_CUSTOMER_LISTS,
        )

        get_all_customer_list_ids = set()
        for customer_list in new_customer_lists:
            get_all_customer_list_ids.add(getattr(customer_list, "_id"))

        assert new_customer_list_ids == get_all_customer_list_ids


class TestGetAnalytics(BaseTestCase):
    """
    Test getting Ad accounts analytics
    """
    DAYS_BACK = 2
    FURTHEST_BACK_HOUR = 7  # Futhest allowed days back for granularity HOUR
    MAX_RANGE_DAYS = 3  # Max time range in days for granularity HOUR
    FURTHEST_BACK_NOT_HOUR = 90  # Futhest allowed days back for any granularity but HOUR

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
        ad_account = AdAccount(
            ad_account_id=self.ad_account_utils.get_default_ad_account_id(),
            client=self.test_client
            )
        ad_account_analytics = ad_account.get_analytics(**analytics_info_dict)
        self.assertIsNotNone(ad_account_analytics)
        self.assertIsNotNone(ad_account_analytics.raw_response)


class TestGetTargetingAnalytics(BaseTestCase):

    def test_get_ad_targeting_analytics_success(self):
        analytics_info_dict = {
            'ad_account_id': DEFAULT_AD_ACCOUNT_ID,
            'start_date': date.today() - timedelta(2),
            'end_date': date.today(),
            'targeting_types':["GENDER"],
            'columns': ["ADVERTISER_ID","PIN_PROMOTION_ID","SPEND_IN_DOLLAR"],
            'granularity': 'DAY',
        }
        ad_account = AdAccount(
            ad_account_id=self.ad_account_utils.get_default_ad_account_id(),
            client=self.test_client
            )
        ad_analytics = ad_account.get_targeting_analytics(**analytics_info_dict)
        self.assertIsNotNone(ad_analytics)
        self.assertIsNotNone(ad_analytics.raw_response)
        self.assertIsNotNone(ad_analytics.raw_response.get('data'))
