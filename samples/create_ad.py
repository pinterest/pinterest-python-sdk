"""Example code to create a Pinterest Ad."""

from pinterest.ads.ads import Ad

AD_ACCOUNT_ID = "12345"
AD_GROUP_ID = "333333"
PIN_ID = "44444"

ad = Ad.create(
  ad_account_id=AD_ACCOUNT_ID,
  ad_group_id=AD_GROUP_ID,
  creative_type="REGULAR",
  pin_id=PIN_ID,
  name="My SDK AD",
  status="ACTIVE",
)

print('New ad created: ', ad)
