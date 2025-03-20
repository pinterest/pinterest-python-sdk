"""
Test Campaign Model
"""

from unittest.mock import patch

from openapi_generated.pinterest_client.model.objective_type import ObjectiveType
from openapi_generated.pinterest_client.exceptions import ApiValueError
from openapi_generated.pinterest_client.exceptions import NotFoundException

from pinterest.ads.ad_groups import AdGroup
from pinterest.ads.campaigns import Campaign
from pinterest.utils.sdk_exceptions import SdkException
from pinterest.utils.bookmark import Bookmark

from integration_tests.base_test import BaseTestCase
from integration_tests.config import DEFAULT_AD_ACCOUNT_ID


class TestCreateCampaign(BaseTestCase):
    """
    Test creating Campaign model
    """
    def test_create_campaign_success(self):
        """
        Test creating a new Campaign successfully
        """
        campaign = Campaign.create(
            client=self.test_client,
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            name="SDK Test Campaign",
            objective_type="AWARENESS",
            daily_spend_cap=10000000,
        )

        assert campaign
        assert getattr(campaign, '_id')
        assert getattr(campaign, '_name') == "SDK Test Campaign"
        assert getattr(campaign, '_objective_type') == ObjectiveType("AWARENESS")
        assert getattr(campaign, "_tracking_urls") is None

    def test_create_campaign_failure_without_budget(self):
        """
        Verify a new Campaign response failure and catching exceptions
        """
        campaign_arguments = dict(
            client=self.test_client,
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            name="SDK Test Campaign",
            objective_type="AWARENESS",
        )

        self.assertRaisesRegex(
            SdkException,
            r"^[\S\s]*code 2384[\S\s]*$",
            Campaign.create,
            **campaign_arguments)

    def test_create_campaign_failure_incorrect_objective_type(self):
        """
        Test creating a new Campaign failing due to incorrect objective_type
        """
        campaign_arguments = dict(
            client=self.test_client,
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            name="SDK Test Campaign",
            objective_type="INCORRECT_OBJECTIVE_TYPE",
            daily_spend_cap=10000000,
        )
        with self.assertRaisesRegex(ApiValueError, "Invalid"):
            Campaign.create(**campaign_arguments)


class TestGetCampaign(BaseTestCase):
    """
    Test creating Campaign model
    """
    def test_get_campaign_success(self):
        """
        Test getting an existing Campaign successfully
        """
        existing_campaign_id = self.campaign_utils.get_campaign_id()
        campaign = Campaign(
            client=self.test_client,
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            campaign_id=existing_campaign_id,
        )

        assert campaign
        assert getattr(campaign, '_id')
        assert getattr(campaign, '_name') == "SDK Test Campaign"
        assert getattr(campaign, '_objective_type') == ObjectiveType("AWARENESS")

    def test_get_campaign_failure_invalid_campaign_id(self):
        """
        Test getting an a Campaign failure due to invalid campaign id
        """
        non_existant_campaign_id = "123123123123"
        campaign_arguments = dict(
            client=self.test_client,
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            campaign_id=non_existant_campaign_id,
        )

        with self.assertRaises(NotFoundException):
            Campaign(**campaign_arguments)


class TestChangeCampaignStatus(BaseTestCase):
    """
    Test change status of existing campaigns
    """
    def test_pause_campaign_successfully(self):
        """
        Test pausing an existing active campaign successfully
        """
        campaign = self.campaign_utils.create_new_campaign(status="ACTIVE")
        campaign.pause()

        assert getattr(campaign, '_status') == "PAUSED"

    def test_activate_campaign_successfully(self):
        """
        Test activate an existing paused campaign successfully
        """
        campaign = self.campaign_utils.create_new_campaign(status="PAUSED")
        campaign.activate()

        assert getattr(campaign, '_status') == "ACTIVE"

    def test_archive_campaign_successfully(self):
        """
        Test archiving an existing paused campaign successfully
        """
        campaign = self.campaign_utils.create_new_campaign(status="PAUSED")
        campaign.archive()

        assert getattr(campaign, '_status') == "ARCHIVED"


class TestGetAllCampaigns(BaseTestCase):
    """
    Test Get All Campaigns class method
    """
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

        campaigns_list, _ = Campaign.get_all(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            campaign_ids=list(created_campaign_ids),
        )

        assert campaigns_get_mock.call_count - 1 == NUMBER_OF_CAMPAIGNS_TO_CREATE
        assert len(created_campaign_ids) == len(campaigns_list)

        get_all_campaigns_ids = set()
        for campaign in campaigns_list:
            get_all_campaigns_ids.add(getattr(campaign, '_id'))
            assert isinstance(campaign, Campaign)

        assert created_campaign_ids == get_all_campaigns_ids

    def test_list_ad_groups(self):
        """
        Test if all campaigns are returned for a given Ad Account ID
        """
        campaign = self.campaign_utils.create_new_campaign()

        created_ad_groups = []
        for _ in range(3):
            created_ad_groups.append(
                AdGroup.create(
                    client=self.test_client,
                    ad_account_id=getattr(campaign, '_ad_account_id'),
                    campaign_id=getattr(campaign, '_id'),
                    billable_event="IMPRESSION",
                    name="SDK_INTEGRATION_TEST_ADGROUP",
                    auto_targeting_enabled=False,
                    bid_in_micro_currency=10000000,
                    targeting_spec=dict(
                        age_bucket=["35-44"],
                        location=["US"],
                    )
                )
            )

        returned_ad_groups, bookmark = campaign.list_ad_groups(page_size=2)
        self.assertEqual(2, len(returned_ad_groups))
        self.assertIsNotNone(bookmark)

        self.assertEqual(getattr(returned_ad_groups[0], '_id'), getattr(created_ad_groups[0], '_id'))
        self.assertEqual(getattr(returned_ad_groups[1], '_id'), getattr(created_ad_groups[1], '_id'))

    def test_get_next_page_of_campaigns(self):
        """
        Test getting next page of campaigns using `Bookmark.get_next()`
        """
        new_ad_account = self.ad_account_utils.create_new_ad_account()

        NUMBER_OF_CAMPAIGNS_TO_CREATE = 6
        created_campaign_ids = set(
            getattr(
                self.campaign_utils.create_new_campaign(
                    ad_account_id=getattr(new_ad_account, '_id')
                    ),
                    '_id'
                ) for _ in range(NUMBER_OF_CAMPAIGNS_TO_CREATE)
        )

        assert len(created_campaign_ids) == NUMBER_OF_CAMPAIGNS_TO_CREATE

        campaigns_list_1, bookmark_1 = Campaign.get_all(
            ad_account_id=getattr(new_ad_account, '_id'),
            page_size=NUMBER_OF_CAMPAIGNS_TO_CREATE//2,
        )

        assert isinstance(bookmark_1, Bookmark)

        campaign_list_2, _ = bookmark_1.get_next()

        campaign_list_combined = campaigns_list_1 + campaign_list_2

        assert len(created_campaign_ids) == len(campaign_list_combined)

        get_all_campaigns_ids = set()
        for campaign in campaign_list_combined:
            get_all_campaigns_ids.add(getattr(campaign, '_id'))
            assert isinstance(campaign, Campaign)

        assert created_campaign_ids == get_all_campaigns_ids
