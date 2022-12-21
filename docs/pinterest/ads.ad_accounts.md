<!-- markdownlint-disable -->

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/pinterest/ads/ad_accounts.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ads.ad_accounts`
AdAccount Class for Pinterest Python SDK 



---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/pinterest/ads/ad_accounts.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AdAccount`
Ad Account model used to create, update its attributes and list its different entities. 

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/pinterest/ads/ad_accounts.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(ad_account_id: 'str', client=None, **kwargs) → None
```

Initialize an object of an AdAccount. 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  Unique identifier of an ad account. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Defaults to `default_api_client`. 


---

#### <kbd>property</kbd> country





---

#### <kbd>property</kbd> currency





---

#### <kbd>property</kbd> id





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> owner





---

#### <kbd>property</kbd> permissions







---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/pinterest/ads/ad_accounts.py#L89"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create`

```python
create(
    name: 'str',
    owner_user_id: 'str',
    country: 'str',
    client: 'PinterestSDKClient' = None,
    **kwargs
) → AdAccount
```

Create a new ad account. Different ad accounts can support different currencies, payment methods, etc. An ad account is needed to create campaigns, ad groups, and ads; other accounts (your employees or partners) can be assigned business access and appropriate roles to access an ad account. <p/> You can set up up to 50 ad accounts per user. (The user must have a business account to            create an ad account.)<p/> For more, see <a class="reference external" href=            "https://help.pinterest.com/en/business/article/create-an-advertiser-account">                Create an advertiser account</a>. 



**Args:**
 
 - <b>`name`</b> (str):  Ad Account name 
 - <b>`owner_user_id`</b> (str):  Ad Account's owning user ID 
 - <b>`country`</b> (str):  Country ID from ISO 3166-1 alpha-2. Example: "US" or "RU". 
 - <b>`client`</b> (PinterestSDKClient):  PinterestSDKClient Object 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`AdAccount`</b>:  AdAccount Object 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/pinterest/ads/ad_accounts.py#L181"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_audiences`

```python
list_audiences(
    entity_statuses: 'list[str]' = None,
    page_size: 'int' = None,
    order: 'str' = 'ASCENDING',
    bookmark: 'str' = None,
    **kwargs
) → tuple[list[Audience], Bookmark]
```

Get a list of the audiences in the AdAccount, filtered by the specified arguments 



**Args:**
 
 - <b>`entity_statuses`</b> (list[str], optional):  Possible Entity Statuses "ACTIVE", "PAUSED" or "ARCHIVED". Defaults  to None. 
 - <b>`page_size`</b> (int[1..100], optional):  Maximum number of items to include in a single page of the response.  See documentation on Pagination for more information. Defaults to None  which will return default number of audiences. 
 - <b>`order`</b> (str, optional):  The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.  Note that higher-value IDs are associated with more-recently added items. Defaults to  "ASCENDING". 
 - <b>`bookmark`</b> (str, optional):  Cursor used to fetch the next page of items. Defaults to None. 



**Returns:**
 
 - <b>`list[Audience]`</b>:  List of Audience Objects 
 - <b>`Bookmark`</b>:  Bookmark for pagination if present, else None. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/pinterest/ads/ad_accounts.py#L134"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_campaigns`

```python
list_campaigns(
    campaign_ids: 'list[str]' = None,
    entity_statuses: 'list[str]' = None,
    page_size: 'int' = None,
    order: 'str' = 'ASCENDING',
    bookmark: 'str' = None,
    **kwargs
) → tuple[list[Campaign], Bookmark]
```

Get a list of the campaigns in the specified <code>ad_account_id</code>, filtered by the specified options. 
- The token's user_account must either be the Owner of the specified ad account, or have one of the necessary            roles granted to them via                <a href="https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts">                    Business Access</a>: Admin, Analyst, Campaign Manager. 



**Args:**
 
 - <b>`campaign_ids`</b> (list[str], optional):  List of Campaign Ids to use to filter the results. Defaults to None. 
 - <b>`entity_statuses`</b> (list[str], optional):  Possible Entity Statuses "ACTIVE", "PAUSED" or "ARCHIVED". Defaults  to None. 
 - <b>`page_size`</b> (int[1..100], optional):  Maximum number of items to include in a single page of the response.  See documentation on Pagination for more information. Defaults to None  which will return default number of campaigns. 
 - <b>`order`</b> (str, optional):  The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.  Note that higher-value IDs are associated with more-recently added items. Defaults to  "ASCENDING". 
 - <b>`bookmark`</b> (str, optional):  Cursor used to fetch the next page of items. Defaults to None. 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`list[Campaign]`</b>:  List of Campaign Objects 
 - <b>`Bookmark`</b>:  Bookmark for pagination if present, else None. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/pinterest/ads/ad_accounts.py#L218"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_customer_lists`

```python
list_customer_lists(
    page_size: 'int' = None,
    order: 'str' = None,
    bookmark: 'str' = None,
    **kwargs
) → tuple[list[CustomerList], Bookmark]
```

Get a list of customer lists in the AdAccount, filtered by the specified arguments 



**Args:**
 
 - <b>`page_size`</b> (int[1..100], optional):  Maximum number of items to include in a single page of the response.  See documentation on Pagination for more information. Defaults to None  which will return all campaigns. 
 - <b>`order`</b> (str, optional):  The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.  Note that higher-value IDs are associated with more-recently added items. Defaults to  "ASCENDING". 
 - <b>`bookmark`</b> (str, optional):  Cursor used to fetch the next page of items. Defaults to None. 



**Returns:**
 
 - <b>`list[CustomerList]`</b>:  List of Audience Objects 
 - <b>`Bookmark`</b>:  Bookmark for pagination if present, else None. 


