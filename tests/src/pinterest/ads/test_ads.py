from unittest import TestCase
from unittest.mock import patch

from openapi_generated.pinterest_client.model.ad_response import AdResponse
from openapi_generated.pinterest_client.model.entity_status import EntityStatus
from openapi_generated.pinterest_client.model.ad_array_response import AdArrayResponse
from openapi_generated.pinterest_client.model.ad_array_response_element import AdArrayResponseElement
from openapi_generated.pinterest_client.model.exception import Exception as ModelException

from pinterest.ads.ads import Ad

class TestAd(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_ad_group_id = "111111111111"
        self.test_ad_account_id = "777777777777"
        self.test_ad_id = "9999999999999"
        self.test_pin_id="222222"


    @patch('pinterest.ads.ads.AdsApi.ads_get')
    def test_create_ad_model_using_existing_ad(self, ads_get_mock):
        '''
        Test if Ad model/object is created successfully with correct account_id, campaign_id
        '''

        ads_get_mock.return_value = AdResponse(
            id=self.test_ad_id,
            ad_account_id=self.test_ad_account_id,
            name='My SDK ad',
            created_time=1461077800,
            # status='ACTIVE',
        )

        ad_response = Ad(
            ad_account_id=self.test_ad_account_id,
            ad_id=self.test_ad_id,
        )

        assert getattr(ad_response, '_id') == self.test_ad_id
        assert getattr(ad_response, '_ad_account_id') == self.test_ad_account_id
        assert getattr(ad_response, '_created_time') == 1461077800
        assert getattr(ad_response, '_name') == 'My SDK ad'
    
    @patch('pinterest.ads.ads.AdsApi.ads_create')
    @patch('pinterest.ads.ads.AdsApi.ads_get')
    def test_create_new_ad(self, ads_get_mock, ads_create_mock):
        """
        Test if Ad model can be created
        """
        ads_create_mock.__name__ = "ads_create"
        ads_create_mock.return_value = AdArrayResponse(
            items=[
                AdArrayResponseElement(
                    data=AdResponse(
                        id=self.test_ad_id,
                        ad_account_id=self.test_ad_account_id,
                        ad_group_id=self.test_ad_group_id,
                        name='My SDK ad',
                    ),
                    exceptions=ModelException(code=0, message='')
                )
            ]
        )
        ads_get_mock.return_value = AdResponse(
            id=self.test_ad_id,
            ad_account_id=self.test_ad_account_id,
            name='My SDK ad',
            created_time=1461077800,
        )


        created_ad = Ad.create(
            ad_account_id=self.test_ad_account_id,
            ad_group_id=self.test_ad_group_id,
            creative_type='REGULAR',
            pin_id=self.test_pin_id,
            name='My SDK ad',
            status='ACTIVE',
        )
    
        assert created_ad
        assert getattr(created_ad, '_id')
        assert getattr(created_ad, '_ad_account_id') == self.test_ad_account_id
        assert getattr(created_ad, '_name') == 'My SDK ad'

    @patch('pinterest.ads.ads.AdsApi.ads_list')
    @patch('pinterest.ads.ads.AdsApi.ads_get')
    def test_get_list_ad(self, get_mock, list_mock):
        """
        Test if function get_all in Ad Model can be used successfully
        """
        list_mock.__name__ = 'ads_list'
        get_mock.__name__ = 'ads_get'

        list_mock.return_value = {
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
        
        ads, bookmark = Ad.get_all(
            ad_account_id=self.test_ad_account_id,
            page_size=1,
        )

        get_mock.assert_not_called()

        assert ads
        assert bookmark.get_bookmark_token() == "test_bookmark"
        print(ads[0])
        assert getattr(ads[0], "_id") == "687195134316"

    @patch('pinterest.ads.ads.AdsApi.ads_update')
    @patch('pinterest.ads.ads.AdsApi.ads_get')
    def test_update_ad_(self, get_mock, update_mock):
        """
        Test if Ad model can be updated successfully
        """
        update_mock.__name__ = "ads_update"

        new_name = "NEW_AD_NAME"
        new_status = "PAUSED"

        get_mock.return_value = AdResponse(
            id=self.test_ad_id,
            ad_account_id=self.test_ad_account_id,
            name='SDK_TEST_AD_NAME',
            created_time=1461077800,
            status=EntityStatus('ACTIVE'),
        )

        update_mock.return_value = AdArrayResponse(
            items=[
                AdArrayResponseElement(
                    data=AdResponse(
                        id=self.test_ad_id,
                        ad_account_id=self.test_ad_account_id,
                        ad_group_id=self.test_ad_group_id,
                        name=new_name,
                        status=EntityStatus(new_status),
                    ),
                    exceptions=ModelException(code=0, message='')
                )
            ]
        )

        ad = Ad(
            ad_account_id=self.test_ad_account_id,
            ad_id=self.test_ad_id,
        )

        get_mock.return_value = update_mock.return_value.items[0].data
        ad.update_fields(
            name=new_name,
            status=new_status,
        )

        assert ad
        assert getattr(ad, "_name") == new_name
        assert getattr(ad, "_status") == EntityStatus(new_status)
