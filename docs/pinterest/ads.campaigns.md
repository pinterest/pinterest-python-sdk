<!-- markdownlint-disable -->

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ads.campaigns`
Campaign Class for Pinterest Python SDK 



---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Campaign`
Campaign model used to view, create, update its attributes and list its different entities. 

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    ad_account_id: 'str',
    campaign_id: 'str',
    client: 'PinterestSDKClient' = None,
    **kwargs
) → None
```

Initialize a Campaign object. 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  Campaign's Ad Account ID. 
 - <b>`campaign_id`</b> (str):  Campaign ID, must be associated with the Ad Account ID provided in the path. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Uses the default client, if not provided. 


---

#### <kbd>property</kbd> ad_account_id





---

#### <kbd>property</kbd> created_time





---

#### <kbd>property</kbd> daily_spend_cap





---

#### <kbd>property</kbd> end_time





---

#### <kbd>property</kbd> id





---

#### <kbd>property</kbd> is_campaign_budget_optimization





---

#### <kbd>property</kbd> is_flexible_daily_budgets





---

#### <kbd>property</kbd> lifetime_spend_cap





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> objective_type





---

#### <kbd>property</kbd> order_line_id





---

#### <kbd>property</kbd> start_time





---

#### <kbd>property</kbd> status





---

#### <kbd>property</kbd> tracking_urls





---

#### <kbd>property</kbd> type





---

#### <kbd>property</kbd> updated_time







---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L463"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `activate`

```python
activate() → bool
```

Activate a paused or archived campaign 



**Returns:**
 
 - <b>`bool`</b>:  If campaign status was successfully changed to 'ACTIVE' 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L472"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `archive`

```python
archive() → bool
```

Archive an active or paused campaign 



**Returns:**
 
 - <b>`bool`</b>:  If campaign status was successfully changed to 'ARCHIVED' 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L152"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create`

```python
create(
    ad_account_id: 'str',
    name: 'str',
    objective_type: 'str',
    status: 'str' = 'ACTIVE',
    lifetime_spend_cap: 'int' = None,
    daily_spend_cap: 'int' = None,
    order_line_id: 'int' = None,
    tracking_urls: 'str' = None,
    start_time: 'int' = None,
    end_time: 'int' = None,
    is_campaign_budget_optimization: 'bool' = False,
    is_flexible_daily_budgets: 'bool' = False,
    default_ad_group_budget_in_micro_currency: 'int' = None,
    is_automated_campaign: 'bool' = False,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → Campaign
```

Create a new campaign. Every campaign has its own campaign_id        and houses one or more ad groups, which contain one or more ads. 

For more,        see <a href="https://help.pinterest.com/en/business/article/set-up-your-campaign/"> Set up your campaign</a>. <p/> 

<strong>Note:</strong> 


- The values for        'lifetime_spend_cap' and 'daily_spend_cap' are microcurrency amounts based        on the currency field set in the advertiser's profile. (e.g. USD) <p/> 

<p>Microcurrency is used to track very small transactions, based on the currency         set in the advertiser’s profile.</p> 

<p>A microcurrency unit is 10^(-6)         of the standard unit of currency selected in the advertiser’s profile.</p> 

<p><strong>Equivalency equations</strong>, using dollars as an example currency:</p> 

<ul> 

<li>$1 = 1,000,000 microdollars</li> 

<li>1 microdollar = $0.000001</li> 

</ul> 

<p><strong>To convert between currency and microcurrency</strong>,        using dollars as an example currency:</p> 

<ul> 

<li>To convert dollars        to microdollars, mutiply dollars by 1,000,000</li> 

<li>To convert microdollars        to dollars, divide microdollars by 1,000,000</li> 

</ul> 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  Campaign's Ad Account ID. 
 - <b>`name`</b> (str):  Campaign name. 
 - <b>`objective_type`</b> (ObjectiveType):  Campaign objective type. Enum: `"AWARENESS"`, `"CONSIDERATION"`,  `"VIDEO_VIEW"`, `"WEB_CONVERSION"`, `"CATALOG_SALES"`, `"WEB_SESSIONS"` 
 - <b>`status`</b> (str, optional):  _description_. Defaults to 'ACTIVE'. 
 - <b>`lifetime_spend_cap`</b> (int, optional):  Campaign total spending cap. Defaults to None. 
 - <b>`daily_spend_cap`</b> (int, optional):  Campaign daily spending cap. Defaults to None. 
 - <b>`order_line_id`</b> (int, optional):  Order line ID that appears on the invoice.  Defaults to None. 
 - <b>`tracking_urls`</b> (str, optional):  Third-party tracking URLs.<br> Python <dict> with the format: 
 - <b>`{"<a href="https`</b>: //developers.pinterest.com/docs/redoc/#section/Tracking-URL-event">Tracking 
 - <b>`event enum</a>"`</b>: [URL string array],...}<br> For example: {"impression": 
 - <b>`["URL1", "URL2"], "click"`</b>:  ["URL1", "URL2", "URL3"]}.<br>Up to three tracking URLs are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. Pass in an empty object - {} - to remove tracking URLs.<br><br> For more 
 - <b>`information, see                         <a href="https`</b>: //help.pinterest.com/en/business/article/third-party-and-dynamic-tracking" target="_blank">Third-party and dynamic tracking</a>. Defaults to None. 
 - <b>`start_time`</b> (int, optional):  Campaign start time. Unix timestamp in seconds. Only used  for Campaign Budget Optimization (CBO) campaigns. Defaults to None. 
 - <b>`end_time`</b> (int, optional):  Campaign end time. Unix timestamp in seconds. Only used for  Campaign Budget Optimization (CBO) campaigns. Defaults to None. 
 - <b>`is_campaign_budget_optimization`</b> (bool, optional):  Determines if a campaign automatically  generate ad-group level budgets given a campaign budget to maximize  campaign outcome. When transitioning from non-cbo to cbo, all  previous child ad group budget will be cleared. Defaults to False. 
 - <b>`is_flexible_daily_budgets`</b> (bool, optional):  Determines if a campaign has flexible  daily budgets setup. Defaults to False. 
 - <b>`default_ad_group_budget_in_micro_currency`</b> (int, optional):  When transitioning from  campaign budget optimization to non-campaign budget optimization,  the default_ad_group_budget_in_micro_currency will propagate to  each child ad groups daily budget. Unit is micro currency  of the associated advertiser account. Defaults to None. 
 - <b>`is_automated_campaign`</b> (bool, optional):  Specifies whether the campaign was created  in the automated campaign flow. Defaults to False. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object, uses the default client, if not provided. 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`Campaign`</b>:  Campaign Object 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L295"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get_all`

