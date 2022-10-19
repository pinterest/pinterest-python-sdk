"""Example code to create a Pinterest ad group."""

from pinterest.ads.ad_groups import AdGroup

AD_ACCOUNT_ID = "12345"
CAMPAIGN_ID = "22222"

ad_group = AdGroup.create(
  ad_account_id=AD_ACCOUNT_ID,
  campaign_id=CAMPAIGN_ID,
  billable_event="IMPRESSION",
  name="My first adgroup from SDK",
)

print('New ad group created: ', ad_group)
