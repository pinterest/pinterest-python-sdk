<!-- markdownlint-disable -->

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/ad_groups.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ads.ad_groups`
High level module class for AdGroup object 



---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/ad_groups.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AdGroup`
AdGroup model used to view, create, update its attributes and list its different entities. 

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/ad_groups.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(ad_account_id: 'str', ad_group_id: 'str', client=None, **kwargs) → None
```

Initialize an AdGroup object. 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  AdGroup's Ad Account ID. 
 - <b>`ad_group_id`</b> (str):  AdGroup ID, must be associated with the Ad Account ID provided in the path. 
 - <b>`client`</b> (_type_, optional):  PinterestSDKClient Object. Defaults to default_api_client. 


---

#### <kbd>property</kbd> ad_account_id





---

#### <kbd>property</kbd> auto_targeting_enabled





---

#### <kbd>property</kbd> bid_in_micro_currency





---

#### <kbd>property</kbd> bid_strategy_type





---

#### <kbd>property</kbd> billable_event





---

#### <kbd>property</kbd> budget_in_micro_currency





---

#### <kbd>property</kbd> budget_type





---

#### <kbd>property</kbd> campaign_id





---

#### <kbd>property</kbd> conversion_learning_mode_type





---

#### <kbd>property</kbd> created_time





---

#### <kbd>property</kbd> dca_assets





---

#### <kbd>property</kbd> end_time





---

#### <kbd>property</kbd> feed_profile_id





---

#### <kbd>property</kbd> id





---

#### <kbd>property</kbd> lifetime_frequency_cap





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> pacing_delivery_type





---

#### <kbd>property</kbd> placement_group





---

#### <kbd>property</kbd> start_time





---

#### <kbd>property</kbd> status





---

#### <kbd>property</kbd> summary_status





---

#### <kbd>property</kbd> targeting_spec





---

#### <kbd>property</kbd> tracking_urls





---

#### <kbd>property</kbd> type





---

#### <kbd>property</kbd> updated_time







---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/ad_groups.py#L205"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create`

```python
create(
    ad_account_id: 'str',
    name: 'str',
    campaign_id: 'str',
    billable_event: 'str',
    budget_in_micro_currency: 'int' = None,
    bid_in_micro_currency: 'int' = None,
    start_time: 'int' = None,
    end_time: 'int' = None,
    tracking_url: 'str' = None,
    auto_targeting_enabled: 'bool' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → AdGroup
```

Create a new ad group. All ads in a given ad group will have the same budget, bid, run dates, targeting, and placement (search, browse, other). For more information, <a href="https://help.pinterest.com/ en/business/article/campaign-structure" target="_blank"> click here</a>.</p><strong>Note:</strong> 


- 'bid_in_micro_currency' 

and 'budget_in_micro_currency' should be expressed in microcurrency amounts based on the currency field set in the advertiser's profile.<p/> 

<p>Microcurrency is used to track very small transactions, based on the currency set in the advertiser’s profile.</p> 

<p>A microcurrency unit is 10^(-6) of the standard unit of currency selected in the advertiser’s profile.</p> 



<p><strong>Equivalency equations</strong>, using dollars as an example currency:</p> 



<ul> 

<li>$1 = 1,000,000 microdollars</li> 

<li>1 microdollar = $0.000001</li> 

</ul> 

<p><strong>To convert between currency and microcurrency</strong>, using dollars as an example currency:</p> 

<ul> 

<li>To convert dollars to microdollars, mutiply dollars by 1,000,000</li> 

<li>To convert microdollars to dollars, divide microdollars by 1,000,000</li> 

</ul> 


- Ad groups belong 

to ad campaigns. Some types of campaigns (e.g. budget optimization) have limits on the number of ad groups they can hold. If you exceed those limits, you will get an error message. 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  Campaign's Ad Account ID. 
 - <b>`name`</b> (str):  Ad Group name. 
 - <b>`campaign_id`</b> (str):  Campaign ID of the ad group. 
 - <b>`billable_event`</b> (str):  Ad group billable event type. 
 - <b>`Enum`</b>:  "CLICKTHROUGH" "IMPRESSION" "VIDEO_V_50_MRC" "BILLABLE_ENGAGEMENT" 
 - <b>`budget_in_micro_currency`</b> (int, optional):  Budget in micro currency. This field is **REQUIRED**  for non-CBO (campaign budget optimization) campaigns.  A CBO campaign automatically  generates ad group budgets from its campaign budget to maximize campaign  outcome. A CBO campaign is limited to 70 or less ad groups. Defaults to None. 
 - <b>`bid_in_micro_currency`</b> (int, optional):  Bid price in micro currency. This field is **REQUIRED** 
 - <b>`for the following campaign objective_type/billable_event combinations`</b>:  AWARENESS/IMPRESSION, CONSIDERATION/CLICKTHROUGH, CATALOG_SALES/CLICKTHROUGH, VIDEO_VIEW/VIDEO_V_50_MRC. Defaults to None. 
 - <b>`start_time`</b> (int, optional):  Campaign start time. Unix timestamp in seconds. Only used  for Campaign Budget Optimization (CBO) campaigns. Defaults to None. 
 - <b>`end_time`</b> (int, optional):  Campaign end time. Unix timestamp in seconds. Only used for  Campaign Budget Optimization (CBO) campaigns. Defaults to None. 
 - <b>`tracking_url`</b> (str, optional):  Third-party tracking URLs.<br> Python <dict> with the format: 
 - <b>`{"<a href="https`</b>: //developers.pinterest.com/docs/redoc/#section/Tracking-URL-event">Tracking 
 - <b>`event enum</a>"`</b>: [URL string array],...}<br> For example: {"impression": 
 - <b>`["URL1", "URL2"], "click"`</b>:  ["URL1", "URL2", "URL3"]}.<br>Up to three tracking URLs are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. Pass in an empty object - {} - to remove tracking URLs.<br><br> For more 
 - <b>`information, see                         <a href="https`</b>: //help.pinterest.com/en/business/article/third-party-and-dynamic-tracking" target="_blank">Third-party and dynamic tracking</a>. Defaults to None. 
 - <b>`auto_targeting_enabled`</b> (bool, optional):  Enable auto-targeting for ad group. Also known as 
 - <b>`<a href="https`</b>: //help.pinterest.com/en/business/article/expanded-targeting" target="_blank">"expanded targeting"</a>. Defaults to None. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Defaults to default_api_client. 



