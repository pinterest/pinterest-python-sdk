'''
Test AdGroup Model
'''
from unittest import TestCase
from unittest.mock import patch

from openapi_generated.pinterest_client.model.ad_response import AdResponse
from openapi_generated.pinterest_client.model.ad_group_response import AdGroupResponse
from openapi_generated.pinterest_client.model.ad_group_array_response import AdGroupArrayResponse
from openapi_generated.pinterest_client.model.ad_group_array_response_element import AdGroupArrayResponseElement
from openapi_generated.pinterest_client.model.targeting_spec import TargetingSpec

from pinterest.ads.ad_groups import AdGroup
from pinterest.ads.ads import Ad

class TestAdGroup(TestCase):
    '''
    Test AdGroup Model and its higher level functions
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_campaign_id = "111111111111"
        self.test_ad_account_id = "777777777777"
        self.test_ad_group_id = "888888888888"

    @patch('pinterest.ads.ad_groups.AdGroupsApi.ad_groups_get')
    def test_create_ad_group_model_using_existing_adgroup(self, ad_group_get_mock):
        '''
        Test if AdGroup model/object is created successfully with correct account_id, campaign_id
        '''

        ad_group_get_mock.return_value = AdGroupResponse(
            id=self.test_ad_group_id,
            ad_account_id=self.test_ad_account_id,
            campaign_id=self.test_campaign_id,
            name='SDK_TEST_CLIENT_ADGROUP',
            created_time=1461077800,
            status='ACTIVE',
        )

        ad_group_response = AdGroup(
            ad_account_id=self.test_ad_account_id,
            ad_group_id=self.test_ad_group_id,
        )

        assert getattr(ad_group_response, '_id') == self.test_ad_group_id
        assert getattr(ad_group_response, '_ad_account_id') == self.test_ad_account_id
        assert getattr(ad_group_response, '_campaign_id') == self.test_campaign_id
        assert getattr(ad_group_response, '_created_time') == 1461077800
        assert getattr(ad_group_response, '_status')

    @patch('pinterest.ads.ad_groups.AdGroupsApi.ad_groups_create')
    @patch('pinterest.ads.ad_groups.AdGroupsApi.ad_groups_get')
    def test_create_ad_group_model_new_ad_group(self, ad_group_get_mock, ad_group_create_mock):
        """
        Test if a AdGroup model/object is created successfully with correct account_id and
        new campaign information
        """
        ad_group_create_mock.__name__ = 'ad_groups_create'
        ad_group_create_mock.return_value = AdGroupArrayResponse(
            items=[
                AdGroupArrayResponseElement(
                    data=AdGroupResponse(
                        id=self.test_ad_group_id,
                        ad_account_id=self.test_ad_account_id,
                        campaign_id=self.test_campaign_id,
                        name='SDK_TEST_CLIENT_ADGROUP',
                        status='ACTIVE'
                    ),
                    exceptions=[]
                )
            ]
        )

        ad_group_get_mock.return_value = AdGroupResponse(
            id=self.test_ad_group_id,
            ad_account_id=self.test_ad_account_id,
            campaign_id=self.test_campaign_id,
            name='SDK_TEST_CLIENT_ADGROUP',
            status='ACTIVE'
        )

        created_ad_group = AdGroup.create(
            ad_account_id=self.test_ad_account_id,
            campaign_id=self.test_campaign_id,
            billable_event='CLICKTHROUGH',
            name='SDK_TEST_CLIENT_ADGROUP',
            auto_targeting_enabled=False
        )

        assert created_ad_group
        assert getattr(created_ad_group, '_id')
        assert getattr(created_ad_group, '_ad_account_id') == self.test_ad_account_id
        assert getattr(created_ad_group, '_campaign_id') == self.test_campaign_id
        assert getattr(created_ad_group, '_name') == 'SDK_TEST_CLIENT_ADGROUP'

    @patch('pinterest.ads.ad_groups.AdGroupsApi.ad_groups_update')
    @patch('pinterest.ads.ad_groups.AdGroupsApi.ad_groups_get')
    def test_update_ad_group(self, get_mock, update_mock):
        """
        Test if AdGroup model can be updated successfully
        """
        update_mock.__name__ = "ad_groups_update"
        new_name = "SDK_AD_GROUP_NEW_NAME"
        new_spec = {
                "gender": ["male"]
        }

        get_mock.return_value = AdGroupResponse(
            id=self.test_ad_group_id,
            ad_account_id=self.test_ad_account_id,
            campaign_id=self.test_campaign_id,
            name='SDK_TEST_CLIENT_ADGROUP',
        )
        ad_group_response = AdGroup(
            ad_account_id=self.test_ad_account_id,
            ad_group_id=self.test_ad_group_id,
        )

        update_mock.return_value = AdGroupArrayResponse(
            items=[
                AdGroupArrayResponseElement(
                    data=AdGroupResponse(
                        id=self.test_ad_group_id,
                        ad_account_id=self.test_ad_account_id,
                        campaign_id=self.test_campaign_id,
                        name=new_name,
                        targeting_spec=TargetingSpec(**new_spec)
                    ),
                    exceptions=[]
                )
            ]
        )
        get_mock.return_value = update_mock.return_value.items[0].data
        update_response = ad_group_response.update_fields(
            name=new_name,
            targeting_spec=new_spec
        )

        assert update_response == True
        assert getattr(ad_group_response, "_name") == new_name
        assert str(getattr(ad_group_response, "_targeting_spec")) == str(new_spec)

    @patch('pinterest.ads.ad_groups.AdGroupsApi.ad_groups_list')
    @patch('pinterest.ads.ad_groups.AdGroupsApi.ad_groups_get')
    def test_get_list_ad_group(self, get_mock, list_mock):
        """
        Test if AdGroup's function get_all can be used successfully
        """
        list_mock.__name__ = "ad_groups_list"
        get_mock.__name__ = "ad_groups_get"
        list_mock.return_value = {
            "items": [
                {
                "name": "Ad Group For Pin: 687195905986",
                "status": "ACTIVE",
                "budget_in_micro_currency": 5000000,
                "bid_in_micro_currency": 5000000,
                "bid_strategy_type": "AUTOMATIC_BID",
                "budget_type": "DAILY",
                "start_time": 5686848000,
                "end_time": 5705424000,
                "targeting_spec": {
                    "property1": [
                    "string"
                    ],
                    "property2": [
                    "string"
                    ]
                },
                "lifetime_frequency_cap": 100,
                "tracking_urls": {
                    "impression": [
                    "URL1",
                    "URL2"
                    ],
                    "click": [
                    "URL1",
                    "URL2"
                    ],
                    "engagement": [
                    "URL1",
                    "URL2"
                    ],
                    "buyable_button": [
                    "URL1",
                    "URL2"
                    ],
                    "audience_verification": [
                    "URL1",
                    "URL2"
                    ]
                },
                "auto_targeting_enabled": True,
                "placement_group": "ALL",
                "pacing_delivery_type": "STANDARD",
                "campaign_id": "626736533506",
                "billable_event": "CLICKTHROUGH",
                "id": "2680060704746",
                "ad_account_id": "549755885175",
                "created_time": 1476477189,
                "updated_time": 1476477189,
                "type": "adgroup",
                "conversion_learning_mode_type": "ACTIVE",
                "summary_status": "RUNNING",
                "feed_profile_id": "626736533506",
                "dca_assets": None,
                }
            ],
            "bookmark": "test_book_mark"
            }

        ad_groups, bookmark = AdGroup.get_all(
            ad_account_id=self.test_ad_account_id,
            ad_group_ids=self.test_ad_group_id,
            page_size=1,
        )

        get_mock.assert_not_called()

        assert ad_groups
        assert bookmark.get_bookmark_token() == "test_book_mark"
        assert getattr(ad_groups[0], "_id") == "2680060704746"

    @patch('pinterest.ads.ads.AdsApi.ads_get')
    @patch('pinterest.ads.ads.AdsApi.ads_list')
    @patch('pinterest.ads.ad_groups.AdGroupsApi.ad_groups_get')
    def test_list_ads_in_ad_group(self, ad_group_get_mock, ad_list_mock, ad_get_mock):
        """
        Test if Ad Group can return all Ads
        """
        ad_group_get_mock.__name__ = "ads_get"
        ad_list_mock.__name__ = "ads_list"
        ad_get_mock.__name__ = "ad_groups_get"

        ad_group_get_mock.return_value = AdGroupResponse(
            id=self.test_ad_group_id,
            ad_account_id=self.test_ad_account_id,
            campaign_id=self.test_campaign_id,
            name='SDK_TEST_CLIENT_ADGROUP',
            created_time=1461077800,
            status='ACTIVE',
        )

        ad_list_mock.return_value = {
            "items": [
                {
                    "ad_group_id": "2680059592705",
                    "android_deep_link": "string",
                    "carousel_android_deep_links": [
                        "string"
                    ],
                    "carousel_destination_urls": [
                        "string"
                    ],
                    "carousel_ios_deep_links": [
                        "string"
                    ],
                    "click_tracking_url": "string",
                    "creative_type": "REGULAR",
                    "destination_url": "string",
                    "ios_deep_link": "string",
                    "is_pin_deleted": False,
                    "is_removable": False,
                    "name": "string",
                    "pin_id": "394205773611545468",
                    "status": "ACTIVE",
                    "tracking_urls": {
                        "impression": [
                        "URL1",
                        "URL2"
                        ],
                        "click": [
                        "URL1",
                        "URL2"
                        ],
                        "engagement": [
                        "URL1",
                        "URL2"
                        ],
                        "buyable_button": [
                        "URL1",
                        "URL2"
                        ],
                        "audience_verification": [
                        "URL1",
                        "URL2"
                        ]
                    },
                    "view_tracking_url": "string",
                    "ad_account_id": "549755885175",
                    "campaign_id": "626735565838",
                    "collection_items_destination_url_template": "string",
                    "created_time": 1451431341,
                    "id": "687195134316",
                    "rejected_reasons": [
                        "HASHTAGS"
                    ],
                    "rejection_labels": [
                        "string"
                    ],
                    "review_status": "PENDING",
                    "type": "pinpromotion",
                    "updated_time": 1451431341,
                    "summary_status": "APPROVED"
                }
            ],
            "bookmark": "test_bookmark"
        }
        ad_get_mock.return_value = AdResponse(
            id="687195134316",
            ad_account_id=self.test_ad_account_id,
            name='My SDK ad',
            created_time=1461077800,
        )

        ad_group = AdGroup(
            ad_account_id=self.test_ad_account_id,
            ad_group_id=self.test_ad_group_id,
        )
        ads, bookmark = ad_group.list_ads(ad_ids="687195134316", page_size=1)

        assert ad_group
        assert ads
        assert bookmark.get_bookmark_token() == "test_bookmark"
        assert isinstance(ads[0], Ad)
        assert getattr(ads[0], "_id") == "687195134316"
