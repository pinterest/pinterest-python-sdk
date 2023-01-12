<!-- markdownlint-disable -->

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/keywords.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ads.keywords`
High level module class for Keyword object 



---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/keywords.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Keyword`
High level model class to manage keywords 

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/keywords.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(ad_account_id, keyword_id, client=None, **kwargs)
```






---

#### <kbd>property</kbd> archived





---

#### <kbd>property</kbd> bid





---

#### <kbd>property</kbd> id





---

#### <kbd>property</kbd> match_type





---

#### <kbd>property</kbd> parent_id





---

#### <kbd>property</kbd> parent_type





---

#### <kbd>property</kbd> type





---

#### <kbd>property</kbd> value







---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/keywords.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create`

```python
create(
    ad_account_id: 'str',
    parent_id: 'str',
    value: 'str',
    bid: 'int' = None,
    match_type: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → Keyword
```

Create keywords for follow entity types (advertiser, campaign, ad group or ad). 



**NOTE:**

> - Advertisers campaigns can only be assigned keywords with excluding ('_NEGATIVE'). - All keyword match types are available for ad groups. 
>

**Args:**
 
 - <b>`ad_account_id`</b> (str):  Ad Account ID 
 - <b>`parent_id`</b> (str):  Keyword parent entity ID (advertiser, campaign, ad group) 
 - <b>`bid`</b> (float):  Keyword custom bid 
 - <b>`match_type`</b> (str):  Keyword match type, ENUM: "BOARD", "PHRASE", "EXACT", "EXACT_NEGATIVE",  "PHRASE_NEGATIVE", null 
 - <b>`value`</b> (str):  Keyword value(120 chars max) 



**Returns:**
 
 - <b>`Keyword`</b>:  Keyword Object 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/keywords.py#L154"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get_all`

```python
get_all(
    ad_account_id: 'str',
    page_size: 'int' = None,
    bookmark: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → tuple[list[Keyword], str]
```

Get a list of keywords bases on the filters provided. 



**NOTE:**

> - Advertisers campaigns can only be assigned keywords with excluding ('_NEGATIVE'). - All keyword match types are available for ad groups. 
>

**Args:**
 
 - <b>`ad_account_id`</b> (str):  Ad Account ID. 
 - <b>`page_size`</b> (int[1..100], optional):  Maximum number of items to include in a single page of the response.  See documentation on Pagination for more information. Defaults to None which will  return all campaigns. 
 - <b>`bookmark`</b> (str, optional):  Cursor used to fetch the next page of items. Defaults to None. 
 - <b>`client`</b> (PinterestSDKClient, optional):  Defaults to the default api client. 



**Returns:**
 
 - <b>`list[Keyword]`</b>:  List of Keyword Objects 
 - <b>`str`</b>:  Bookmark for paginations if present, else None. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/keywords.py#L206"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_fields`

```python
update_fields(**kwargs) → bool
```

Update keyword fields using any attributes 

Keyword Args:  Any valid keyword fields with valid values 



**Returns:**
 
 - <b>`bool`</b>:  if keyword fields were successfully updated 


