"""
Provide helper and utility functions for Integration Testing
"""

from pinterest.client import PinterestSDKClient
from pinterest.ads.ads import Ad
from pinterest.ads.ad_accounts import AdAccount
from pinterest.ads.ad_groups import AdGroup
from pinterest.ads.audiences import Audience
from pinterest.ads.customer_lists import CustomerList
from pinterest.ads.campaigns import Campaign
from pinterest.ads.keywords import Keyword
from pinterest.ads.conversion_tags import ConversionTag


from integration_tests.config import DEFAULT_PIN_ID, OWNER_USER_ID, DEFAULT_AD_ACCOUNT_ID


def _merge_default_params_with_params(default_params, params):
    if not params:
        return default_params

    for field, new_value in params.items():
        default_params[field] = new_value

    return default_params


def _get_client(client: PinterestSDKClient = None):
    return client or PinterestSDKClient.create_default_client()


class AdAccountUtils:
    def __init__(self, client=None):
        self.test_client = _get_client(client)
        self.ad_account = AdAccount.create(
            client=self.test_client,
            country="US",
            name="SDK Test Ad Account",
            owner_user_id=OWNER_USER_ID,
        )
        self.ad_account_id = self.ad_account._id

    def get_ad_account(self):
        return self.ad_account

    def get_ad_account_id(self):
        return self.ad_account_id

    def get_default_ad_account(self):
        return AdAccount(ad_account_id=DEFAULT_AD_ACCOUNT_ID, client=self.test_client)

    def get_default_ad_account_id(self):
        return DEFAULT_AD_ACCOUNT_ID

    def get_default_params(self):
        return dict(
            client=self.test_client,
            country="US",
            name="SDK Test Ad Account",
            owner_user_id=OWNER_USER_ID,
        )
    
    def create_new_ad_account(self):
        return AdAccount.create(**self.get_default_params())

class AudienceUtils:
    def __init__(self, client=None):
        self.test_client = _get_client(client)
        self.audience = Audience.create(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            name="SDK Test Audience",
            rule=dict(
                engager_type=1
                ),
            audience_type="ENGAGEMENT",
            description="SDK Test Audience Description",
            client=self.test_client
        )
        self.audience_id = self.audience._id

    def get_audience(self):
        return self.audience

    def get_audience_id(self):
        return self.audience_id

    def get_default_params(self):
        return dict(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            name="SDK Test Audience",
            rule=dict(
                engager_type=1
                ),
            audience_type="ENGAGEMENT",
            description="SDK Test Audience Description",
            client=self.test_client
        )

    def create_new_audience(self):
        return Audience.create(**self.get_default_params())

class CampaignUtils:
    def __init__(self, client=None):
        self.test_client = _get_client(client)
        self.campaign = Campaign.create(
            client=self.test_client,
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            name="SDK Test Campaign",
            objective_type="AWARENESS",
            daily_spend_cap=10000000,
        )
        self.campaign_id = self.campaign._id

    def get_campaign(self):
        return self.campaign

    def get_campaign_id(self):
        return self.campaign_id

    def get_default_params(self):
        return dict(
            client=self.test_client,
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            name="SDK Test Campaign",
            objective_type="AWARENESS",
            daily_spend_cap=10000000,
        )

    def create_new_campaign(self, **kwargs):
        return Campaign.create(**_merge_default_params_with_params(self.get_default_params(), kwargs))


class AdGroupUtils:
    def __init__(self, client=None):
        self.test_client = _get_client(client)

        self.campaign = CampaignUtils().get_campaign()
        self.ad_group = AdGroup.create(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            campaign_id=getattr(self.campaign, "_id"),
            billable_event="IMPRESSION",
            client=self.test_client,
            name="SDK_INTEGRATION_TEST_ADGROUP",
            auto_targeting_enabled=False,
            bid_in_micro_currency=10000000,
            targeting_spec=dict(
                age_bucket=["35-44"],
                location=["US"],
            )
        )
        self.ad_group_id = self.ad_group._id

    def get_ad_group(self):
        return self.ad_group

    def get_ad_group_id(self):
        return self.ad_group_id

    def get_default_params(self):
        return dict(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            campaign_id=getattr(self.campaign, "_id"),
            billable_event="IMPRESSION",
            client=self.test_client,
            name="SDK_INTEGRATION_TEST_ADGROUP",
            auto_targeting_enabled=False,
            bid_in_micro_currency=10000000,
            targeting_spec=dict(
                age_bucket=["35-44"],
                location=["US"],
            )
        )

    def create_new_ad_group(self, **kwargs):
        return AdGroup.create(**_merge_default_params_with_params(self.get_default_params(), kwargs))


