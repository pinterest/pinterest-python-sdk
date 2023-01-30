"""
Test Campaign Model
"""

from unittest import TestCase
from unittest.mock import patch

from openapi_generated.pinterest_client.model.campaign_response import CampaignResponse
from openapi_generated.pinterest_client.model.campaign_create_response import CampaignCreateResponse
from openapi_generated.pinterest_client.model.campaign_create_response_item import CampaignCreateResponseItem
from openapi_generated.pinterest_client.model.campaign_create_response_data import CampaignCreateResponseData
from openapi_generated.pinterest_client.model.campaign_update_response import CampaignUpdateResponse
from openapi_generated.pinterest_client.model.objective_type import ObjectiveType

from pinterest.ads.campaigns import Campaign


class TestCampaign(TestCase):
    """
    Test Campaign model and its higher level functions
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_campaign_id = "111111111111"
        self.test_ad_account_id = "777777777777"

    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_get')
    def test_create_campaign_model_using_existing_campaign(self, campaigns_get_mock):
        """
        Test if a Campaign model/object is created successfully with correct account_id, campaign_id
        """

        campaigns_get_mock.return_value = CampaignResponse(
            id=self.test_campaign_id,
            ad_account_id=self.test_ad_account_id,
            objective_type=ObjectiveType("AWARENESS"),
            created_time=1461077800,
            status='ACTIVE',
            )

        campaign_response = Campaign(
            ad_account_id=self.test_ad_account_id,
            campaign_id=self.test_campaign_id,
        )

        assert getattr(campaign_response, '_id') == self.test_campaign_id
        assert getattr(campaign_response, '_ad_account_id') == self.test_ad_account_id
        assert getattr(campaign_response, '_objective_type') == ObjectiveType("AWARENESS")
        assert getattr(campaign_response, '_created_time') == 1461077800
        assert getattr(campaign_response, '_status')


    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_create')
    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_get')
    def test_create_campaign_model_new_campaign(self, campaigns_get_mock, campaigns_create_mock):
        """
        Test if a Campaign model/object is created successfully with correct account_id and
        new campaign information
        """
        campaigns_create_mock.__name__ = "campaigns_create"
        campaigns_create_mock.return_value = CampaignCreateResponse(
            items=[
                CampaignCreateResponseItem(
                    data=CampaignCreateResponseData(
                        id="123123123123",
                        ad_account_id=self.test_ad_account_id,
                        name='SDK_TEST_CLIENT',
                        objective_type=ObjectiveType("AWARENESS"),
                        daily_spend_cap=100000,
                    ),
                    exceptions=[]
                )
            ]
            )
        campaigns_get_mock.return_value = CampaignResponse(
            id="123123123123",
            ad_account_id=self.test_ad_account_id,
            name='SDK_TEST_CLIENT',
            objective_type=ObjectiveType("AWARENESS"),
            daily_spend_cap=100000,
        )

        created_campaign = Campaign.create(
            ad_account_id=self.test_ad_account_id,
            name='SDK_TEST_CLIENT',
            objective_type="AWARENESS",
            daily_spend_cap=100000,
        )

        assert created_campaign
        assert getattr(created_campaign, '_id')
        assert getattr(created_campaign, '_name') == 'SDK_TEST_CLIENT'


    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_update')
    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_get')
    def test_set_campaign_lifetime_budget(self, campaigns_get_mock, campaigns_update_mock):
        """
        Test if the lifetime budget of a campaign is updated correctly
        """
        old_lifetime_budget, new_lifetime_budget = 10, 20

        campaigns_get_mock.return_value = CampaignResponse(
            id=self.test_campaign_id,
            ad_account_id=self.test_ad_account_id,
            type='campaign',
            created_time=1461077800,
            status='ACTIVE',
            lifetime_spend_cap=old_lifetime_budget,
            )

        campaigns_update_mock.return_value = CampaignUpdateResponse(
            items=[
                CampaignCreateResponseItem(
                    data=CampaignCreateResponseData(
                        id=self.test_campaign_id,
                        ad_account_id=self.test_ad_account_id,
                        type='campaign',
                        created_time=1461077800,
                        status='ACTIVE',
                        lifetime_spend_cap=new_lifetime_budget,
                    ),
                    exceptions=[]
                )
            ]
            )

        campaign_response = Campaign(ad_account_id=self.test_ad_account_id, campaign_id=self.test_campaign_id)
        campaigns_get_mock.return_value = campaigns_update_mock.return_value.items[0].data
        update_response = campaign_response.set_lifetime_budget(new_lifetime_budget)

        assert update_response
        assert campaign_response.get_lifetime_budget() == new_lifetime_budget

    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_update')
    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_get')
    def test_set_campaign_daily_budget(self, campaigns_get_mock, campaigns_update_mock):
        """
        Test if the daily budget of a campaign is updated correctly
        """
        old_daily_budget, new_daily_budget = 10, 20

        campaigns_get_mock.return_value = CampaignResponse(
            id=self.test_campaign_id,
            ad_account_id=self.test_ad_account_id,
            type='campaign',
            created_time=1461077800,
            status='ACTIVE',
            daily_spend_cap=old_daily_budget,
            )
        
        campaigns_update_mock.return_value = CampaignUpdateResponse(
            items=[
                CampaignCreateResponseItem(
                    data=CampaignCreateResponseData(
                        id=self.test_campaign_id,
                        ad_account_id=self.test_ad_account_id,
                        type='campaign',
                        created_time=1461077800,
                        status='ACTIVE',
                        daily_spend_cap=new_daily_budget,
                    ),
                    exceptions=[]
                )
            ]
            )

        campaign_response = Campaign(ad_account_id=self.test_ad_account_id, campaign_id=self.test_campaign_id)
        campaigns_get_mock.return_value = campaigns_update_mock.return_value.items[0].data
        update_response = campaign_response.set_daily_budget(new_daily_budget)

        assert update_response
        assert campaign_response.get_daily_budget() == new_daily_budget

    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_update')
    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_get')
    def test_pause_campaign(self, campaigns_get_mock, campaigns_update_mock):
        """
        Test if the status of the campaign is updated to PAUSED successfully
        """
        old_status, new_status = 'ACTIVE', 'PAUSED'

        campaigns_get_mock.return_value = CampaignResponse(
            id=self.test_campaign_id,
            ad_account_id=self.test_ad_account_id,
            type='campaign',
            status=old_status,
            )

        campaigns_update_mock.return_value = CampaignUpdateResponse(
            items=[
                CampaignCreateResponseItem(
                    data=CampaignCreateResponseData(
                        id=self.test_campaign_id,
                        ad_account_id=self.test_ad_account_id,
                        type='campaign',
                        status=new_status,
                    ),
                    exceptions=[]
                )
            ]
            )

        campaign_response = Campaign(ad_account_id=self.test_ad_account_id, campaign_id=self.test_campaign_id)
        campaigns_get_mock.return_value = campaigns_update_mock.return_value.items[0].data
        update_response = campaign_response.pause()

        assert update_response
        assert getattr(campaign_response, '_status') == new_status

    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_update')
    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_get')
    def test_activate_campaign(self, campaigns_get_mock, campaigns_update_mock):
        """
        Test if the status of the campaign is updated to ACTIVE successfully
        """
        old_status, new_status = 'PAUSED', 'ACTIVE'

        campaigns_get_mock.return_value = CampaignResponse(
            id=self.test_campaign_id,
            ad_account_id=self.test_ad_account_id,
            type='campaign',
            status=old_status,
            )

        campaigns_update_mock.return_value = CampaignUpdateResponse(
            items=[
                CampaignCreateResponseItem(
                    data=CampaignCreateResponseData(
                        id=self.test_campaign_id,
                        ad_account_id=self.test_ad_account_id,
                        type='campaign',
                        status=new_status,
                    ),
                    exceptions=[]
                )
            ]
            )

        campaign_response = Campaign(ad_account_id=self.test_ad_account_id, campaign_id=self.test_campaign_id)
        campaigns_get_mock.return_value = campaigns_update_mock.return_value.items[0].data
        update_response = campaign_response.activate()

        assert update_response
        assert getattr(campaign_response, '_status') == new_status

    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_update')
    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_get')
    def test_archive_campaign(self, campaigns_get_mock, campaigns_update_mock):
        """
        Test if the status of the campaign is updated to ARCHIVED successfully
        """
        old_status, new_status = 'ACTIVE', 'ARCHIVED'

        campaigns_get_mock.return_value = CampaignResponse(
            id=self.test_campaign_id,
            ad_account_id=self.test_ad_account_id,
            type='campaign',
            status=old_status,
            )

        campaigns_update_mock.return_value = CampaignUpdateResponse(
            items=[
                CampaignCreateResponseItem(
                    data=CampaignCreateResponseData(
                        id=self.test_campaign_id,
                        ad_account_id=self.test_ad_account_id,
                        type='campaign',
                        status=new_status,
                    ),
                    exceptions=[]
                )
            ]
            )

        campaign_response = Campaign(ad_account_id=self.test_ad_account_id, campaign_id=self.test_campaign_id)
        campaigns_get_mock.return_value = campaigns_update_mock.return_value.items[0].data
        update_response = campaign_response.archive()

        assert update_response
        assert getattr(campaign_response, '_status') == new_status

    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_update')
    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_get')
    def test_update_campaign_with_kwargs(self, campaigns_get_mock, campaigns_update_mock):
        """
        Test if a given campaign is updated successfully with passed in keyword arguments
        """
        old_status, new_status = 'ACTIVE', 'ARCHIVED'
        old_name, new_name = 'SDK_TEST_CAMPAIGN', 'SDK_TEST_CAMPAIGN_UPDATED'
        old_daily_budget, new_daily_budget = 10, 20

        campaigns_get_mock.return_value = CampaignResponse(
            id=self.test_campaign_id,
            ad_account_id=self.test_ad_account_id,
            status=old_status,
            name=old_name,
            daily_spend_cap=old_daily_budget,
            )

        campaigns_update_mock.return_value = CampaignUpdateResponse(
            items=[
                CampaignCreateResponseItem(
                    data=CampaignCreateResponseData(
                        id=self.test_campaign_id,
                        ad_account_id=self.test_ad_account_id,
                        status=new_status,
                        name=new_name,
                        daily_spend_cap=new_daily_budget,

                    ),
                    exceptions=[]
                )
            ]
            )

        campaign_response = Campaign(ad_account_id=self.test_ad_account_id, campaign_id=self.test_campaign_id)
        campaigns_get_mock.return_value = campaigns_update_mock.return_value.items[0].data
        update_response = campaign_response.archive()

        assert update_response
        assert getattr(campaign_response, '_status') == new_status
        assert getattr(campaign_response, '_name') == new_name
        assert getattr(campaign_response, '_daily_spend_cap') == new_daily_budget

    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_get')
    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_list')
    def test_list_campaigns_in_ad_account(self, campaigns_list_mock, campaigns_get_mock):
        """
        Test if a given Campaigns returns all Campaigns in a given ad_account in a list
        """
        campaigns_list_mock.__name__ = "campaigns_list"
        campaigns_get_mock.__name__ = "campaigns_get"
        campaigns_list_mock.return_value = {
            "items": [
                {
                    "id": "123123123123",
                    "ad_account_id": self.test_ad_account_id,
                    "name": 'SDK_TEST_CLIENT',
                    "type": "campaign",
                    "daily_spend_cap": 100000,
                }
            ],
            "bookmark": "test_bookmark_string"
        }

        campaign_list, bookmark = Campaign.get_all(
            ad_account_id=self.test_ad_account_id,
            campaign_ids=["123123123123"],
            page_size=1
        )

        campaigns_get_mock.assert_not_called()

        assert campaign_list
        assert bookmark.get_bookmark_token() == "test_bookmark_string"
        assert isinstance(campaign_list[0], Campaign)
        assert campaign_list[0].get_daily_budget() == 100000
