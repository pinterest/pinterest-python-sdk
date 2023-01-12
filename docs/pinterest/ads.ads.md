<!-- markdownlint-disable -->

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/ads.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ads.ads`
Ads high level model 



---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/ads.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Ad`
Ad model used to view, create, update its attributes 

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/ads.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    ad_account_id: 'str',
    ad_id: 'str',
    client: 'PinterestSDKClient' = None,
    **kwargs
) → None
```

Initialize an Ad object. 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  Ad's Ad Account ID. 
 - <b>`ad_id`</b> (str):  Ad ID, must be associated with the Ad Account ID provided in the path. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Defaults to default_api_client. 


---

#### <kbd>property</kbd> ad_account_id





---

#### <kbd>property</kbd> ad_group_id





---

#### <kbd>property</kbd> android_deep_link





---

#### <kbd>property</kbd> campaign_id





---

#### <kbd>property</kbd> carousel_android_deep_links





---

#### <kbd>property</kbd> carousel_destination_urls





---

#### <kbd>property</kbd> carousel_ios_deep_links





---

#### <kbd>property</kbd> click_tracking_url





---

#### <kbd>property</kbd> collection_items_destination_url_template





---

#### <kbd>property</kbd> created_time





---

#### <kbd>property</kbd> creative_type





---

#### <kbd>property</kbd> destination_url





---

#### <kbd>property</kbd> id





---

#### <kbd>property</kbd> ios_deep_link





---

#### <kbd>property</kbd> is_pin_deleted





---

#### <kbd>property</kbd> is_removable





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> pin_id





---

#### <kbd>property</kbd> rejected_reasons





---

#### <kbd>property</kbd> rejection_labels





---

#### <kbd>property</kbd> review_status





---

#### <kbd>property</kbd> status





---

#### <kbd>property</kbd> summary_status





---

#### <kbd>property</kbd> tracking_urls





---

#### <kbd>property</kbd> type





---

#### <kbd>property</kbd> updated_time





---

#### <kbd>property</kbd> view_tracking_url







---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/ads.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create`

```python
create(
    ad_account_id: 'str',
    ad_group_id: 'str',
    creative_type: 'str',
    pin_id: 'str',
    is_pin_deleted: 'bool' = False,
    is_removable: 'bool' = True,
    status: 'str' = 'ACTIVE',
    android_deep_link: 'str' = None,
    carousel_android_deep_links: 'list[str]' = None,
    carousel_destination_urls: 'list[str]' = None,
    carousel_ios_deep_links: 'list[str]' = None,
    click_tracking_url: 'str' = None,
    destination_url: 'str' = None,
    ios_deep_link: 'str' = None,
    name: 'str' = None,
    tracking_urls: 'dict' = None,
    view_tracking_url: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → Ad
```