**Returns:**
 
 - <b>`AdGroup`</b>:  AdGroup Object 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/ad_groups.py#L471"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable_auto_targeting`

```python
disable_auto_targeting()
```

Disable auto-targeting for ad group. Also known as <a href='https://help.pinterest.com/en/business/article/expanded-targeting'>"expanded targeting"</a>. 



**Returns:**
 
 - <b>`bool`</b>:  true if ad group disable auto_targeting_enabled 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/ad_groups.py#L461"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `enable_auto_targeting`

```python
enable_auto_targeting()
```

Enable auto-targeting for ad group. Also known as <a href='https://help.pinterest.com/en/business/article/expanded-targeting'>"expanded targeting"</a>. 



**Returns:**
 
 - <b>`bool`</b>:  true if ad group enable auto_targeting_enabled 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/ad_groups.py#L362"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get_all`

```python
get_all(
    ad_account_id: 'str',
    campaign_ids: 'list[str]' = None,
    ad_group_ids: 'list[str]' = None,
    entity_statuses: 'list[str]' = None,
    page_size: 'int' = None,
    order: 'str' = 'ASCENDING',
    bookmark: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → tuple[list[AdGroup], Bookmark]
```

List ad groups based on provided campaign IDs or ad group IDs.(campaign_ids or ad_group_ids). <p/> <strong>Note:</strong><p/> Provide only campaign_id or ad_group_id. Do not provide both.  # noqa: E501 This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please pass async_req=True 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  _description_ 
 - <b>`campaign_ids`</b> (list[str], optional):  _description_. Defaults to None. 
 - <b>`ad_group_ids`</b> (list[str], optional):  _description_. Defaults to None. 
 - <b>`page_size`</b> (int, optional):  _description_. Defaults to None. 
 - <b>`order`</b> (str, optional):  _description_. Defaults to "ASCENDING". 
 - <b>`bookmark`</b> (str, optional):  _description_. Defaults to None. 
 - <b>`client`</b> (PinterestSDKClient, optional):  _description_. Defaults to default_api_client. 



**Returns:**
 
 - <b>`tuple[list[AdGroup], Bookmark]`</b>:  _description_ 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/ad_groups.py#L422"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_ads`

```python
list_ads(
    ad_ids: 'list[str]' = None,
    entity_statuses: 'list[str]' = None,
    page_size: 'int' = None,
    order: 'str' = 'ASCENDING',
    bookmark: 'str' = None,
    **kwargs
) → tuple[list[Ad], Bookmark]
```

Get list of ads under current AdGroup with specified arguments 



**Args:**
 
 - <b>`ad_ids`</b> (list[str], optional):  List of Ad IDs 
 - <b>`entity_statuses`</b> (list[str], optional):  Possible Entity Statuses "ACTIVE", "PAUSED" or "ARCHIVED". Defaults  to None. 
 - <b>`page_size`</b> (int[1..100], optional):  Maximum number of items to include in a single page of the response.  See documentation on Pagination for more information. Defaults to None which will  return all campaigns. 
 - <b>`order`</b> (str, optional):  The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.  Note that higher-value IDs are associated with more-recently added items. Defaults to  "ASCENDING". 
 - <b>`bookmark`</b> (str, optional):  Cursor used to fetch the next page of items. Defaults to None. 



**Returns:**
 
 - <b>`list[Ad]`</b>:  List of Ads 
 - <b>`Bookmark`</b>:  Bookmark object 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/ad_groups.py#L336"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_fields`

```python
update_fields(**kwargs) → bool
```

Update adgroup fields using any arguments 



**Returns:**
 
 - <b>`bool`</b>:  if adgroup fields were updated successfully 


