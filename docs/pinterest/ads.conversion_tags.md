<!-- markdownlint-disable -->

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/conversion_tags.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ads.conversion_tags`
Conversion Class for Pinterest Python SDK 



---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/conversion_tags.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ConversionTag`
Conversion Tag model used to view, create, update its attributes and list its different entities 

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/conversion_tags.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    ad_account_id: 'str',
    conversion_tag_id: 'str',
    client: 'PinterestSDKClient' = None,
    **kwargs
) → None
```

Initialize Conversion Tag Object. 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  ConversionTag's Ad Account ID 
 - <b>`conversion_tag_id`</b> (str):  ConversionTag ID, must be associated with Ad Account ID provided 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Uses the default client, if not provided. 


---

#### <kbd>property</kbd> ad_account_id





---

#### <kbd>property</kbd> code_snippet





---

#### <kbd>property</kbd> configs





---

#### <kbd>property</kbd> enhanced_match_status





---

#### <kbd>property</kbd> id





---

#### <kbd>property</kbd> last_fired_time_ms





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> status





---

#### <kbd>property</kbd> version







---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/conversion_tags.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create`

```python
create(
    ad_account_id: 'str',
    name: 'str',
    aem_enabled: 'bool' = None,
    md_frequency: 'float' = None,
    aem_fnln_enabled: 'bool' = None,
    aem_ph_enabled: 'bool' = None,
    aem_ge_enabled: 'bool' = None,
    aem_db_enabled: 'bool' = None,
    aem_loc_enabled: 'bool' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → ConversionTag
```

Create a conversion tag, also known as        <a href="https://help.pinterest.com/en/business/article/set-up-the-pinterest-tag"\ target="_blank">Pinterest tag</a> with the option to enable enhance match.<p/> 

The Pinterest Tag tracks actions people take on the ad account’        s website after they view the ad account's ad on Pinterest. The advertiser        needs to customize this tag to track conversions.<p/> 

For more information,        see:<p/> 

<a class="reference external"         href="https://help.pinterest.com/en/business/article/set-up-the-pinterest-tag"        >Set up the Pinterest tag</a><p/> 

<a class="reference external" href="        https://developers.pinterest.com/docs/conversions/pinterest-tag/">Pinterest        Tag</a><p/> 

<a class="reference external" href="https://developers.pinterest.com/docs/conversions/enhanced-match/"        >Enhanced match</a>" 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  ConversionTag's Ad Account ID 
 - <b>`name`</b> (str):  ConversionTag name 
 - <b>`aem_enabled`</b> (bool=False, Nullable):  Whether Automatic Enhanced Match email is enabled. See            Enhanced match for more information. 


 - <b>`md_frequency`</b> (float=1.0, Nullable):  Metadata ingestion frequency. 
 - <b>`aem_fnln_enabled`</b> (bool=False, Nullable):  Whether Automatic Enhanced Match name is enabled. See            Enhanced match for more information. 


 - <b>`aem_ph_enabled`</b> (bool=False, Nullable):  Whether Automatic Enhanced Match phone is enabled. See            Enhanced match for more information. 


 - <b>`aem_ge_enabled`</b> (bool=False, Nullable):  Whether Automatic Enhanced Match gender is enabled. See            Enhanced match for more information. 


 - <b>`aem_db_enabled`</b> (bool=False, Nullable):  Whether Automatic Enhanced Match birthdate is enabled. See            Enhanced match for more information. 


 - <b>`aem_loc_enabled`</b> (bool=False, Nullable):  Whether Automatic Enhanced Match location is enabled. See            Enhanced match for more information. 



**Returns:**
 
 - <b>`ConversionTag`</b>:  ConversionTag Object 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/conversion_tags.py#L199"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get_all`

```python
get_all(
    ad_account_id: 'str',
    filter_deleted: 'bool' = False,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → list[ConversionTag]
```

Get a list of ConversionTag, filter by specified arguments 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  Unique identifier of an ad account. 
 - <b>`filter_deleted`</b> (bool=False, optional):  Filter out deleted tags. 
 - <b>`client`</b> (_type_, optional):  PinterestSDKClient Object. Uses the default client, if not provided. 



**Returns:**
 
 - <b>`list[ConversionTag]`</b>:  List of ConversionTags 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/conversion_tags.py#L279"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get_ocpm_eligible_conversion_tag_events`

```python
get_ocpm_eligible_conversion_tag_events(
    ad_account_id: 'str',
    client: 'PinterestSDKClient' = None,
    **kwargs
) → tuple[str, list[ConversionEventResponse]]
```

Get OCPM eligible conversion tag events for an Ad Account. 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  Ad Account ID 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Uses the default client, if not provided. 



**Returns:**
 
 - <b>`list[ConversionEventResponse]`</b>:  List of ConversionTagEvent 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/conversion_tags.py#L237"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get_page_visit_conversion_tag_events`

```python
get_page_visit_conversion_tag_events(
    ad_account_id: 'str',
    page_size: 'int' = None,
    order: 'str' = 'ASCENDING',
    bookmark: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → tuple[list[ConversionEventResponse], Bookmark]
```

Get page visit conversion tag events for an ad account. 



**Args:**
 
 - <b>`ad_account`</b> (str):  Ad Account ID 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Uses the default client, if not provided. 



**Returns:**
 
 - <b>`list[ConversionEventResponse]`</b>:  List of ConversionTagEvent 


