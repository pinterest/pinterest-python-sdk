"""Example code to create a Pinterest Customer List."""

from pinterest.ads.customer_lists import CustomerList

AD_ACCOUNT_ID = "12345"

customer_list = CustomerList.create(
  ad_account_id=AD_ACCOUNT_ID,
  name="SDK Test Customer List",
  records="test@pinterest.com,test@example.com",
  list_type="EMAIL",
)

print("New customer list: ", customer_list)
