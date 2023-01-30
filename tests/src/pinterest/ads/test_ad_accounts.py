"""
Test Ad Account Model
"""

from unittest import TestCase
from unittest.mock import patch

from openapi_generated.pinterest_client.model.ad_account import AdAccount as GeneratedAdAccount
from openapi_generated.pinterest_client.model.customer_list import CustomerList as GeneratedCustomerList
from openapi_generated.pinterest_client.model.country import Country
from openapi_generated.pinterest_client.model.ad_account_owner import AdAccountOwner
from openapi_generated.pinterest_client.model.currency import Currency

from openapi_generated.pinterest_client.model.campaign_response import CampaignResponse

from pinterest.ads.ad_accounts import AdAccount
from pinterest.ads.campaigns import Campaign
from pinterest.ads.audiences import Audience
from pinterest.ads.customer_lists import CustomerList


class TestAdAccount(TestCase):
    """
    Test Ad Account model and its higher level functions
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_ad_account_id = "777777777777"
        self.test_owner_user_id = "111111111111"
        self.test_customer_list_id = "22222222222"

    @patch('pinterest.ads.ad_accounts.AdAccountsApi.ad_accounts_get')
    def test_create_adaccount_model_using_existing_adaccount(self, ad_accounts_get_mock):
        """
        Test if a AdAccount model/object is created successfully with correct account_id
        """
        ad_accounts_get_mock.__name__ = "ad_accounts_get"

        ad_accounts_get_mock.return_value = GeneratedAdAccount(
            id=self.test_ad_account_id,
            name="Test Ad Account",
            owner=AdAccountOwner(username="TestOwner"),
            country=Country("US"),
            currency=Currency("USD"),
            permissions=[]
            )

        ad_account_response = AdAccount(ad_account_id=self.test_ad_account_id)

        assert getattr(ad_account_response, '_id') == self.test_ad_account_id
        assert getattr(ad_account_response, '_owner') == AdAccountOwner(username="TestOwner")
        assert getattr(ad_account_response, '_currency') == Currency("USD")

    @patch('pinterest.ads.ad_accounts.AdAccountsApi.ad_accounts_create')
    @patch('pinterest.ads.ad_accounts.AdAccountsApi.ad_accounts_get')
    def test_create_new_adaccount(self, ad_accounts_get_mock, ad_accounts_create_mock):
        """
        Test if a Ad Account model/object is created successfully with correct information
        """
        ad_accounts_get_mock.__name__ = "ad_accounts_create"
        ad_accounts_create_mock.__name__ = "ad_accounts_get"

        ad_accounts_create_mock.return_value = GeneratedAdAccount(
            id=self.test_ad_account_id,
            name="Test Ad Account",
            owner=AdAccountOwner(username="TestOwner"),
            country=Country("US"),
            currency=Currency("USD"),
            permissions=[]
            )
        ad_accounts_get_mock.return_value = ad_accounts_create_mock.return_value

        created_ad_account = AdAccount.create(
            country="US",
            name="Test Ad Account",
            owner_user_id=self.test_owner_user_id,
        )

        assert created_ad_account
        assert getattr(created_ad_account, '_id') == self.test_ad_account_id
        assert getattr(created_ad_account, '_name') == "Test Ad Account"

    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_get')
    @patch('pinterest.ads.campaigns.CampaignsApi.campaigns_list')
    @patch('pinterest.ads.ad_accounts.AdAccountsApi.ad_accounts_get')
    def test_list_campaigns_in_ad_account(self, ad_accounts_get_mock, campaigns_list_mock, campaigns_get_mock):
        """
        Test if a given Ad Acocunt returns all its Campaigns in a list
        """
        ad_accounts_get_mock.__name__ = "campaigns_get"
        campaigns_list_mock.__name__ = "campaigns_list"
        campaigns_get_mock.__name__ = "ad_accounts_get"

        ad_accounts_get_mock.return_value = GeneratedAdAccount(
            id=self.test_ad_account_id,
            name="Test Ad Account",
            owner=AdAccountOwner(username="TestOwner"),
            country=Country("US"),
            currency=Currency("USD"),
            permissions=[]
            )
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
        campaigns_get_mock.return_value = CampaignResponse(
            id="123123123123",
            ad_account_id=self.test_ad_account_id,
            name="SDK_TEST_CLIENT",
            type="campaign",
            daily_spend_cap=100000,
        )

        ad_account = AdAccount(ad_account_id=self.test_ad_account_id)
        campaign_list, bookmark = ad_account.list_campaigns(campaign_ids=["123123123123"], page_size=1)

        assert ad_account
        assert campaign_list
        assert bookmark.get_bookmark_token() == "test_bookmark_string"
        assert isinstance(campaign_list[0], Campaign)
        assert campaign_list[0].get_daily_budget() == 100000

    @patch('pinterest.ads.audiences.AudiencesApi.audiences_get')
    @patch('pinterest.ads.audiences.AudiencesApi.audiences_list')
    @patch('pinterest.ads.ad_accounts.AdAccountsApi.ad_accounts_get')
    def test_list_audiences_in_ad_account(self, ad_accounts_get_mock, audiences_list_mock, audiences_get_mock):
        """
        Test if a given Ad Acocunt returns all its Audiences in a list
        """

        ad_accounts_get_mock.__name__ = "audiences_get"
        audiences_list_mock.__name__ = "audiences_list"
        audiences_get_mock.__name__ = "ad_accounts_get"

        ad_accounts_get_mock.return_value = GeneratedAdAccount(
            id=self.test_ad_account_id,
            name="Test Ad Account",
            owner=AdAccountOwner(username="TestOwner"),
            country=Country("US"),
            currency=Currency("USD"),
            permissions=[]
            )
        audiences_list_mock.return_value = {
            "items": [
                {
                    "id": "123123123123",
                    "ad_account_id": self.test_ad_account_id,
                    "name": 'SDK_TEST_CLIENT',
                    "audience_type": "ENGAGEMENT",
                    "type": "audience",
                }
            ],
            "bookmark": None
        }

        audience_list, bookmark = Audience.get_all(
            ad_account_id=self.test_ad_account_id,
            page_size=1
        )

        audiences_get_mock.assert_not_called()

        assert audience_list
        assert not bookmark
        assert isinstance(audience_list[0], Audience)
        assert getattr(audience_list[0], '_audience_type') == "ENGAGEMENT"

    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_get')
    @patch('pinterest.ads.customer_lists.CustomerListsApi.customer_lists_list')
    @patch('pinterest.ads.ad_accounts.AdAccountsApi.ad_accounts_get')
    def test_list_customer_lists_in_ad_account(self, ad_account_get_mock, customer_list_list_mock, customer_list_get_mock):
        """
        Test if given Ad Account can return its Customer List
        """

        customer_list_list_mock.__name__ = "customer_lists_list"

        ad_account_get_mock.return_value = GeneratedAdAccount(
            id=self.test_ad_account_id,
            name="Test Ad Account",
            owner=AdAccountOwner(username="TestOwner"),
            country=Country("US"),
            currency=Currency("USD"),
            permissions=[]
        )
        customer_list_list_mock.return_value = {
            "items": [
                {
                    "ad_account_id": self.test_ad_account_id,
                    "created_time": 1452208622,
                    "id": self.test_customer_list_id,
                    "name": "Test Customer List",
                    "num_batches": 1,
                    "num_removed_user_records": 0,
                    "num_uploaded_user_records": 1.0,
                    "status": "PROCESSING",
                    "type": "customerlist",
                    "updated_time": 1499361351.0,
                    "exceptions": {},
                }
            ],
            "bookmark": "test_bookmark",
        }
        customer_list_get_mock.return_value = GeneratedCustomerList(
            ad_account_id=self.test_ad_account_id,
            id=self.test_customer_list_id,
            name="Test Customer List",
            num_batches=1.0,
            num_removed_user_records=0.0,
            num_uploaded_user_records=1.0,
            status="PROCESSING",
            type="customerlist",
            updated_time=1499361351.0,
            )

        ad_account = AdAccount(ad_account_id=self.test_ad_account_id)
        customer_lists, bookmark = ad_account.list_customer_lists(page_size=1)

        assert ad_account
        assert customer_lists
        assert bookmark.get_bookmark_token() == "test_bookmark"
        assert isinstance(customer_lists[0], CustomerList)
        assert getattr(customer_lists[0], "_name") == "Test Customer List"
