"""Example code to create a Pinterest campaign."""

from pinterest.ads.campaigns import Campaign

campaign = Campaign.create(
  ad_account_id="12345",
  name="SDK Test Campaign",
  objective_type="AWARENESS",
  daily_spend_cap=10,
)

print('New campaign created: ', campaign)