Create a new ad. Request must contain ad_group_id, creative_type, and the source Pin pin_id. 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  Campaign's Ad Account ID. 
 - <b>`ad_group_id`</b> (str):  ID of the ad group that contains the ad. 
 - <b>`creative_type`</b> (str):  Ad creative type enum. Enum: `"REGULAR"` `"VIDEO"` `"SHOPPING"`  `"CAROUSEL"` `"MAX_VIDEO"` `"SHOP_THE_PIN"` `"IDEA"` 
 - <b>`pin_id`</b> (str):  ID of the pin used to make the ad. 
 - <b>`status`</b> (str):  Entity status of the ad. Enum: `"ACTIVE"` `"PAUSED"` `"ARCHIVED"` 
 - <b>`is_pin_deleted`</b> (bool):  Is original pin deleted? 
 - <b>`is_removable`</b> (bool):  Is pin repinnable? 
 - <b>`android_deep_link`</b> (str, optional):  Deep link URL for Android devices. Not currently  available. Using this field will generate an error. Defaults to None. 
 - <b>`carousel_android_deep_links`</b> (list[str], optional):  List of deep links for the carousel pin on  Android. Defaults to None. 
 - <b>`carousel_destination_urls`</b> (list[str], optional):  List of destination URLs for the carousel  pin to promote. Defaults to None. 
 - <b>`carousel_ios_deep_links`</b> (list[str], optional):  List of deep links for the carousel pin on iOS.  Defaults to None. 
 - <b>`click_tracking_url`</b> (str, optional):  Tracking url for the ad clicks. Defaults to None. 
 - <b>`destination_url`</b> (str, optional):  Destination URL. Defaults to None. 
 - <b>`ios_deep_link`</b> (str, optional):  Deep link URL for iOS devices. Not currently available. Using  this field will generate an error.Defaults to None. 
 - <b>`name`</b> (str, optional):  Name of the ad - 255 chars max.  Defaults to None. 
 - <b>`tracking_urls`</b> (dict, optional):  Third-party tracking URLs.<br> Python <dict> with the format: 
 - <b>`{"<a href="https`</b>: //developers.pinterest.com/docs/redoc/#section/Tracking-URL-event">Tracking 
 - <b>`event enum</a>"`</b>: [URL string array],...}<br> For example: {"impression": 
 - <b>`["URL1", "URL2"], "click"`</b>:  ["URL1", "URL2", "URL3"]}.<br>Up to three tracking URLs are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. Pass in an empty object - {} - to remove tracking URLs.<br><br> For more 
 - <b>`information, see                         <a href="https`</b>: //help.pinterest.com/en/business/article/third-party-and-dynamic-tracking" target="_blank">Third-party and dynamic tracking</a>. Defaults to None. 
 - <b>`view_tracking_url`</b> (str, optional):  Tracking URL for ad impressions. Defaults to None. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Defaults to default_api_client. 



**Returns:**
 
 - <b>`Ad`</b>:  The newly created Ad. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/ads.py#L315"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get_all`

```python
get_all(
    ad_account_id: 'str',
    campaign_ids: 'list[str]' = None,
    ad_group_ids: 'list[str]' = None,
    ad_ids: 'list[str]' = None,
    entity_statuses: 'list[str]' = None,
    page_size: 'int' = None,
    order: 'str' = 'ASCENDING',
    bookmark: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → tuple[list[Ad], Bookmark]
```

List ads that meet the filters provided: 
  - Listed campaign ids or ad group ids or ad ids 
  - Listed entity statuses <p/> If no filter is provided, all ads in the ad account are returned. 



**NOTE:**

> Provide only campaign_id or ad_group_id or ad_id. Do not provide more than one type. Review status is provided for each ad; if review_status is REJECTED, the rejected_reasons field will contain additional information. For more, see https://policy.pinterest.com/en/advertising-guidelines Pinterest advertising standards. 
>

**Args:**
 
 - <b>`ad_account_id`</b> (str):  Ad Account ID 
 - <b>`campaign_ids`</b> (list[str], optional):  List of Campaign IDs to use to filter the results 
 - <b>`ad_group_ids`</b> (list[str], optional):  List of Ad Group IDs to use to filter the results 
 - <b>`ad_ids`</b> (list[str], optional):  List of Ad IDs to use to filter the results 
 - <b>`entity_statuses`</b> (list[str], optional):  Possible Entity Statuses "ACTIVE", "PAUSED" or "ARCHIVED". Defaults  to None. 
 - <b>`page_size`</b> (int[1..100], optional):  Maximum number of items to include in a single page of the response.  See documentation on Pagination for more information. Defaults to None which will  return all campaigns. 
 - <b>`order`</b> (str, optional):  The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.  Note that higher-value IDs are associated with more-recently added items. Defaults to  "ASCENDING". 
 - <b>`bookmark`</b> (str, optional):  Cursor used to fetch the next page of items. Defaults to None. 
 - <b>`client`</b> (ApiClient):  ApiClient Object 



**Returns:**
 
 - <b>`list[Ad]`</b>:  List of Ad Objects 
 - <b>`Bookmark`</b>:  Bookmark for pagination if present, else None. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/ads.py#L394"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_fields`

```python
update_fields(**kwargs) → bool
```

Update Ad fields suing any arguments 



**Returns:**
 
 - <b>`bool`</b>:  If Ad fields were updated successfully 


