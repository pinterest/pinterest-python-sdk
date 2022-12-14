"""
Test Pinterest Base Model
"""
from parameterized import parameterized

from pinterest.ads.campaigns import Campaign
from pinterest.organic.boards import Board

from integration_tests.base_test import BaseTestCase
from integration_tests.config import DEFAULT_AD_ACCOUNT_ID
from integration_tests.config import DEFAULT_BOARD_ID

class TestPinterestBaseModel(BaseTestCase):
    def test_error_message_for_accessing_non_existant_attribute(self):
        """
        Test getting a Campaign and accessing an attribute that does not exist
        """
        existing_campaign_id = self.campaign_utils.get_campaign_id()
        campaign = Campaign(
            client=self.test_client,
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            campaign_id=existing_campaign_id,
        )

        assert campaign
        with self.assertRaises(AttributeError):
            campaign.non_existing_property

    def test_equality_of_campaign_models(self):
        """
        Test if two campaign model instances of same campaign id are equal to each other
        """
        existing_campaign_id = self.campaign_utils.get_campaign_id()
        campaign_v1_0 = Campaign(
            client=self.test_client,
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            campaign_id=existing_campaign_id,
        )
        campaign_v1_1 = Campaign(
            client=self.test_client,
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            campaign_id=existing_campaign_id,
        )
        campaign_v2_0 = self.campaign_utils.create_new_campaign()

        assert campaign_v1_0 == campaign_v1_1
        assert campaign_v1_1 != campaign_v2_0

    def test_set_board_attributes_failure(self):
        """
        Test setting a Board attribute failure
        """
        board = Board(
            board_id=DEFAULT_BOARD_ID,
            client=self.test_client,
        )

        assert board
        with self.assertRaises(AttributeError):
            board.name = "FAILURE_BOARD_NAME"

class TestModelAttributes(BaseTestCase):
    @parameterized.expand(
        [
            # Ads Models
            ("ad_account",),
            ("campaign"),
            ("ad_group"),
            ("ad"),
            ("customer_list"),
            ("audience"),
        ]
    )
    def test_ads_model_attributes_match_properties(self, model_name):
        model_creation_util = f"{model_name}_utils"
        model_creation_util_fn = f"create_new_{model_name}"
        model = getattr(getattr(self, model_creation_util), model_creation_util_fn)()
        api_spec_attribute_set = set(model._model_attribute_types.keys())
        sdk_model_property_set = set(model._property_dict.keys())

        assert api_spec_attribute_set == sdk_model_property_set

    @parameterized.expand(
        [
            # Organic Models
            ("board"),
            ("pin"),
        ]
    )
    def test_organic_model_attributes_match_properties(self, model_name):
        model_creation_util = f"{model_name}_utils"
        model_creation_util_fn = f"create_new_{model_name}"
        model_deletion_util_fn = f"delete_{model_name}"

        model = getattr(getattr(self, model_creation_util), model_creation_util_fn)()

        getattr(getattr(self, model_creation_util), model_deletion_util_fn)(model.id)

        api_spec_attribute_set = set(model._model_attribute_types.keys())
        sdk_model_property_set = set(model._property_dict.keys())

        assert api_spec_attribute_set == sdk_model_property_set
