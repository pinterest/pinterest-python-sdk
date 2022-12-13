"""Example code to create a Pinterest Ad."""
import os

from pinterest.config import PINTEREST_API_URI, PINTEREST_STATE
from pinterest.client import PinterestSDKClient
from pinterest.ads.ad_accounts import AdAccount

DEFAULT_AD_ACCOUNT_ID = os.environ.get('PINTEREST_DEFAULT_AD_ACCOUNT_ID')


def main():
    client = PinterestSDKClient.create_default_client()
    assert client is not None
    assert PINTEREST_API_URI is not None
    assert PINTEREST_STATE == 'package_test'
    campaigns = AdAccount(ad_account_id=DEFAULT_AD_ACCOUNT_ID).list_campaigns()
    assert len(campaigns) > 0


if __name__ == "__main__":
    main()
