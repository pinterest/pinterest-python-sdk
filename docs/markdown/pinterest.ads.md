# pinterest.ads package

## Submodules

## pinterest.ads.ad_accounts module

AdAccount Class for Pinterest Python SDK


### _class_ pinterest.ads.ad_accounts.AdAccount(ad_account_id: str, client=None, \*\*kwargs)
Bases: `PinterestBaseModel`

Ad Account model used to create, update its attributes and list its different entities.


#### _classmethod_ create(name: str, owner_user_id: str, country: str, client: ~pinterest.client.PinterestSDKClient = <pinterest.client.PinterestSDKClient object>, \*\*kwargs)
Create a new ad account. Different ad accounts can support different currencies, payment methods, etc.
An ad account is needed to create campaigns, ad groups, and ads; other accounts (your employees or partners)
can be assigned business access and appropriate roles to access an ad account. <p/>
You can set up up to 50 ad accounts per user. (The user must have a business account to            create an ad account.)<p/>
For more, see <a class=”reference external” href=            “[https://help.pinterest.com/en/business/article/create-an-advertiser-account](https://help.pinterest.com/en/business/article/create-an-advertiser-account)”>                Create an advertiser account</a>.


* **Parameters**

    
    * **name** (*str*) – Ad Account name


    * **owner_user_id** (*str*) – Ad Account’s owning user ID


    * **country** (*str*) – Country ID from ISO 3166-1 alpha-2. Example: “US” or “RU”.


    * **client** ([*PinterestSDKClient*](pinterest.client.md#pinterest.client.PinterestSDKClient)) – PinterestSDKClient Object



* **Keyword Arguments**

    **endpoint.** (*Any valid keyword arguments** or **query parameters for*) – 



* **Returns**

    AdAccount Object



* **Return type**

    AdAccount



#### list_audiences(entity_statuses: Optional[list[str]] = None, page_size: Optional[int] = None, order: str = 'ASCENDING', bookmark: Optional[str] = None, \*\*kwargs)
Get a list of the audiences in the AdAccount, filtered by the specified arguments


* **Parameters**

    
    * **entity_statuses** (*list**[**str**]**, **optional*) – Possible Entity Statuses “ACTIVE”, “PAUSED” or “ARCHIVED”. Defaults
    to None.


    * **page_size** (*int**[**1..100**]**, **optional*) – Maximum number of items to include in a single page of the response.
    See documentation on Pagination for more information. Defaults to None
    which will return default number of audiences.


    * **order** (*str**, **optional*) – The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
    Note that higher-value IDs are associated with more-recently added items. Defaults to
    “ASCENDING”.


    * **bookmark** (*str**, **optional*) – Cursor used to fetch the next page of items. Defaults to None.



* **Returns**

    List of Audience Objects
    str: Bookmark for pagination if present, else None.



* **Return type**

    list[Audience]



#### list_campaigns(campaign_ids: Optional[list[str]] = None, entity_statuses: Optional[list[str]] = None, page_size: Optional[int] = None, order: str = 'ASCENDING', bookmark: Optional[str] = None, \*\*kwargs)
Get a list of the campaigns in the specified <code>ad_account_id</code>, filtered by the specified options.
- The token’s user_account must either be the Owner of the specified ad account, or have one of the necessary            roles granted to them via                <a href=”[https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts)”>                    Business Access</a>: Admin, Analyst, Campaign Manager.


* **Parameters**

    
    * **campaign_ids** (*list**[**str**]**, **optional*) – List of Campaign Ids to use to filter the results. Defaults to None.


    * **entity_statuses** (*list**[**str**]**, **optional*) – Possible Entity Statuses “ACTIVE”, “PAUSED” or “ARCHIVED”. Defaults
    to None.


    * **page_size** (*int**[**1..100**]**, **optional*) – Maximum number of items to include in a single page of the response.
    See documentation on Pagination for more information. Defaults to None
    which will return default number of campaigns.


    * **order** (*str**, **optional*) – The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
    Note that higher-value IDs are associated with more-recently added items. Defaults to
    “ASCENDING”.


    * **bookmark** (*str**, **optional*) – Cursor used to fetch the next page of items. Defaults to None.



* **Keyword Arguments**

    **endpoint.** (*Any valid keyword arguments** or **query parameters for*) – 



* **Returns**

    List of Campaign Objects
    str: Bookmark for pagination if present, else None.



* **Return type**

    list[Campaign]



#### list_customer_lists(page_size: Optional[int] = None, order: Optional[str] = None, bookmark: Optional[str] = None, \*\*kwargs)
Get a list of customer lists in the AdAccount, filtered by the specified arguments


* **Parameters**

    
    * **page_size** (*int**[**1..100**]**, **optional*) – Maximum number of items to include in a single page of the response.
    See documentation on Pagination for more information. Defaults to None
    which will return all campaigns.


    * **order** (*str**, **optional*) – The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
    Note that higher-value IDs are associated with more-recently added items. Defaults to
    “ASCENDING”.


    * **bookmark** (*str**, **optional*) – Cursor used to fetch the next page of items. Defaults to None.



* **Returns**

    List of Audience Objects
    str: Bookmark for pagination if present, else None.



* **Return type**

    list[CustomerList]


## pinterest.ads.ad_groups module

High level module class for AdGroup object


### _class_ pinterest.ads.ad_groups.AdGroup(ad_account_id: str, ad_group_id: str, client=None, \*\*kwargs)
Bases: `PinterestBaseModel`

AdGroup model used to view, create, update its attributes and list its different entities.


#### _classmethod_ create(ad_account_id: str, name: str, campaign_id: str, billable_event: str, budget_in_micro_currency: ~typing.Optional[int] = None, bid_in_micro_currency: ~typing.Optional[int] = None, start_time: ~typing.Optional[int] = None, end_time: ~typing.Optional[int] = None, tracking_url: ~typing.Optional[str] = None, auto_targeting_enabled: ~typing.Optional[bool] = None, client: ~pinterest.client.PinterestSDKClient = <pinterest.client.PinterestSDKClient object>, \*\*kwargs)
Create a new ad group. All ads in a given ad group will
have the same budget, bid, run dates, targeting, and placement (search,
browse, other). For more information, <a href=”[https://help.pinterest.com/](https://help.pinterest.com/)
en/business/article/campaign-structure”
target=”_blank”> click here</a>.</p><strong>Note:</strong>


* ‘bid_in_micro_currency’

and ‘budget_in_micro_currency’ should be expressed in microcurrency amounts
based on the currency field set in the advertiser’s profile.<p/>

<p>Microcurrency
is used to track very small transactions, based on the currency set in the
advertiser’s profile.</p>

<p>A microcurrency unit is 10^(-6) of the
standard unit of currency selected in the advertiser’s profile.</p>

<p><strong>Equivalency equations</strong>, using dollars as an example currency:</p>

<ul>

<li>$1 = 1,000,000 microdollars</li>

<li>1 microdollar = $0.000001</li>

</ul>

<p><strong>To convert between currency and microcurrency</strong>,
using dollars as an example currency:</p>

<ul>

<li>To convert dollars
to microdollars, mutiply dollars by 1,000,000</li>

<li>To convert microdollars
to dollars, divide microdollars by 1,000,000</li>

</ul>


* Ad groups belong

to ad campaigns. Some types of campaigns (e.g. budget optimization) have
limits on the number of ad groups they can hold. If you exceed those limits,
you will get an error message.


* **Parameters**

    
    * **ad_account_id** (*str*) – Campaign’s Ad Account ID.


    * **name** (*str*) – Ad Group name.


    * **campaign_id** (*str*) – Campaign ID of the ad group.


    * **billable_event** (*str*) – Ad group billable event type.
    Enum: “CLICKTHROUGH” “IMPRESSION” “VIDEO_V_50_MRC” “BILLABLE_ENGAGEMENT”


    * **budget_in_micro_currency** (*int**, **optional*) – Budget in micro currency. This field is **REQUIRED**
    for non-CBO (campaign budget optimization) campaigns.  A CBO campaign automatically
    generates ad group budgets from its campaign budget to maximize campaign
    outcome. A CBO campaign is limited to 70 or less ad groups. Defaults to None.


    * **bid_in_micro_currency** (*int**, **optional*) – Bid price in micro currency. This field is **REQUIRED**
    for the following campaign objective_type/billable_event combinations: AWARENESS/IMPRESSION,
    CONSIDERATION/CLICKTHROUGH, CATALOG_SALES/CLICKTHROUGH, VIDEO_VIEW/VIDEO_V_50_MRC.
    Defaults to None.


    * **start_time** (*int**, **optional*) – Campaign start time. Unix timestamp in seconds. Only used
    for Campaign Budget Optimization (CBO) campaigns. Defaults to None.


    * **end_time** (*int**, **optional*) – Campaign end time. Unix timestamp in seconds. Only used for
    Campaign Budget Optimization (CBO) campaigns. Defaults to None.


    * **tracking_url** (*str**, **optional*) – Third-party tracking URLs.<br> Python <dict> with the format:
    {“<a href=”[https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event](https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event)”>Tracking
    event enum</a>”:[URL string array],…}<br> For example: {“impression”:
    [“URL1”, “URL2”], “click”: [“URL1”, “URL2”, “URL3”]}.<br>Up to three tracking
    URLs are supported for each event type. Tracking URLs set at the ad group
    or ad level can override those set at the campaign level.
    Pass in an empty object - {} - to remove tracking URLs.<br><br> For more
    information, see                         <a href=”[https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking](https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking)”
    target=”_blank”>Third-party and dynamic tracking</a>. Defaults to None.


    * **auto_targeting_enabled** (*bool**, **optional*) – Enable auto-targeting for ad group. Also known as
    <a href=”[https://help.pinterest.com/en/business/article/expanded-targeting](https://help.pinterest.com/en/business/article/expanded-targeting)”
    target=”_blank”>”expanded targeting”</a>. Defaults to None.


    * **client** ([*PinterestSDKClient*](pinterest.client.md#pinterest.client.PinterestSDKClient)*, **optional*) – PinterestSDKClient Object. Defaults to default_api_client.



* **Returns**

    AdGroup Object



* **Return type**

    AdGroup



#### _classmethod_ get_all(ad_account_id: str, campaign_ids: ~typing.Optional[list[str]] = None, ad_group_ids: ~typing.Optional[list[str]] = None, entity_statuses: ~typing.Optional[list[str]] = None, page_size: ~typing.Optional[int] = None, order: str = 'ASCENDING', bookmark: ~typing.Optional[str] = None, client: ~pinterest.client.PinterestSDKClient = <pinterest.client.PinterestSDKClient object>, \*\*kwargs)
List ad groups based on provided campaign IDs or ad group IDs.(campaign_ids or ad_group_ids).
<p/> <strong>Note:</strong><p/> Provide only campaign_id or ad_group_id. Do not provide both.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True


* **Parameters**

    
    * **ad_account_id** (*str*) – _description_


    * **campaign_ids** (*list**[**str**]**, **optional*) – _description_. Defaults to None.


    * **ad_group_ids** (*list**[**str**]**, **optional*) – _description_. Defaults to None.


    * **page_size** (*int**, **optional*) – _description_. Defaults to None.


    * **order** (*str**, **optional*) – _description_. Defaults to “ASCENDING”.


    * **bookmark** (*str**, **optional*) – _description_. Defaults to None.


    * **client** ([*PinterestSDKClient*](pinterest.client.md#pinterest.client.PinterestSDKClient)*, **optional*) – _description_. Defaults to default_api_client.



* **Returns**

    _description_



* **Return type**

    tuple[list[AdGroup], str]



#### list_ads(ad_ids: Optional[list[str]] = None, entity_statuses: Optional[list[str]] = None, page_size: Optional[int] = None, order: str = 'ASCENDING', bookmark: Optional[str] = None, \*\*kwargs)
Get list of ads under current AdGroup with specified arguments


* **Parameters**

    
    * **ad_ids** (*list**[**str**]**, **optional*) – List of Ad IDs


    * **entity_statuses** (*list**[**str**]**, **optional*) – Possible Entity Statuses “ACTIVE”, “PAUSED” or “ARCHIVED”. Defaults
    to None.


    * **page_size** (*int**[**1..100**]**, **optional*) – Maximum number of items to include in a single page of the response.
    See documentation on Pagination for more information. Defaults to None which will
    return all campaigns.


    * **order** (*str**, **optional*) – The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
    Note that higher-value IDs are associated with more-recently added items. Defaults to
    “ASCENDING”.


    * **bookmark** (*str**, **optional*) – Cursor used to fetch the next page of items. Defaults to None.



* **Returns**

    _description_



* **Return type**

    tuple[list[Ad], str]



#### update_fields(\*\*kwargs)
Update adgroup fields using any arguments


* **Returns**

    if adgroup fields were updated successfully



* **Return type**

    bool


## pinterest.ads.ads module

Ads high level model


### _class_ pinterest.ads.ads.Ad(ad_account_id: str, ad_id: str, client: Optional[[PinterestSDKClient](pinterest.client.md#pinterest.client.PinterestSDKClient)] = None, \*\*kwargs)
Bases: `PinterestBaseModel`

Ad model used to view, create, update its attributes


#### _classmethod_ create(ad_account_id: str, ad_group_id, creative_type: str, pin_id: str, is_pin_deleted: bool = False, is_removable: bool = True, status: str = 'ACTIVE', android_deep_link: ~typing.Optional[str] = None, carousel_android_deep_links: ~typing.Optional[list[str]] = None, carousel_destination_urls: ~typing.Optional[list[str]] = None, carousel_ios_deep_links: ~typing.Optional[list[str]] = None, click_tracking_url: ~typing.Optional[str] = None, destination_url: ~typing.Optional[str] = None, ios_deep_link: ~typing.Optional[str] = None, name: ~typing.Optional[str] = None, tracking_urls: ~typing.Optional[dict] = None, view_tracking_url: ~typing.Optional[str] = None, client: ~pinterest.client.PinterestSDKClient = <pinterest.client.PinterestSDKClient object>, \*\*kwargs)
Create a new ad. Request must contain ad_group_id, creative_type, and the source Pin pin_id.


* **Parameters**

    
    * **ad_account_id** (*str*) – Campaign’s Ad Account ID.


    * **ad_group_id** (*_type_*) – ID of the ad group that contains the ad.


    * **creative_type** (*str*) – Ad creative type enum. Enum: “REGULAR” “VIDEO” “SHOPPING”
    “CAROUSEL” “MAX_VIDEO” “SHOP_THE_PIN” “IDEA”


    * **pin_id** (*str*) – ID of the pin used to make the ad.


    * **status** (*str*) – Entity status of the ad. Enum: “ACTIVE” “PAUSED” “ARCHIVED”


    * **is_pin_deleted** (*bool*) – Is original pin deleted?


    * **is_removable** (*bool*) – Is pin repinnable?


    * **android_deep_link** (*str**, **optional*) – Deep link URL for Android devices. Not currently
    available. Using this field will generate an error. Defaults to None.


    * **carousel_android_deep_links** (*list**[**str**]**, **optional*) – List of deep links for the carousel pin on
    Android. Defaults to None.


    * **carousel_destination_urls** (*list**[**str**]**, **optional*) – List of destination URLs for the carousel
    pin to promote. Defaults to None.


    * **carousel_ios_deep_links** (*list**[**str**]**, **optional*) – List of deep links for the carousel pin on iOS.
    Defaults to None.


    * **click_tracking_url** (*str**, **optional*) – Tracking url for the ad clicks. Defaults to None.


    * **destination_url** (*str**, **optional*) – Destination URL. Defaults to None.


    * **ios_deep_link** (*str**, **optional*) – Deep link URL for iOS devices. Not currently available. Using
    this field will generate an error.Defaults to None.


    * **name** (*str**, **optional*) – Name of the ad - 255 chars max.
    Defaults to None.


    * **tracking_urls** (*dict**, **optional*) – Third-party tracking URLs.<br> Python <dict> with the format:
    {“<a href=”[https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event](https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event)”>Tracking
    event enum</a>”:[URL string array],…}<br> For example: {“impression”:
    [“URL1”, “URL2”], “click”: [“URL1”, “URL2”, “URL3”]}.<br>Up to three tracking
    URLs are supported for each event type. Tracking URLs set at the ad group
    or ad level can override those set at the campaign level.
    Pass in an empty object - {} - to remove tracking URLs.<br><br> For more
    information, see                         <a href=”[https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking](https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking)”
    target=”_blank”>Third-party and dynamic tracking</a>. Defaults to None.


    * **view_tracking_url** (*str**, **optional*) – Tracking URL for ad impressions. Defaults to None.


    * **client** ([*PinterestSDKClient*](pinterest.client.md#pinterest.client.PinterestSDKClient)*, **optional*) – PinterestSDKClient Object. Defaults to default_api_client.



* **Returns**

    _description_



* **Return type**

    Ad



#### _classmethod_ get_all(ad_account_id: str, campaign_ids: ~typing.Optional[list[str]] = None, ad_group_ids: ~typing.Optional[list[str]] = None, ad_ids: ~typing.Optional[list[str]] = None, entity_statuses: ~typing.Optional[list[str]] = None, page_size: ~typing.Optional[int] = None, order: str = 'ASCENDING', bookmark: ~typing.Optional[str] = None, client: ~pinterest.client.PinterestSDKClient = <pinterest.client.PinterestSDKClient object>, \*\*kwargs)
List ads that meet the filters provided:

    
    * Listed campaign ids or ad group ids or ad ids


    * Listed entity statuses <p/>

If no filter is provided, all ads in the ad account are returned.

NOTE:
Provide only campaign_id or ad_group_id or ad_id. Do not provide more than one type.
Review status is provided for each ad; if review_status is REJECTED, the rejected_reasons field will
contain additional information.
For more, see [https://policy.pinterest.com/en/advertising-guidelines](https://policy.pinterest.com/en/advertising-guidelines) Pinterest advertising standards.


* **Parameters**

    
    * **ad_account_id** (*str*) – Ad Account ID


    * **campaign_ids** (*list**[**str**]**, **optional*) – List of Campaign IDs to use to filter the results


    * **ad_group_ids** (*list**[**str**]**, **optional*) – List of Ad Group IDs to use to filter the results


    * **ad_ids** (*list**[**str**]**, **optional*) – List of Ad IDs to use to filter the results


    * **entity_statuses** (*list**[**str**]**, **optional*) – Possible Entity Statuses “ACTIVE”, “PAUSED” or “ARCHIVED”. Defaults
    to None.


    * **page_size** (*int**[**1..100**]**, **optional*) – Maximum number of items to include in a single page of the response.
    See documentation on Pagination for more information. Defaults to None which will
    return all campaigns.


    * **order** (*str**, **optional*) – The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
    Note that higher-value IDs are associated with more-recently added items. Defaults to
    “ASCENDING”.


    * **bookmark** (*str**, **optional*) – Cursor used to fetch the next page of items. Defaults to None.


    * **client** (*ApiClient*) – ApiClient Object



* **Returns**

    List of Ad Objects
    str: Bookmark for pagination if present, else None.



* **Return type**

    list[Ad]



#### update_fields(\*\*kwargs)
Update Ad fields suing any arguments


* **Returns**

    If Ad fields were updated successfully



* **Return type**

    bool


## pinterest.ads.audiences module

High level module class for Audience object


### _class_ pinterest.ads.audiences.Audience(ad_account_id, audience_id, client=None, \*\*kwargs)
Bases: `PinterestBaseModel`

High level model class to manage audiences for an AdAccount


#### _classmethod_ create(ad_account_id: str, name: str, rule: dict, audience_type: str, description: ~typing.Optional[str] = None, client: ~pinterest.client.PinterestSDKClient = <pinterest.client.PinterestSDKClient object>, \*\*kwargs)
Create an audience you can use in targeting for specific ad groups. Targeting combines customer information
with the ways users interact with Pinterest to help you reach specific groups of users; you can include or
exclude specific audience_ids when you create an ad group.

For more information, visit [https://help.pinterest.com/en/business/article/audience-targeting](https://help.pinterest.com/en/business/article/audience-targeting).


* **Parameters**

    
    * **client** ([*PinterestSDKClient*](pinterest.client.md#pinterest.client.PinterestSDKClient)) – PinterestSDKClient Object


    * **ad_account_id** (*str*) – Audience’s Advertiser or Ad Account ID.


    * **name** (*str*) – Audience name.


    * **rule** (*dict*) – python <dict> defining targeted audience users. The keys and value formats:

        rule_example_format = {
        country (str): Valid countries include: “US”, “CA”, and “GB”
        customer_list_id (str): Customer list ID. For CUSTOMER_LIST audience_type
        engagement_domain (list[str]): The audience account’s verified domain. **Required** for ENGAGEMENT audience_type
        engagement_type (str): Engagement type enum. Optional for ENGAGEMENT audience_type. Supported values are click, save, closeup, comment and like. All engagements are included if this field is not set.
        event (str): A Pinterest tag event. Optional for VISITOR audience_type. Possible values are pagevisit, signup, checkout, viewcategory, search, addtocart, watchvideo, lead, and custom. This field also accepts a partner-defined Pinterest tag event.
        event_data: **NOT YET SUPPORTED**
        percentage (int): Percentage should be 1-10. The targeted audience should be this % size across Pinterest.
        pin_id (list[str]): IDs of engaged organic pins. Optional for ENGAGEMENT audience_type. For example, “pin_id:”: [“34567”].
        prefill (bool): Optional for VISITOR audience_type. If true, the specified rule on existing engagement data is applied to pre-populate the audience. If false, the audience is empty at creation time. The default is true.
        retention_days (int): Number of days a Pinterest user remains in the audience. Optional for ENGAGEMENT and VISITOR audience_type. Accepted range is 1-540. Defaults to 180 if not specified.
        seed_id ([str]): Audience ID(s). For ACTALIKE audience_type.
        url ([str]): Optional for ENGAGEMENT or VISITOR audience_type. For ENGAGEMENT, it is the engaged pin’s URL. For VISITOR, you can use it as a string or a {operator: value} object for filtering visitors based on conversion tag event URLs. Supported operators are [ =, !=, contains, not_contains].<br>Example 1:  “url”: “[http://www.myonlinestore123.com/view_item/shoe](http://www.myonlinestore123.com/view_item/shoe)”<br>Example 2: “url”: {“contains”: “view_item_shoe”}.
        visitor_source_id (str): The conversion tag ID, or the Pinterest tag ID, that you use on your website. For VISITOR audience_type.
        event_source (dict): Optional for VISITOR. You can use it as a {‘=’: [value]}. Supported values are: web, mobile, offline.
        ingestion_source (dict): Optional for VISITOR. You can use it as a {‘=’: [value]}. Supported values are: tag, mmp, file_upload, conversions_api.
        engager_type (int): Optional for ENGAGEMENT. Engager type value should be 1-2.
        campaign_id (list[str]): Campaign ID for engagement audience filter.
        ad_id (list[str]): Ad ID for engagement audience filter.
        objective_type (list[str]): Objective for engagement audience filter.

    }



    * **audience_type** (*str*) – Enum (“CUSTOMER_LIST” “VISITOR” “ENGAGEMENT” “ACTALIKE”)



* **Keyword Arguments**

    **endpoint.** (*Any valid keyword arguments** or **query parameters for*) – 



* **Returns**

    Audience Object



* **Return type**

    Audience



#### _classmethod_ get_all(ad_account_id: str, entity_statuses: ~typing.Optional[list[str]] = None, page_size: ~typing.Optional[int] = None, order: str = 'ASCENDING', bookmark: ~typing.Optional[str] = None, client: ~pinterest.client.PinterestSDKClient = <pinterest.client.PinterestSDKClient object>, \*\*kwargs)
Get a list of the audiences in the AdAccount, filtered by the specified arguments


* **Parameters**

    
    * **client** ([*PinterestSDKClient*](pinterest.client.md#pinterest.client.PinterestSDKClient)) – PinterestSDKClient Object


    * **ad_account_id** (*str*) – Audience’s Advertiser ID.


    * **entity_statuses** (*list**[**str**]**, **optional*) – Possible Entity Statuses “ACTIVE”, “PAUSED” or “ARCHIVED”. Defaults
    to None.


    * **page_size** (*int**[**1..100**]**, **optional*) – Maximum number of items to include in a single page of the response.
    See documentation on Pagination for more information. Defaults to None which will
    return default number of audiences.


    * **order** (*str**, **optional*) – The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
    Note that higher-value IDs are associated with more-recently added items. Defaults to
    “ASCENDING”.


    * **bookmark** (*str**, **optional*) – Cursor used to fetch the next page of items. Defaults to None.



* **Keyword Arguments**

    **endpoint.** (*Any valid keyword arguments** or **query parameters for*) – 



* **Returns**

    List of Audience Objects
    bookmark (str): Bookmark for pagination if present, else None.



* **Return type**

    campaign_list (list[Audience])



#### update_fields(\*\*kwargs)
Update audience fields


* **Keyword Arguments**

    **values** (*Any valid audience fields with valid*) – 


## pinterest.ads.campaigns module

Campaign Class for Pinterest Python SDK


### _class_ pinterest.ads.campaigns.Campaign(ad_account_id: str, campaign_id: str, client: Optional[[PinterestSDKClient](pinterest.client.md#pinterest.client.PinterestSDKClient)] = None, \*\*kwargs)
Bases: `PinterestBaseModel`

Campaign model used to view, create, update its attributes and list its different entities.


#### activate()
Activate a paused or archived campaign


* **Returns**

    If campaign status was successfully changed to ‘ACTIVE’



* **Return type**

    bool



#### archive()
Archive an active or paused campaign


* **Returns**

    If campaign status was successfully changed to ‘ARCHIVED’



* **Return type**

    bool



#### _classmethod_ create(ad_account_id: str, name: str, objective_type: str, status: str = 'ACTIVE', lifetime_spend_cap: ~typing.Optional[int] = None, daily_spend_cap: ~typing.Optional[int] = None, order_line_id: ~typing.Optional[int] = None, tracking_urls: ~typing.Optional[str] = None, start_time: ~typing.Optional[int] = None, end_time: ~typing.Optional[int] = None, is_campaign_budget_optimization: bool = False, is_flexible_daily_budgets: bool = False, default_ad_group_budget_in_micro_currency: ~typing.Optional[int] = None, is_automated_campaign: bool = False, client: ~pinterest.client.PinterestSDKClient = <pinterest.client.PinterestSDKClient object>, \*\*kwargs)
Create a new campaign. Every campaign has its own campaign_id        and houses one or more ad groups, which contain one or more ads.

For more,        see <a href=”[https://help.pinterest.com/en/business/article/set-up-your-campaign/](https://help.pinterest.com/en/business/article/set-up-your-campaign/)”>
Set up your campaign</a>. <p/>

<strong>Note:</strong>


* The values for        ‘lifetime_spend_cap’ and ‘daily_spend_cap’ are microcurrency amounts based        on the currency field set in the advertiser’s profile. (e.g. USD) <p/>

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


* **Parameters**

    
    * **ad_account_id** (*str*) – Campaign’s Ad Account ID.


    * **name** (*str*) – Campaign name.


    * **objective_type** (*ObjectiveType*) – Campaign objective type. Enum: “AWARENESS”, “CONSIDERATION”,
    “VIDEO_VIEW”, “WEB_CONVERSION”, “CATALOG_SALES”, “WEB_SESSIONS”


    * **status** (*str**, **optional*) – _description_. Defaults to ‘ACTIVE’.


    * **lifetime_spend_cap** (*int**, **optional*) – Campaign total spending cap. Defaults to None.


    * **daily_spend_cap** (*int**, **optional*) – Campaign daily spending cap. Defaults to None.


    * **order_line_id** (*int**, **optional*) – Order line ID that appears on the invoice.
    Defaults to None.


    * **tracking_urls** (*str**, **optional*) – Third-party tracking URLs.<br> Python <dict> with the format:
    {“<a href=”[https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event](https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event)”>Tracking
    event enum</a>”:[URL string array],…}<br> For example: {“impression”:
    [“URL1”, “URL2”], “click”: [“URL1”, “URL2”, “URL3”]}.<br>Up to three tracking
    URLs are supported for each event type. Tracking URLs set at the ad group
    or ad level can override those set at the campaign level.
    Pass in an empty object - {} - to remove tracking URLs.<br><br> For more
    information, see                         <a href=”[https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking](https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking)”
    target=”_blank”>Third-party and dynamic tracking</a>. Defaults to None.


    * **start_time** (*int**, **optional*) – Campaign start time. Unix timestamp in seconds. Only used
    for Campaign Budget Optimization (CBO) campaigns. Defaults to None.


    * **end_time** (*int**, **optional*) – Campaign end time. Unix timestamp in seconds. Only used for
    Campaign Budget Optimization (CBO) campaigns. Defaults to None.


    * **is_campaign_budget_optimization** (*bool**, **optional*) – Determines if a campaign automatically
    generate ad-group level budgets given a campaign budget to maximize
    campaign outcome. When transitioning from non-cbo to cbo, all
    previous child ad group budget will be cleared. Defaults to False.


    * **is_flexible_daily_budgets** (*bool**, **optional*) – Determines if a campaign has flexible
    daily budgets setup. Defaults to False.


    * **default_ad_group_budget_in_micro_currency** (*int**, **optional*) – When transitioning from
    campaign budget optimization to non-campaign budget optimization,
    the default_ad_group_budget_in_micro_currency will propagate to
    each child ad groups daily budget. Unit is micro currency
    of the associated advertiser account. Defaults to None.


    * **is_automated_campaign** (*bool**, **optional*) – Specifies whether the campaign was created
    in the automated campaign flow. Defaults to False.


    * **client** ([*PinterestSDKClient*](pinterest.client.md#pinterest.client.PinterestSDKClient)) – PinterestSDKClient Object



* **Keyword Arguments**

    **endpoint.** (*Any valid keyword arguments** or **query parameters for*) – 



* **Returns**

    Campaign Object



* **Return type**

    Campaign



#### _classmethod_ get_all(ad_account_id: str, campaign_ids: ~typing.Optional[list[str]] = None, entity_statuses: ~typing.Optional[list[str]] = None, page_size: ~typing.Optional[int] = None, order: str = 'ASCENDING', bookmark: ~typing.Optional[str] = None, client: ~pinterest.client.PinterestSDKClient = <pinterest.client.PinterestSDKClient object>, \*\*kwargs)
Get a list of the campaigns in the AdAccount, filtered by the specified arguments


* **Parameters**

    
    * **ad_account_id** (*str*) – Campaign’s Ad Account ID.


    * **campaign_ids** (*list**[**str**]**, **optional*) – List of Campaign Ids to use to filter the results. Defaults to None.


    * **entity_statuses** (*list**[**str**]**, **optional*) – Possible Entity Statuses “ACTIVE”, “PAUSED” or “ARCHIVED”. Defaults
    to None.


    * **page_size** (*int**[**1..100**]**, **optional*) – Maximum number of items to include in a single page of the response.
    See documentation on Pagination for more information. Defaults to None which will
    return default page size campaigns.


    * **order** (*str**, **optional*) – The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
    Note that higher-value IDs are associated with more-recently added items. Defaults to
    “ASCENDING”.


    * **bookmark** (*str**, **optional*) – Cursor used to fetch the next page of items. Defaults to None.


    * **client** ([*PinterestSDKClient*](pinterest.client.md#pinterest.client.PinterestSDKClient)) – PinterestSDKClient Object



* **Keyword Arguments**

    **endpoint.** (*Any valid keyword arguments** or **query parameters for*) – 



* **Returns**

    List of Campaign Objects
    str: Bookmark for pagination if present, else None.



* **Return type**

    list[Campaign]



#### get_daily_budget()
Get the current daily spend cap budget of the campaign.


* **Returns**

    Current daily spend cap budget



* **Return type**

    float



#### get_lifetime_budget()
Get the current life time spend cap budget of the campaign.


* **Returns**

    Current life time spend cap budget



* **Return type**

    float



#### list_ad_groups(page_size: int = 25, order: str = 'ASCENDING', bookmark: Optional[str] = None, entity_statuses: Optional[list[str]] = None, \*\*kwargs)
List ad groups directed related to campaign.
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True


* **Parameters**

    
    * **page_size** (*int**, **optional*) – _description_. Defaults to None.


    * **order** (*str**, **optional*) – _description_. Defaults to “ASCENDING”.


    * **bookmark** (*str**, **optional*) – _description_. Defaults to None.


    * **entity_statuses** (*str**, **optional*) – _description_. Defaults to None.



* **Returns**

    _description_



* **Return type**

    tuple[list[AdGroup], str]



#### pause()
Pause an active or archived campaign


* **Returns**

    If campaign status was successfully changed to ‘PAUSED’



* **Return type**

    bool



#### set_daily_budget(new_spend_cap: int)
Set new daily spend cap budget for the campaign.


* **Parameters**

    **new_spend_cap** (*int*) – The new campaign daily spending cap.



* **Returns**

    If the daily budget was changed successfully



* **Return type**

    bool



#### set_lifetime_budget(new_spend_cap: int)
Set new life time spend cap budget for the campaign.


* **Parameters**

    **new_spend_cap** (*int*) – The new campaign total spending cap.



* **Returns**

    If the lifetime budget was changed successfully



* **Return type**

    bool



#### update_fields(\*\*kwargs)
Update the campaign fields using any attributes.


* **Keyword Arguments**

    **values** (*Any valid campaign fields with valid*) – 



* **Returns**

    If campaign fields were successfully updated



* **Return type**

    bool


## pinterest.ads.customer_lists module

High level module class for Customer List object


### _class_ pinterest.ads.customer_lists.CustomerList(ad_account_id, customer_list_id, client=None, \*\*kwargs)
Bases: `PinterestBaseModel`

High level model class to manage customer_lists for an CustomerList


#### add_record(record)
Add records to an existing customer list, the system scans the additions for existing Pinterest accounts; those
are the records that will be added to your “CUSTOMER_LIST” audience.

Your original list of records to add will be deleted when the matching process is complete.


* **Parameters**

    
    * **record** (*str*) – Records list. Can be any combination of emails, MAIDs, or IDFAs. Emails must be


    * **SHA1** (*lowercase and can be plain text** or **hashed using*) – 


    * **SHA256** – 


    * **with** (*or MD5. MAIDs and IDFAs must be hashed*) – 


    * **SHA1** – 


    * **SHA256** – 


    * **MD5.** (*or*) – 



* **Returns**

    If record was added to the customer list fields were successfully updated



* **Return type**

    bool



#### _classmethod_ create(ad_account_id: str, name: str, records: str, list_type: str = 'EMAIL', client: ~pinterest.client.PinterestSDKClient = <pinterest.client.PinterestSDKClient object>, \*\*kwargs)
Create a customer list from your records(hashed or plain-text email addresses, or hashed MAIDs or IDFAs).

A customer list is one of the four types of Pinterest audiences: for more information, see <a href=”[https://help.pinterest.com/en/business/article/audience-targeting](https://help.pinterest.com/en/business/article/audience-targeting)”>Audience targeting</a>
or the <a href=”[https://developers.pinterest.com/docs/features/ads-management/#Audiences](https://developers.pinterest.com/docs/features/ads-management/#Audiences)”>Audiences</a> section of the ads management guide.

Please review our <a href=”[https://help.pinterest.com/en/business/article/audience-targeting#section-13341](https://help.pinterest.com/en/business/article/audience-targeting#section-13341)”>requirements</a> for what type of information is allowed when uploading a customer list.

When you create a customer list, the system scans the list for existing Pinterest accounts; the list
must include at least 100 Pinterest accounts. Your original list will be deleted when the matching process
is complete. The filtered list – containing only the Pinterest accounts that were included in your starting
list – is what will be used to create the audience.

Note that once you have created your customer list, you must convert it into an audience
(of the “CUSTOMER_LIST” type) using the <a href=”[https://developers.pinterest.com/docs/api/v5/#operation/create_audience_handler](https://developers.pinterest.com/docs/api/v5/#operation/create_audience_handler)”>create audience endpoint</a> before it can be used.


* **Parameters**

    
    * **ad_account_id** (*str*) – Unique identifier of an ad account.


    * **name** (*str*) – Customer list name.


    * **records** (*str*) – Records list. Can be any combination of emails, MAIDs, or IDFAs. Emails must be lowercase
    and can be plain text or hashed using SHA1, SHA256, or MD5. MAIDs and IDFAs must be hashed with SHA1, SHA256, or MD5.


    * **list_type** (*str**, **optional*) – User list type. Possible Enum: “EMAIL” “IDFA” “MAID” “LR_ID” “DLX_ID” “HASHED_PINNER_ID”. Defaults to “EMAIL”.


    * **client** ([*PinterestSDKClient*](pinterest.client.md#pinterest.client.PinterestSDKClient)*, **optional*) – Defaults to default_api_client.



* **Keyword Arguments**

    **endpoint.** (*Any valid keyword arguments** or **query parameters for*) – 



* **Returns**

    CustomerList object



* **Return type**

    CustomerList



#### _classmethod_ get_all(ad_account_id: str, page_size: ~typing.Optional[int] = None, order: ~typing.Optional[str] = None, bookmark: ~typing.Optional[str] = None, client: ~pinterest.client.PinterestSDKClient = <pinterest.client.PinterestSDKClient object>, \*\*kwargs)
Get a list of the customer lists in the AdAccount, filtered by the specified arguments


* **Parameters**

    
    * **ad_account_id** (*str*) – Campaign’s Ad Account ID.


    * **page_size** (*int**, **optional*) – Maximum number of items to include in a single page of the response.
    See documentation on Pagination for more information. Defaults to None which will
    return default page size customer lists.


    * **order** (*str**, **optional*) – _description_. Defaults to None.


    * **bookmark** (*str**, **optional*) – Cursor used to fetch the next page of items. Defaults to None.


    * **client** ([*PinterestSDKClient*](pinterest.client.md#pinterest.client.PinterestSDKClient)*, **optional*) – PinterestSDKClient Object



* **Keyword Arguments**

    **endpoint.** (*Any valid keyword arguments** or **query parameters for*) – 



* **Returns**

    List of CustomerList Objects
    str: Bookmark for pagination if present, else None.



* **Return type**

    list[CustomerList]



#### remove_record(record)
Remove records to an existing customer list.


* **Parameters**

    
    * **record** (*str*) – Records list. Can be any combination of emails, MAIDs, or IDFAs. Emails must be


    * **SHA1** (*lowercase and can be plain text** or **hashed using*) – 


    * **SHA256** – 


    * **with** (*or MD5. MAIDs and IDFAs must be hashed*) – 


    * **SHA1** – 


    * **SHA256** – 


    * **MD5.** (*or*) – 



* **Returns**

    If record was removed to the customer list fields were successfully updated



* **Return type**

    bool



#### update_fields(\*\*kwargs)
Update customer lists fields with valid values

Keywords Args:

    Any valid customer list field with valid value

## pinterest.ads.keywords module

High level module class for Keyword object


### _class_ pinterest.ads.keywords.Keyword(ad_account_id, keyword_id, client=None, \*\*kwargs)
Bases: `PinterestBaseModel`

High level model class to manage keywords


#### _classmethod_ create(ad_account_id: str, parent_id: str, value: str, bid: ~typing.Optional[int] = None, match_type: ~typing.Optional[str] = None, client: ~pinterest.client.PinterestSDKClient = <pinterest.client.PinterestSDKClient object>, \*\*kwargs)
Create keywords for follow entity types (advertiser, campaign, ad group or ad).

NOTE:
- Advertisers campaigns can only be assigned keywords with excluding (‘_NEGATIVE’).
- All keyword match types are available for ad groups.


* **Parameters**

    
    * **ad_account_id** (*str*) – Ad Account ID


    * **parent_id** (*str*) – Keyword parent entity ID (advertiser, campaign, ad group)


    * **bid** (*float*) – Keyword custom bid


    * **match_type** (*str*) – Keyword match type, ENUM: “BOARD”, “PHRASE”, “EXACT”, “EXACT_NEGATIVE”,
    “PHRASE_NEGATIVE”, null


    * **value** (*str*) – Keyword value(120 chars max)



* **Returns**

    Keyword Object



* **Return type**

    Keyword



#### _classmethod_ get_all(ad_account_id: str, page_size: ~typing.Optional[int] = None, bookmark: ~typing.Optional[str] = None, client: ~pinterest.client.PinterestSDKClient = <pinterest.client.PinterestSDKClient object>, \*\*kwargs)
Get a list of keywords bases on the filters provided.

NOTE:
- Advertisers campaigns can only be assigned keywords with excluding (‘_NEGATIVE’).
- All keyword match types are available for ad groups.


* **Parameters**

    
    * **ad_account_id** (*str*) – Ad Account ID.


    * **page_size** (*int**[**1..100**]**, **optional*) – Maximum number of items to include in a single page of the response.
    See documentation on Pagination for more information. Defaults to None which will
    return all campaigns.


    * **bookmark** (*str**, **optional*) – Cursor used to fetch the next page of items. Defaults to None.


    * **client** ([*PinterestSDKClient*](pinterest.client.md#pinterest.client.PinterestSDKClient)*, **optional*) – _description_. Defaults to default_api_client.



* **Returns**

    List of Keyword Objects
    str: Bookmark for paginations if present, else None.



* **Return type**

    list[Keyword]



#### update_fields(\*\*kwargs)
Update keyword fields using any attributes


* **Keyword Arguments**

    **values** (*Any valid keyword fields with valid*) – 



* **Returns**

    if keyword fields were successfully updated



* **Return type**

    bool


## Module contents
