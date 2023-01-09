<!-- markdownlint-disable -->

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/pinterest/organic/pins.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `organic.pins`
Pin Class for Pinterest Python SDK 



---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/pinterest/organic/pins.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Pin`
Pin model used to view, create, update its attributes and list its different entities. 

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/pinterest/organic/pins.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    pin_id: 'str',
    ad_account_id: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → None
```

Initialize or get a Pin owned by the "operation user_account" - or on a group board that has been shared with this account. 

By default, the "operation user_account" is the token user_account. Optional: Business Access: Specify an ad_account_id (obtained via List ad accounts) to use the owner of that ad_account as the "operation user_account". In order to do this, the token user_account must have one of the following Business Access roles on the ad_account: 


- For Pins on public or protected boards: Owner, Admin, Analyst, Campaign Manager. 
- For Pins on secret boards: Owner, Admin. 



**Args:**
 
 - <b>`pin_id`</b> (str):  Unique identifier of a Pin. 
 - <b>`ad_account_id`</b> (str, optional):  Unique identifier of an ad account. Defaults to None. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Uses the default client, if not provided. 


---

#### <kbd>property</kbd> alt_text





---

#### <kbd>property</kbd> board_id





---

#### <kbd>property</kbd> board_owner





---

#### <kbd>property</kbd> board_section_id





---

#### <kbd>property</kbd> created_at





---

#### <kbd>property</kbd> description





---

#### <kbd>property</kbd> dominant_color





---

#### <kbd>property</kbd> id





---

#### <kbd>property</kbd> link





---

#### <kbd>property</kbd> media





---

#### <kbd>property</kbd> media_source





---

#### <kbd>property</kbd> parent_pin_id





---

#### <kbd>property</kbd> title







---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/pinterest/organic/pins.py#L140"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create`

```python
create(
    board_id: 'str',
    media_source: 'dict',
    link: 'str' = None,
    title: 'str' = None,
    description: 'str' = None,
    dominant_color: 'str' = None,
    alt_text: 'str' = None,
    board_section_id: 'str' = None,
    parent_pin_id: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → Pin
```

Create a Pin on a board or board section owned by the "operation user_account". 

Note: If the current "operation user_account" (defined by the access token) has access to another user's Ad Accounts via Pinterest Business Access, you can modify your request to make use of the current operation_user_account's permissions to those Ad Accounts by including the ad_account_id in the path parameters for the request (e.g. .../?ad_account_id=12345&...). 

This function is intended solely for publishing new content created by the user. If you are interested in saving content created by others to your Pinterest boards, sometimes called 'curated content', please use our Save button (https://developers.pinterest.com/docs/add-ons/save-button) instead. For more tips on creating fresh content for Pinterest, review our Content App Solutions Guide (https://developers.pinterest.com/docs/solutions/content-apps). 

Learn more (https://developers.pinterest.com/docs/solutions/content-apps/#creatingvideopins) about video Pin creation 



**Args:**
 
 - <b>`board_id`</b> (str):  The board to which this Pin belongs. 
 - <b>`media_source`</b> (dict):  Pin media source. In format:  { 
 - <b>`'source_type'`</b>:  (str), 
 - <b>`'content_type'`</b>:  (str), 
 - <b>`'data'`</b>:  (str), 
 - <b>`'url'`</b>:  (str), 
 - <b>`'cover_image_url'`</b>:  (str), 
 - <b>`'media_id'`</b>:  (str), } 
 - <b>`link`</b> (str, optional):  Redirect link of <= 2048 characters. Defaults to None. 
 - <b>`title`</b> (str, optional):  Title of the pin <= 100 characters. Defaults to None. 
 - <b>`description`</b> (str, optional):  Description of the pin <= 500 characters. Defaults to None. 
 - <b>`dominant_color`</b> (str, optional):  Dominant pin color. Hex number, e.g. "#6E7874". Defaults to None. 
 - <b>`alt_text`</b> (str, optional):  <= 500 characters. Defaults to None. 
 - <b>`board_section_id`</b> (str, optional):  The board section to which this Pin belongs. Defaults to None. 
 - <b>`parent_pin_id`</b> (str, optional):  The source pin id if this pin was saved from another pin. 
 - <b>`Learn more (https`</b>: //help.pinterest.com/article/save-pins-on-pinterest). Defaults to None. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object, uses the default client, if not provided. 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`Pin`</b>:  Pin object 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/pinterest/organic/pins.py#L222"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `delete`

```python
delete(pin_id: 'str', client: 'PinterestSDKClient' = None) → bool
```

Delete a Pin owned by the "operation user_account". 


- By default, the "operation user_account" is the token user_account. 



**Args:**
 
 - <b>`pin_id`</b> (str):  Unique identifier of a pin. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Uses the default client, if not provided. 



**Returns:**
 
 - <b>`bool`</b>:  If the pin was deleted successfully. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/pinterest/organic/pins.py#L250"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `save`

```python
save(board_id: 'str', board_section_id: 'str' = None) → None
```

Save a pin on a board or board section owned by the "operation user_account". 


- By default, the "operation user_account" is the token user_account. 



**Args:**
 
 - <b>`board_id`</b> (str):  Unique identifier of the board to which the pin will be saved. Defaults to None. 
 - <b>`board_section_id`</b> (str, optional):  Unique identifier of the board section to which the pin will be saved.  Defaults to None. 


