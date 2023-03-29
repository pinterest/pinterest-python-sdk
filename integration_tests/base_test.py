"""
Base test case for centralized the common code between different integration tests
"""

from unittest import TestCase
from pinterest.client import PinterestSDKClient

from integration_tests.utils.ads_utils import AdAccountUtils
from integration_tests.utils.ads_utils import CampaignUtils
from integration_tests.utils.ads_utils import AudienceUtils
from integration_tests.utils.ads_utils import CustomerListUtils
from integration_tests.utils.ads_utils import AdGroupUtils
from integration_tests.utils.ads_utils import ConversionTagUtils
from integration_tests.utils.ads_utils import AdUtils

from integration_tests.utils.organic_utils import BoardUtils
from integration_tests.utils.organic_utils import PinUtils


class BaseTestCase(TestCase):
    """
    Base test case for centralized the common code between different integration tests
    """
    # pylint: disable=too-many-instance-attributes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_client = None
        self._ad_account_utils = None
        self._campaign_utils = None
        self._customer_list_utils = None
        self._audience_utils = None
        self._ad_group_utils = None
        self._ads_utils = None
        self._conversion_tag_utils = None
        self._ad_utils = None
        self._test_customer_list_utils = None
        self._board_utils = None
        self._pin_utils = None

    @property
    def test_client(self):
        """Default pinterest sdk client"""
        if not self._test_client:
            self._test_client = PinterestSDKClient.create_default_client()
        return self._test_client

    @property
    def ad_account_utils(self):
        """Ad account util object"""
        if not self._ad_account_utils:
            self._ad_account_utils = AdAccountUtils()
        return self._ad_account_utils

    @property
    def campaign_utils(self):
        """Campaign utils util object"""
        if not self._campaign_utils:
            self._campaign_utils = CampaignUtils()
        return self._campaign_utils

    @property
    def customer_list_utils(self):
        """Customer list utils util object"""
        if not self._customer_list_utils:
            self._customer_list_utils = CustomerListUtils()
        return self._customer_list_utils

    @property
    def audience_utils(self):
        """Audience utils util object"""
        if not self._audience_utils:
            self._audience_utils = AudienceUtils()
        return self._audience_utils

    @property
    def ad_group_utils(self):
        """Ad group utils util object"""
        if not self._ad_group_utils:
            self._ad_group_utils = AdGroupUtils()
        return self._ad_group_utils

    @property
    def ad_utils(self):
        """Ads utils util object"""
        if not self._ad_utils:
            self._ad_utils = AdUtils()
        return self._ad_utils

    @property
    def conversion_tag_utils(self):
        """Conversion Tag util object"""
        if not self._conversion_tag_utils:
            self._conversion_tag_utils = ConversionTagUtils()
        return self._conversion_tag_utils

    @property
    def board_utils(self):
        """Board utils util object"""
        if not self._board_utils:
            self._board_utils = BoardUtils()
        return self._board_utils

    @property
    def pin_utils(self):
        """Pin utils util object"""
        if not self._pin_utils:
            self._pin_utils = PinUtils()
        return self._pin_utils
