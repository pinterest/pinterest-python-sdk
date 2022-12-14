"""
Test Audiences Model
"""

from unittest.mock import patch

from pinterest.ads.audiences import Audience

from integration_tests.base_test import BaseTestCase
from integration_tests.config import DEFAULT_AD_ACCOUNT_ID


class TestAudience(BaseTestCase):
    """
    Test Audience model and its higher level functions
    """

    def test_create_audience(self):
        """
        Test creating a new audience
        """
        audience = Audience.create(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            name="SDK Test Audience",
            rule=dict(
                engager_type=1
                ),
            audience_type="ENGAGEMENT",
            description="SDK Test Audience Description",
            client=self.test_client
        )

        assert audience
        assert getattr(audience, '_id')
        assert getattr(audience, '_name') == "SDK Test Audience"
        assert getattr(audience, '_created_timestamp')

    def test_get_existing_audience(self):
        """
        Test if a Audience model/object is created successfully with correct audience_id
        """
        audience = Audience(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            audience_id=self.audience_utils.get_audience_id(),
            client=self.test_client
            )
        assert audience
        assert getattr(audience, '_id') == self.audience_utils.get_audience_id()

    def test_update_audience_with_kwargs(self):
        """
        Test if a given audience is updated successfully with passed in keyword arguments
        """
        new_name = "SDK Test Audience UPDATED"

        audience_response = Audience(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            audience_id=self.audience_utils.get_audience_id(),
            client=self.test_client
            )
        update_response = audience_response.update_fields(
            name=new_name,
            description="SDK Test Audience Description UPDATED",
            )

        assert update_response
        assert getattr(audience_response, '_name') == "SDK Test Audience UPDATED"
        assert getattr(audience_response, '_description') == "SDK Test Audience Description UPDATED"


class TestGetAllAudiences(BaseTestCase):
    """
    Test Get All Audiences class method
    """
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
