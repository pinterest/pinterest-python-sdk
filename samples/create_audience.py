"""Example code to create a Pinterest Audience."""

from pinterest.ads.audiences import Audience

AD_ACCOUNT_ID = "549764334122"

audience = Audience.create(
  ad_account_id=AD_ACCOUNT_ID,
  name="SDK Test Audience",
  rule=dict(
    engager_type=1
  ),
  audience_type="ENGAGEMENT",
  description="SDK Test Audience Description",
)

print("New audience: ", audience)
