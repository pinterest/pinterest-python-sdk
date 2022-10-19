"""Example code to create a Pinterest Keyword."""

from pinterest.ads.keywords import Keyword

AD_ACCOUNT_ID = "12345"
AD_GROUP_ID = "56789"

keyword = Keyword.create(
  ad_account_id=AD_ACCOUNT_ID,
  parent_id=AD_GROUP_ID,
  value="baby shoes",
  match_type="BROAD",
  bid=1000,
)

print("New keyword: ", keyword)
