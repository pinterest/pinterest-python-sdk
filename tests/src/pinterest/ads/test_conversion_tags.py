'''
Test Conversion Tag Model
'''
from unittest import TestCase
from unittest.mock import patch

from pinterest.ads.conversion_tags import ConversionTag

from openapi_generated.pinterest_client.model.entity_status import EntityStatus
from openapi_generated.pinterest_client.model.conversion_tag_type import ConversionTagType
from openapi_generated.pinterest_client.model.conversion_tag_configs import ConversionTagConfigs
from openapi_generated.pinterest_client.model.conversion_tag_response import ConversionTagResponse
from openapi_generated.pinterest_client.model.conversion_event_response import ConversionEventResponse
from openapi_generated.pinterest_client.model.enhanced_match_status_type import EnhancedMatchStatusType
from openapi_generated.pinterest_client.model.conversion_tag_list_response import ConversionTagListResponse
from openapi_generated.pinterest_client.model.conversion_tags_ocpm_eligible_response import ConversionTagsOcpmEligibleResponse


class TestConversionTagCreate(TestCase):
    """
    Test Conversion Tag create successfully
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_conversion_tag_id = "111111111111"
        self.test_ad_account_id = "777777777777"

    @patch('pinterest.ads.conversion_tags.ConversionTagsApi.conversion_tags_get')
    def test_create_conversion_tag_using_existing_conversion_tag(self, get_mock):
        """
        Test if Conversion Tag can be created successfully from a ad_account_id and
        conversion_tag_id
        """
        test_configs = ConversionTagConfigs(
            aem_enabled = True,
            md_frequency = float(0.6),
            aem_fnln_enabled = True,
            aem_ph_enabled = True,
            aem_ge_enabled = True,
            aem_db_enabled = True,
            aem_loc_enabled = True,
        )
        get_mock.return_value = ConversionTagResponse(
            ad_account_id = self.test_ad_account_id,
            code_snippet = "<script type=text/javascript> [...]",
            enhanced_match_status = EnhancedMatchStatusType("VALIDATION_COMPLETE"),
            id = self.test_conversion_tag_id,
            last_fired_time_ms = float(1599030000000),
            name = "ACME Checkout Test Tag",
            status = EntityStatus("ACTIVE"),
            version = "3",
            configs = test_configs
        )

        conversion_tag = ConversionTag(
            ad_account_id = self.test_ad_account_id,
            conversion_tag_id = self.test_conversion_tag_id,
        )

        assert conversion_tag
        assert conversion_tag.ad_account_id == self.test_ad_account_id
        assert conversion_tag.code_snippet == "<script type=text/javascript> [...]"
        assert conversion_tag.enhanced_match_status == EnhancedMatchStatusType("VALIDATION_COMPLETE")
        assert conversion_tag.id == self.test_conversion_tag_id
        assert conversion_tag.last_fired_time_ms == float(1599030000000)
        assert conversion_tag.name == "ACME Checkout Test Tag"
        assert conversion_tag.status == EntityStatus("ACTIVE")
        assert conversion_tag.version == "3"
        assert conversion_tag.configs == test_configs

    @patch('pinterest.ads.conversion_tags.ConversionTagsApi.conversion_tags_create')
    @patch('pinterest.ads.conversion_tags.ConversionTagsApi.conversion_tags_get')
    def test_create_conversion_tag_new_model(self, get_mock, create_mock):
        """
        Test if Conversion Tag model can be created successfully from account_id and new conversion tag
        information
        """
        test_configs = ConversionTagConfigs(
            aem_enabled = True,
            md_frequency = float(0.6),
            aem_fnln_enabled = True,
            aem_ph_enabled = True,
            aem_ge_enabled = True,
            aem_db_enabled = True,
            aem_loc_enabled = True,
        )
        create_mock.__name__ = "conversion_tags_create"
        create_mock.return_value = ConversionTagResponse(
            ad_account_id = self.test_ad_account_id,
            code_snippet = "<script type=text/javascript> [...]",
            enhanced_match_status = EnhancedMatchStatusType("VALIDATION_COMPLETE"),
            id = self.test_conversion_tag_id,
            last_fired_time_ms = float(1599030000000),
            name = "ACME Checkout Test Tag",
            status = EntityStatus("ACTIVE"),
            version = "3",
            configs = test_configs
        )

        get_mock.return_value = ConversionTagResponse(
            ad_account_id = self.test_ad_account_id,
            code_snippet = "<script type=text/javascript> [...]",
            enhanced_match_status = EnhancedMatchStatusType("VALIDATION_COMPLETE"),
            id = self.test_conversion_tag_id,
            last_fired_time_ms = float(1599030000000),
            name = "ACME Checkout Test Tag",
            status = EntityStatus("ACTIVE"),
            version = "3",
            configs = test_configs
        )

        conversion_tag = ConversionTag.create(
            ad_account_id = self.test_ad_account_id,
            name = "ACME Checkout Test Tag",
            aem_enabled = True,
            md_frequency = float(0.6),
            aem_fnln_enabled = True,
            aem_ph_enabled = True,
            aem_ge_enabled = True,
            aem_db_enabled = True,
            aem_loc_enabled = True,
        )

        assert conversion_tag
        assert conversion_tag.ad_account_id == self.test_ad_account_id
        assert conversion_tag.code_snippet == "<script type=text/javascript> [...]"
        assert conversion_tag.enhanced_match_status == EnhancedMatchStatusType("VALIDATION_COMPLETE")
        assert conversion_tag.id == self.test_conversion_tag_id
        assert conversion_tag.last_fired_time_ms == float(1599030000000)
        assert conversion_tag.name == "ACME Checkout Test Tag"
        assert conversion_tag.status == EntityStatus("ACTIVE")
        assert conversion_tag.version == "3"
        assert conversion_tag.configs == test_configs


    @patch('pinterest.ads.conversion_tags.ConversionTagsApi.conversion_tags_get')
    @patch('pinterest.ads.conversion_tags.ConversionTagsApi.conversion_tags_list')
    def test_get_list_conversion_tag(self, list_mock, get_mock):
        """
        Test get list of Converion Tags with a given ad_account
        """
        list_mock.__name__ = "conversion_tags_list"
        get_mock.__name = "conversion_tags_get"
        
        test_configs = ConversionTagConfigs(
            aem_enabled = True,
            md_frequency = float(0.6),
            aem_fnln_enabled = True,
            aem_ph_enabled = True,
            aem_ge_enabled = True,
            aem_db_enabled = True,
            aem_loc_enabled = True,
        )
        list_mock.return_value = ConversionTagListResponse(
            items = [
                ConversionTagResponse(
                    ad_account_id = self.test_ad_account_id,
                    code_snippet = "<script type=text/javascript> [...]",
                    enhanced_match_status = EnhancedMatchStatusType("VALIDATION_COMPLETE"),
                    id = self.test_conversion_tag_id,
                    last_fired_time_ms = float(1599030000000),
                    name = "ACME Checkout Test Tag",
                    status = EntityStatus("ACTIVE"),
                    version = "3",
                    configs = test_configs
                )
            ]
        )

        conversion_tags = ConversionTag.get_all(
            ad_account_id = self.test_ad_account_id,
        )
        conversion_tag = conversion_tags[0]

        get_mock.assert_not_called()

        assert conversion_tags
        assert len(conversion_tags) == 1
        assert conversion_tag
        assert conversion_tag.ad_account_id == self.test_ad_account_id
        assert conversion_tag.code_snippet == "<script type=text/javascript> [...]"
        assert conversion_tag.enhanced_match_status == EnhancedMatchStatusType("VALIDATION_COMPLETE")
        assert conversion_tag.id == self.test_conversion_tag_id
        assert conversion_tag.last_fired_time_ms == float(1599030000000)
        assert conversion_tag.name == "ACME Checkout Test Tag"
        assert conversion_tag.status == EntityStatus("ACTIVE")
        assert conversion_tag.version == "3"
        assert conversion_tag.configs == test_configs

    @patch('pinterest.ads.conversion_tags.ConversionTagsApi.page_visit_conversion_tags_get')
    def test_get_page_visit_conversion_tag_event(self, get_page_visit_mock):
        """
        Test Get page visit conversion tag events for an ad account
        """
        get_page_visit_mock.__name__ = "page_visit_conversion_tags_get"
        get_page_visit_mock.return_value = {
            "items" : [
                {
                    "conversion_event": "PAGE_LOAD",
                    "conversion_tag_id": self.test_conversion_tag_id,
                    "ad_account_id": self.test_ad_account_id,
                    "created_time": 1564768710,
                }
            ],
            "bookmark": "test_bookmark",
        }

        conversion_tag_events, bookmark = ConversionTag.get_page_visit_conversion_tag_events(
            ad_account_id = self.test_ad_account_id,
            page_size = 1,
        )

        assert bookmark.get_bookmark_token() == "test_bookmark"

        assert conversion_tag_events
        assert len(conversion_tag_events) == 1
        assert type(conversion_tag_events[0]) == ConversionEventResponse
        assert conversion_tag_events[0].ad_account_id == self.test_ad_account_id
        assert conversion_tag_events[0].conversion_tag_id == self.test_conversion_tag_id

    @patch('pinterest.ads.conversion_tags.ConversionTagsApi.ocpm_eligible_conversion_tags_get')
    def test_get_ocpm_eligible_conversion_tag_events(self, get_mock):
        """
        Test Get OCPM eligible conversion tag events for an ad account
        """
        get_mock.__name__ = "ocpm_eligible_conversion_tags_get"
        param = {
            "123": [
                    ConversionEventResponse(
                        conversion_event = ConversionTagType("PAGE_LOAD"),
                        conversion_tag_id = self.test_conversion_tag_id,
                        ad_account_id = self.test_ad_account_id,
                        created_time = 1564768710,
                    ),
                    ConversionEventResponse(
                        conversion_event = ConversionTagType("CHECKOUT"),
                        conversion_tag_id = self.test_conversion_tag_id,
                        ad_account_id = self.test_ad_account_id,
                        created_time = 1564768723,
                    ),
                ]
        }
        get_mock.return_value = ConversionTagsOcpmEligibleResponse(**param)

        property_name, conversion_tag_events = ConversionTag.get_ocpm_eligible_conversion_tag_events(
            ad_account_id = self.test_ad_account_id
        )

        assert property_name == "123"
        assert conversion_tag_events
        assert len(conversion_tag_events) == 2

        assert type(conversion_tag_events[0]) == ConversionEventResponse
        assert conversion_tag_events[0].ad_account_id == self.test_ad_account_id
        assert conversion_tag_events[0].conversion_tag_id == self.test_conversion_tag_id
        assert conversion_tag_events[0].conversion_event == ConversionTagType("PAGE_LOAD")

        assert type(conversion_tag_events[1]) == ConversionEventResponse
        assert conversion_tag_events[1].ad_account_id == self.test_ad_account_id
        assert conversion_tag_events[1].conversion_tag_id == self.test_conversion_tag_id
        assert conversion_tag_events[1].conversion_event == ConversionTagType("CHECKOUT")
