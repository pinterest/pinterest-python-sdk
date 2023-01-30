"""
Test Error Handling
"""

from unittest import TestCase

from openapi_generated.pinterest_client.model.campaign_create_response import CampaignCreateResponse
from openapi_generated.pinterest_client.model.campaign_create_response_item import CampaignCreateResponseItem
from openapi_generated.pinterest_client.model.campaign_create_response_data import CampaignCreateResponseData
from openapi_generated.pinterest_client.model.exception import Exception as GeneratedException

from pinterest.utils.sdk_exceptions import SdkException
from pinterest.utils.error_handling import verify_api_response

class TestErrorHandling(TestCase):
    """
    Test Error Handling utility functions
    """

    def test_verify_api_response_without_exceptions(self):
        """
        Verify if the function successfully returns True when there are no errors in api response
        """
        test_api_response = CampaignCreateResponse(
            items=[
                CampaignCreateResponseItem(
                    data=CampaignCreateResponseData(
                        id="123123123123",
                        ad_account_id="456456456456",
                        name='SDK_TEST_CLIENT',
                    ),
                    exceptions=[]
                )
            ],
            )
        assert verify_api_response(test_api_response)

    def test_verify_api_response_with_exceptions(self):
        """
        Verify if the function throws `SdkException` when there are exceptions in api response
        """
        test_api_response = CampaignCreateResponse(
            items=[
                CampaignCreateResponseItem(
                    data=CampaignCreateResponseData(),
                    exceptions=[
                        GeneratedException(
                            code=1234,
                            message="Test exception caught."
                            )
                        ]
                )
            ],
            )
        self.assertRaises(SdkException, verify_api_response, response=test_api_response)