class CustomerListUtils:
    def __init__(self, client=None):
        self.test_client = _get_client(client)
        self.customer_list = CustomerList.create(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            name="SDK Test Customer List",
            records="test@pinterest.com",
            list_type="EMAIL",
            client=self.test_client,
        )
        self.customer_list_id = self.customer_list._id

    def get_customer_list(self):
        return self.customer_list

    def get_customer_list_id(self):
        return self.customer_list_id

    def get_default_params(self):
        return dict(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            name="SDK Test Customer List",
            records="test@pinterest.com",
            list_type="EMAIL",
            client=self.test_client
        )

    def create_new_customer_list(self, **kwargs):
        if not kwargs:
            return CustomerList.create(**self.get_default_params())

        kwargs = self.get_default_params()
        for field, new_value in kwargs.items():
            kwargs[field] = new_value
        return CustomerList.create(**kwargs)

class AdUtils:
    def __init__(self, client=None):
        self.test_client = _get_client(client)
        self.ad_group = AdGroupUtils().get_ad_group()

        self.ad = Ad.create(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_group_id=getattr(self.ad_group, "_id"),
            creative_type="REGULAR",
            pin_id=DEFAULT_PIN_ID,
            name="Test_create_ad",
            status="ACTIVE",
            is_pin_deleted=False,
            is_removable=False,
            client=self.test_client,
        )
        self.ad_id = getattr(self.ad, "_id")

    def get_ad(self):
        return self.ad

    def get_ad_id(self):
        return self.ad_id

    def get_default_params(self):
        return dict(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            ad_group_id=getattr(self.ad_group, "_id"),
            creative_type="REGULAR",
            pin_id=DEFAULT_PIN_ID,
            name="Test_create_ad",
            status="ACTIVE",
            is_pin_deleted=False,
            is_removable=False,
            client=self.test_client,
        )

    def create_new_ad(self):
        return Ad.create(**self.get_default_params())

class KeywordUtils:
    def __init__(self, client=None):
        self.test_client = _get_client(client)
        self.ad_group = AdGroupUtils().get_ad_group()

        self.keyword = Keyword.create(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            parent_id=getattr(self.ad_group, "_id"),
            value="string",
            match_type="BROAD",
            bid=1000,
        )
        self.keyword_id = getattr(self.keyword, "_id")

    def get_keyword(self):
        return self.keyword

    def get_keyword_id(self):
        return self.keyword_id

    def get_default_params(self):
        return dict(
            ad_account_id=DEFAULT_AD_ACCOUNT_ID,
            parent_id=getattr(self.ad_group, "_id"),
            value="string",
            match_type="BROAD",
            bid=1000,    
        )

    def create_new_keyword(self):
        return Keyword.create(**self.get_default_params())

class ConversionTagUtils:
    def __init__(self, client=None):
        self.test_client = _get_client(client)

        self.conversion_tag = ConversionTag.create(
            ad_account_id = DEFAULT_AD_ACCOUNT_ID,
            name = "SDK_TEST_CONVERSION_TAG"
        )
        self.conversion_tag_id = getattr(self.conversion_tag, "_id")

    def get_conversion_tag(self):
        return self.conversion_tag

    def get_conversion_tag_id(self):
        return self.conversion_tag_id

    def get_default_params(self):
        return dict(
            ad_account_id = DEFAULT_AD_ACCOUNT_ID,
            name = "SDK_TEST_CONVERSION_TAG",
        )

    def create_new_conversion_tag(self, **kwargs):
        if not kwargs:
            return ConversionTag.create(**self.get_default_params())
        return ConversionTag.create(**kwargs)
