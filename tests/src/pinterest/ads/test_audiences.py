"""
Test Audience Model
"""

from unittest import TestCase
from unittest.mock import patch

from pinterest.generated.client.model.audience import Audience as GeneratedAudience
from pinterest.generated.client.model.audience_rule import AudienceRule

from pinterest.ads.audiences import Audience


class TestAudience(TestCase):
    """
    Test Audience model and its higher level functions
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_ad_account_id = "777777777777"
        self.test_audience_id = "111111111111"

    @patch('pinterest.ads.audiences.AudiencesApi.audiences_get')
    def test_create_audience_model_using_existing_audience(self, audiences_get_mock):
        """
        Test if a Audience model/object is created successfully with correct audience_id
        """

        audiences_get_mock.return_value = GeneratedAudience(
            ad_account_id=self.test_ad_account_id,
            id=self.test_audience_id,
            name="Test Audience",
            audience_type="VISITOR",
            description="Test Description",
            rule=AudienceRule(
                prefill = True,
                retention_days = 7,
                visitor_source_id = "123123123123",
                ),
            size=100000,
            status="READY",
            created_timestamp=1499361351,
            updated_timestamp=1499361351,
            )

        audience_response = Audience(ad_account_id=self.test_ad_account_id, audience_id=self.test_audience_id)

        assert getattr(audience_response, '_id') == self.test_audience_id
        assert getattr(audience_response, '_audience_type') == 'VISITOR'

    @patch('pinterest.ads.audiences.AudiencesApi.audiences_create')
    @patch('pinterest.ads.audiences.AudiencesApi.audiences_get')
    def test_create_new_audience(self, audiences_get_mock, audiences_create_mock):
        """
        Test if a Audience model/object is created successfully with correct information
        """
        audiences_create_mock.return_value = GeneratedAudience(
            ad_account_id=self.test_ad_account_id,
            id=self.test_audience_id,
            name="Test Audience",
            audience_type="VISITOR",
            description="Test Description",
            rule=AudienceRule(
                prefill = True,
                retention_days = 7,
                visitor_source_id = "123123123123",
                ),
            size=100000,
            status="READY",
            created_timestamp=1499361351,
            updated_timestamp=1499361351,
            )
        audiences_get_mock.return_value = audiences_create_mock.return_value

        created_audience = Audience.create(
            ad_account_id=self.test_ad_account_id,
            name="Test Audience",
            rule=dict(
                prefill = True,
                retention_days = 7,
                visitor_source_id = "123123123123",
                ),
                audience_type="VISITOR",
                description="TEST DESCRIPTION",
        )

        assert created_audience
        assert getattr(created_audience, '_id') == self.test_audience_id
        assert getattr(created_audience, '_name') == "Test Audience"

    @patch('pinterest.ads.audiences.AudiencesApi.audiences_update')
    @patch('pinterest.ads.audiences.AudiencesApi.audiences_get')
    def test_update_audience_with_kwargs(self, audiences_get_mock, audiences_update_mock):
        """
        Test if a given audience is updated successfully with passed in keyword arguments
        """
        old_name, new_name = "Test Old Audience Name", "Test New Audience Name"
        old_audience_type, new_audience_type = "VISITOR", "ENGAGEMENT"

        audiences_get_mock.return_value = GeneratedAudience(
            ad_account_id=self.test_ad_account_id,
            id=self.test_audience_id,
            name=old_name,
            audience_type=old_audience_type,
            description="Test Description",
            rule=AudienceRule(
                prefill = True,
                retention_days = 7,
                visitor_source_id = "123123123123",
                ),
            size=100000,
            status="READY",
            created_timestamp=1499361351,
            updated_timestamp=1499361351,
            )

        audiences_update_mock.return_value = GeneratedAudience(
            ad_account_id=self.test_ad_account_id,
            id=self.test_audience_id,
            name=new_name,
            audience_type=new_audience_type,
            description="Test Description",
            rule=AudienceRule(
                prefill = True,
                retention_days = 7,
                visitor_source_id = "123123123123",
                ),
            size=100000,
            status="READY",
            created_timestamp=1499361351,
            updated_timestamp=1499361351,
            )

        audience_response = Audience(ad_account_id=self.test_ad_account_id, audience_id=self.test_audience_id)
        audiences_get_mock.return_value = audiences_update_mock.return_value
        update_response = audience_response.update_fields(name=new_name, audience_type=new_audience_type)

        assert update_response
        assert getattr(audience_response, '_name') == new_name
        assert getattr(audience_response, '_audience_type') == new_audience_type

    @patch('pinterest.ads.audiences.AudiencesApi.audiences_get')
    @patch('pinterest.ads.audiences.AudiencesApi.audiences_list')
    def test_get_all_audiences_in_ad_account(self, audiences_list_mock, audiences_get_mock):
        """
        Test class method returns all Audiences in a given ad_account in a list
        """
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
