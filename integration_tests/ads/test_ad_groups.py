'''
Test AdGroup Model
'''

from integration_tests.base_test import BaseTestCase
from integration_tests.config import DEFAULT_AD_ACCOUNT_ID

from pinterest.ads.ad_groups import AdGroup


class TestCreateAdGroup(BaseTestCase):
    '''
    Test creating AdGroup Model
    '''

    def test_create_ad_group_success(self):
        '''
        Test creating AdGroup successfully
        '''
        ad_group = AdGroup.create(
            client=self.test_client,
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            campaign_id=getattr(self.ad_group_utils.campaign, "_id"),
            billable_event="IMPRESSION",
            name="SDK_INTEGRATION_TEST_ADGROUP",
            auto_targeting_enabled=False,
            bid_in_micro_currency=10000000,
            targeting_spec=dict(
                age_bucket=["35-44"],
                location=["US"],
            )
        )

        assert ad_group
        assert getattr(ad_group, "_id")
        assert getattr(ad_group, "_name") == "SDK_INTEGRATION_TEST_ADGROUP"
        assert getattr(ad_group, "_ad_account_id") == DEFAULT_AD_ACCOUNT_ID
        assert getattr(ad_group, "_campaign_id") == getattr(self.ad_group_utils.campaign, "_id")

    def test_get_existing_ad_group(self):
        '''
        Test if a AdGroup model/object is created successfully with correct audience_id
        '''
        ad_group = AdGroup(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_group_id=self.ad_group_utils.get_ad_group_id(),
            client=self.test_client,
        )

        assert ad_group
        assert getattr(ad_group, "_id") == self.ad_group_utils.get_ad_group_id()
        assert getattr(ad_group, "_campaign_id") == getattr(self.ad_group_utils.campaign, "_id")


class TestUpdateAdGroup(BaseTestCase):
    """
    Test update on AdGroup Model
    """
    def test_update_success(self):
        """
        Test update successfully
        """
        ad_group = AdGroup(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_group_id=self.ad_group_utils.get_ad_group_id(),
            client=self.test_client,
        )

        new_name = "SDK_AD_GROUP_NEW_NAME"
        new_spec = {
            "age_bucket":["35-44"],
            "location": ["US"],
        }

        ad_group.update_fields(
            name=new_name,
            targeting_spec=new_spec
        )

        assert ad_group
        assert getattr(ad_group, "_name") == new_name
        assert str(getattr(ad_group,"_targeting_spec")).lower() == str(new_spec).lower()

    def test_update_fail_with_invalid_tracking_urls(self):
        """
        Test update with invalid tracking url
        """
        ad_group = AdGroup(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_group_id=self.ad_group_utils.get_ad_group_id(),
            client=self.test_client,
        )

        new_tracking_url = {
            "impression": ["URL1","URL2"],
            "click": ["URL1","URL2"],
            "engagement": ["URL1","URL2"],
            "buyable_button": ["URL1","URL2"],
            "audience_verification": ["URL1","URL2"],
        }

        update_argument = dict(
            tracking_urls=new_tracking_url
        )

        with self.assertRaises(AssertionError):
            ad_group.update_fields(**update_argument)


class TestGetListAdGroup(BaseTestCase):
    """
    Test get list on AdGroup Model
    """
    def test_get_list_success(self):
        """
        Test get list successfully
        """
        NUMBER_OF_NEW_AD_GROUP = 5

        new_ad_group_ids = list(
            getattr(self.ad_group_utils.create_new_ad_group(), "_id") for _ in range(NUMBER_OF_NEW_AD_GROUP)
        )
        ad_groups, _ = AdGroup.get_all(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_group_ids=new_ad_group_ids,
        )

        assert len(ad_groups) == NUMBER_OF_NEW_AD_GROUP

    def test_get_list_with_campaign_ids_success(self):
        """
        Test get list with campaign id
        """
        old_ad_groups, _ = AdGroup.get_all(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            campaign_ids=[getattr(self.ad_group_utils.campaign, "_id")]
        )

        new_campaign = self.campaign_utils.create_new_campaign()
        AdGroup.create(
            client=self.test_client,
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            campaign_id=getattr(new_campaign, "_id"),
            billable_event="IMPRESSION",
            name="SDK_INTEGRATION_TEST_ADGROUP",
            auto_targeting_enabled=False,
            bid_in_micro_currency=10000000,
            targeting_spec=dict(
                age_bucket=["35-44"],
                location=["US"],
            )
        )

        new_ad_groups = AdGroup.get_all(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            campaign_ids=[getattr(self.ad_group_utils.campaign, "_id"), getattr(new_campaign, "_id")]
        )

        assert len(new_ad_groups) == len(old_ad_groups) + 1

    def test_get_list_invalid_id_fail(self):
        """
        Test get list with invalid id
        """
        INVALID_AD_GROUP_ID = "1111111"
        get_list_dict = dict(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_group_ids=[INVALID_AD_GROUP_ID],
        )

        with self.assertRaises(TypeError):
            AdGroup.get_all(get_list_dict)


class TestListAds(BaseTestCase):
    """
    Test get list on AdGroup Model
    """
    def test_list_ads_success(self):
        """
        Test if all ads can be listed from an Ad Group
        """
        NUMBER_OF_NEW_ADS = 4
        new_ad_ids = []
        for _ in range(NUMBER_OF_NEW_ADS):
            new_ad_ids.append(getattr(self.ad_utils.create_new_ad(),"_id"))

        ad_group = AdGroup(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_group_id=getattr(self.ad_utils.ad_group, "_id"),
            client=self.test_client
        )
        ads, _ = ad_group.list_ads(
            ad_ids=new_ad_ids,
        )

        assert ads
        assert len(ads) == len(new_ad_ids)
        for ad in ads:
            assert getattr(ad, "_id") in new_ad_ids

    def test_enable_auto_targeting(self):
        """
        Test enable auto targeting
        """
        ad_group_0 = self.ad_group_utils.create_new_ad_group(
            auto_targeting_enabled=False,
        )
        self.assertFalse(getattr(ad_group_0, "_auto_targeting_enabled"))
        ad_group_0.enable_auto_targeting()

        ad_group_1 = AdGroup(
            ad_account_id=getattr(ad_group_0, "_ad_account_id"),
            ad_group_id=getattr(ad_group_0, "_id")
        )
        self.assertTrue(getattr(ad_group_1, "_auto_targeting_enabled"))

    def test_disable_auto_targeting(self):
        """
        Test disable auto targeting
        """
        ad_group_0 = self.ad_group_utils.create_new_ad_group(
            auto_targeting_enabled=True,
        )
        self.assertTrue(getattr(ad_group_0, "_auto_targeting_enabled"))
        ad_group_0.disable_auto_targeting()

        ad_group_1 = AdGroup(
            ad_account_id=getattr(ad_group_0, "_ad_account_id"),
            ad_group_id=getattr(ad_group_0, "_id")
        )
        self.assertFalse(getattr(ad_group_1, "_auto_targeting_enabled"))