```python
get_all(
    ad_account_id: 'str',
    campaign_ids: 'list[str]' = None,
    entity_statuses: 'list[str]' = None,
    page_size: 'int' = None,
    order: 'str' = 'ASCENDING',
    bookmark: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → tuple[list[Campaign], Bookmark]
```

Get a list of the campaigns in the AdAccount, filtered by the specified arguments 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  Campaign's Ad Account ID. 
 - <b>`campaign_ids`</b> (list[str], optional):  List of Campaign Ids to use to filter the results. Defaults to None. 
 - <b>`entity_statuses`</b> (list[str], optional):  Possible Entity Statuses "ACTIVE", "PAUSED" or "ARCHIVED". Defaults  to None. 
 - <b>`page_size`</b> (int[1..100], optional):  Maximum number of items to include in a single page of the response.  See documentation on Pagination for more information. Defaults to None which will  return default page size campaigns. 
 - <b>`order`</b> (str, optional):  The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.  Note that higher-value IDs are associated with more-recently added items. Defaults to  "ASCENDING". 
 - <b>`bookmark`</b> (str, optional):  Cursor used to fetch the next page of items. Defaults to None. 
 - <b>`client`</b> (PinterestSDKClient):  PinterestSDKClient Object 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`list[Campaign]`</b>:  List of Campaign Objects 
 - <b>`Bookmark`</b>:  Bookmark for pagination if present, else None. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L417"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_daily_budget`

```python
get_daily_budget() → float
```

Get the current daily spend cap budget of the campaign. 



**Returns:**
 
 - <b>`float`</b>:  Current daily spend cap budget 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L408"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_lifetime_budget`

```python
get_lifetime_budget() → float
```

Get the current life time spend cap budget of the campaign. 



**Returns:**
 
 - <b>`float`</b>:  Current life time spend cap budget 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L507"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_ad_groups`

```python
list_ad_groups(
    page_size: 'int' = 25,
    order: 'str' = 'ASCENDING',
    bookmark: 'str' = None,
    entity_statuses: 'list[str]' = None,
    **kwargs
) → tuple(list[AdGroup], Bookmark)
```

List ad groups directed related to campaign. This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please pass async_req=True 



**Args:**
 
 - <b>`page_size`</b> (int, optional):  _description_. Defaults to None. 
 - <b>`order`</b> (str, optional):  _description_. Defaults to "ASCENDING". 
 - <b>`bookmark`</b> (str, optional):  _description_. Defaults to None. 
 - <b>`entity_statuses`</b> (str, optional):  _description_. Defaults to None. 

**Returns:**
 
 - <b>`tuple[list[AdGroup], Bookmark]`</b>:  _description_ 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L454"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `pause`

```python
pause() → bool
```

Pause an active or archived campaign 



**Returns:**
 
 - <b>`bool`</b>:  If campaign status was successfully changed to 'PAUSED' 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L384"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_daily_budget`

```python
set_daily_budget(new_spend_cap: 'int') → bool
```

Set new daily spend cap budget for the campaign. 



**Args:**
 
 - <b>`new_spend_cap`</b> (int):  The new campaign daily spending cap. 



**Returns:**
 
 - <b>`bool`</b>:  If the daily budget was changed successfully 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L360"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_lifetime_budget`

```python
set_lifetime_budget(new_spend_cap: 'int') → bool
```

Set new life time spend cap budget for the campaign. 



**Args:**
 
 - <b>`new_spend_cap`</b> (int):  The new campaign total spending cap. 



**Returns:**
 
 - <b>`bool`</b>:  If the lifetime budget was changed successfully 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/campaigns.py#L481"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_fields`

```python
update_fields(**kwargs) → bool
```

Update the campaign fields using any attributes. 

Keyword Args:  Any valid campaign fields with valid values 



**Returns:**
 
 - <b>`bool`</b>:  If campaign fields were successfully updated 


