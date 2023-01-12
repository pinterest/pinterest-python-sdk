<!-- markdownlint-disable -->

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/audiences.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ads.audiences`
High level module class for Audience object 



---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/audiences.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Audience`
High level model class to manage audiences for an AdAccount 

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/audiences.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(ad_account_id, audience_id, client=None, **kwargs)
```






---

#### <kbd>property</kbd> ad_account_id





---

#### <kbd>property</kbd> audience_type





---

#### <kbd>property</kbd> created_timestamp





---

#### <kbd>property</kbd> description





---

#### <kbd>property</kbd> id





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> rule





---

#### <kbd>property</kbd> size





---

#### <kbd>property</kbd> status





---

#### <kbd>property</kbd> type





---

#### <kbd>property</kbd> updated_timestamp







---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/audiences.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create`

```python
create(
    ad_account_id: 'str',
    name: 'str',
    rule: 'dict',
    audience_type: 'str',
    description: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → Audience
```

Create an audience you can use in targeting for specific ad groups. Targeting combines customer information with the ways users interact with Pinterest to help you reach specific groups of users; you can include or exclude specific audience_ids when you create an ad group. 

For more information, visit https://help.pinterest.com/en/business/article/audience-targeting. 



**Args:**
 
 - <b>`client`</b> (PinterestSDKClient):  PinterestSDKClient Object 
 - <b>`ad_account_id`</b> (str):  Audience's Advertiser or Ad Account ID. 
 - <b>`name`</b> (str):  Audience name. 
 - <b>`rule`</b> (dict):  python <dict> defining targeted audience users. The keys and value formats:  rule_example_format = { 
 - <b>`country`</b> (str):  Valid countries include: "US", "CA", and "GB" 
 - <b>`customer_list_id`</b> (str):  Customer list ID. For CUSTOMER_LIST `audience_type` 
 - <b>`engagement_domain`</b> (list[str]):  The audience account's verified domain. **Required** for ENGAGEMENT `audience_type` 
 - <b>`engagement_type`</b> (str):  Engagement type enum. Optional for ENGAGEMENT `audience_type`. Supported values are `click`, `save`, `closeup`, `comment` and `like`. All engagements are included if this field is not set. 
 - <b>`event`</b> (str):  A Pinterest tag event. Optional for VISITOR `audience_type`. Possible values are `pagevisit`, `signup`, `checkout`, `viewcategory`, `search`, `addtocart`, `watchvideo`, `lead`, and `custom`. This field also accepts a partner-defined Pinterest tag event. 
 - <b>`event_data`</b>:  **NOT YET SUPPORTED** 
 - <b>`percentage`</b> (int):  Percentage should be 1-10. The targeted audience should be this % size across Pinterest. 
 - <b>`pin_id`</b> (list[str]):  IDs of engaged organic pins. Optional for ENGAGEMENT `audience_type`. For example, "pin_id:": ["34567"]. 
 - <b>`prefill`</b> (bool):  Optional for VISITOR `audience_type`. If `true`, the specified rule on existing engagement data is applied to pre-populate the audience. If `false`, the audience is empty at creation time. The default is `true`. 
 - <b>`retention_days`</b> (int):  Number of days a Pinterest user remains in the audience. Optional for ENGAGEMENT and VISITOR `audience_type`. Accepted range is 1-540. Defaults to 180 if not specified. 
 - <b>`seed_id`</b> ([str]):  Audience ID(s). For ACTALIKE `audience_type`. 
 - <b>`url`</b> ([str]):  Optional for ENGAGEMENT or VISITOR `audience_type`. For ENGAGEMENT, it is the engaged pin's URL. For VISITOR, you can use it as a string or a {operator: value} object for filtering visitors based on conversion tag event URLs. Supported operators are [ =, !=, contains, not_contains].<br>Example 1:  "url": "http://www.myonlinestore123.com/view_item/shoe"<br>Example 2: "url": {"contains": "view_item_shoe"}. 
 - <b>`visitor_source_id`</b> (str):  The conversion tag ID, or the Pinterest tag ID, that you use on your website. For VISITOR `audience_type`. 
 - <b>`event_source`</b> (dict):  Optional for VISITOR. You can use it as a {'=': [value]}. Supported values are: web, mobile, offline. 
 - <b>`ingestion_source`</b> (dict):  Optional for VISITOR. You can use it as a {'=': [value]}. Supported values are: tag, mmp, file_upload, conversions_api. 
 - <b>`engager_type`</b> (int):  Optional for ENGAGEMENT. Engager type value should be 1-2. 
 - <b>`campaign_id`</b> (list[str]):  Campaign ID for engagement audience filter. 
 - <b>`ad_id`</b> (list[str]):  Ad ID for engagement audience filter. 
 - <b>`objective_type`</b> (list[str]):  Objective for engagement audience filter. } 
 - <b>`audience_type`</b> (str):  Enum ("CUSTOMER_LIST" "VISITOR" "ENGAGEMENT" "ACTALIKE") 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`Audience`</b>:  Audience Object 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/audiences.py#L190"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get_all`

```python
get_all(
    ad_account_id: 'str',
    entity_statuses: 'list[str]' = None,
    page_size: 'int' = None,
    order: 'str' = 'ASCENDING',
    bookmark: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → tuple[list[Audience], Bookmark]
```

Get a list of the audiences in the AdAccount, filtered by the specified arguments 



**Args:**
 
 - <b>`client`</b> (PinterestSDKClient):  PinterestSDKClient Object 
 - <b>`ad_account_id`</b> (str):  Audience's Advertiser ID. 
 - <b>`entity_statuses`</b> (list[str], optional):  Possible Entity Statuses "ACTIVE", "PAUSED" or "ARCHIVED". Defaults  to None. 
 - <b>`page_size`</b> (int[1..100], optional):  Maximum number of items to include in a single page of the response.  See documentation on Pagination for more information. Defaults to None which will  return default number of audiences. 
 - <b>`order`</b> (str, optional):  The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.  Note that higher-value IDs are associated with more-recently added items. Defaults to  "ASCENDING". 
 - <b>`bookmark`</b> (str, optional):  Cursor used to fetch the next page of items. Defaults to None. 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`list[Audience]`</b>:  List of Audience Objects 
 - <b>`Bookmark`</b>:  Bookmark for pagination if present, else None. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/audiences.py#L252"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_fields`

```python
update_fields(**kwargs)
```

Update audience fields 

Keyword Args:  Any valid audience fields with valid values 


