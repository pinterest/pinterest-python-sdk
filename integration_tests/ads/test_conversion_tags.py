"""
Test Conversion Tag Model
"""

from integration_tests.base_test import BaseTestCase
from integration_tests.config import DEFAULT_AD_ACCOUNT_ID

from pinterest.ads.conversion_tags import ConversionTag

class TestCreateConversionTag(BaseTestCase):
    """
    Test creating Conversion Tag
    """

    def test_create_conversion_tag_success(self):
        """
        Test creating a new Conversion Tag successfully
        """
        conversion_tag = ConversionTag.create(
            ad_account_id = DEFAULT_AD_ACCOUNT_ID,
            name = "Test Conversion Tag",
            aem_enabled = None,
            md_frequency = None,
            aem_fnln_enabled = None,
            aem_ph_enabled = None,
            aem_ge_enabled = None,
            aem_db_enabled = None,
            aem_loc_enabled = None,
        )

        assert conversion_tag
        assert getattr(conversion_tag, "_id")
        assert getattr(conversion_tag, "_name") == "Test Conversion Tag"
        assert getattr(conversion_tag.configs, "aem_enabled") == False

    def test_create_conversion_tag_with_configs_success(self):
        """
        Test creating a new Conversion Tag successfully
        """
        conversion_tag = ConversionTag.create(
            ad_account_id = DEFAULT_AD_ACCOUNT_ID,
            name = "Test Conversion Tag",
            aem_enabled = True,
            md_frequency = 1.2,
            aem_fnln_enabled = None,
            aem_ph_enabled = None,
            aem_ge_enabled = None,
            aem_db_enabled = None,
            aem_loc_enabled = None,
        )

        assert conversion_tag
        assert getattr(conversion_tag, "_id")
        assert getattr(conversion_tag, "_name") == "Test Conversion Tag"
        assert getattr(conversion_tag.configs, "aem_enabled") == True
        assert getattr(conversion_tag.configs, "md_frequency") == 1.2

class TestGetConversionTag(BaseTestCase):
    """
    Test get Conversion Tag
    """

    def test_get_conversion_tag_success(self):
        """
        Test get conversion tag from existing conversion tag
        """
        exiting_conversion_tag_id = self.conversion_tag_utils.get_conversion_tag_id()
        conversion_tag = ConversionTag(
            client = self.test_client,
            ad_account_id = DEFAULT_AD_ACCOUNT_ID,
            conversion_tag_id = exiting_conversion_tag_id,
            )

        assert conversion_tag
        assert getattr(conversion_tag, "_id")
        assert getattr(conversion_tag, "_name") == getattr(self.conversion_tag_utils.get_conversion_tag(), "_name")

class TestGetListConversionTag(BaseTestCase):
    """
    Test get list of ConversionTags
    """
    def test_get_list_success(self):
        """
        Test get list successfully
        """
        # Create new account so the integration test does not get slow as number of conversion
        # tags increasing while testing
        ad_account_id = getattr(self.ad_account_utils.create_new_ad_account(), "_id")

        NUMBER_OF_NEW_CONVERSION_TAG = 3
        for _ in range(NUMBER_OF_NEW_CONVERSION_TAG):
            self.conversion_tag_utils.create_new_conversion_tag(
                name = "SDK_TEST_CONVERSION_TAG",
                ad_account_id = ad_account_id,
            )

        conversion_tags = ConversionTag.get_all(ad_account_id = ad_account_id)

        assert len(conversion_tags) == NUMBER_OF_NEW_CONVERSION_TAG
        for conversion_tag in conversion_tags:
            assert conversion_tag.name == "SDK_TEST_CONVERSION_TAG"
            assert conversion_tag.ad_account_id == ad_account_id


class TestGetPageVsitConversionTag(BaseTestCase):
    """
    Test get page visit conversion tag events
    """
    def test_get_page_visit_success(self):
        """
        Test get page visit converion tag events for an Ad Account
        """
        conversion_tag_events, bookmark = ConversionTag.get_page_visit_conversion_tag_events(
            ad_account_id = DEFAULT_AD_ACCOUNT_ID
        )

        assert not conversion_tag_events
        assert not bookmark

class TestGetOcpmEligibleConversionTag(BaseTestCase):
    """
    Test get ocpm eligible conversion tag events
    """
    def test_get_ocpm_eligible_conversion_tags(self):
        """
        Test get ocpm eligible conversion tag events for an Ad Account
        """
        property, conversion_tag_events = ConversionTag.get_ocpm_eligible_conversion_tag_events(
            ad_account_id = DEFAULT_AD_ACCOUNT_ID
        )

        assert not property
        assert not conversion_tag_events
