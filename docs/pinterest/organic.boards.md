<!-- markdownlint-disable -->

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `organic.boards`
Board Class for Pinterest Python SDK 



---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BoardSection`
Board Section model used as a helper model for `BOARD` 

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(board_section_id: 'str', name: 'str') → None
```

Initialize a Board Section object. 



**Args:**
 
 - <b>`board_section_id`</b> (str):  Unique identifier of a board section. 
 - <b>`name`</b> (str):  Name for the board section. 


---

#### <kbd>property</kbd> id





---

#### <kbd>property</kbd> name







---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create`

```python
create(
    board_id: 'str',
    name: 'str',
    client: 'PinterestSDKClient' = None
) → BoardSection
```

Class method to help create a board section. 



**Args:**
 
 - <b>`board_id`</b> (str):  Unique identifier of a board. 
 - <b>`name`</b> (str):  Name for the board section. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Uses the default client, if not provided. 



**Returns:**
 
 - <b>`BoardSection`</b>:  The created board section. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `delete`

```python
delete(
    board_id: 'str',
    board_section_id: 'str',
    client: 'PinterestSDKClient' = None
) → None
```

Class method to help delete a board section. 



**Args:**
 
 - <b>`board_id`</b> (str):  Unique identifier of a board. 
 - <b>`board_section_id`</b> (str):  Unique identifier of a board section. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Uses the default client, if not provided. 



**Returns:**
 None 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get_all`

```python
get_all(
    board_id: 'str',
    page_size: 'int' = None,
    bookmark: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → tuple[list[BoardSection], Bookmark]
```

List board sections in a given board id. 





**Args:**
 
 - <b>`board_id`</b> (str, optional):  Unique identifier of a board. 
 - <b>`page_size`</b> (int[1..100], optional):  Maximum number of items to include in a single page of the response.  See documentation on Pagination for more information. Defaults to None which will  return default page size campaigns. 
 - <b>`bookmark`</b> (str, optional):  Cursor used to fetch the next page of items. Defaults to None. 
 - <b>`client`</b> (PinterestSDKClient, optional):  _description_. Defaults to None. 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`list[BoardSection]`</b>:  List of BoardSection Objects 
 - <b>`Bookmark`</b>:  Bookmark for pagination if present, else None. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `update`

```python
update(
    board_id: 'str',
    board_section_id: 'str',
    name: 'str',
    client: 'PinterestSDKClient' = None
) → BoardSection
```

Class method to help update a board section. 



**Args:**
 
 - <b>`board_id`</b> (str):  Unique identifier of a board. 
 - <b>`board_section_id`</b> (str):  Unique identifier of a board section. 
 - <b>`name`</b> (str):  Name for the board section. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Uses the default client, if not provided. 



**Returns:**
 
 - <b>`BoardSection`</b>:  The updated board section. 


---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L190"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Board`
Board model used to view, create, update its attributes and list its different entities. 

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L194"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(board_id: 'str', client: 'PinterestSDKClient' = None, **kwargs) → None
```

Initialize a Board object. 



**Args:**
 
 - <b>`board_id`</b> (str):  Unique identifier of a board. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Uses the default client, if not provided. 


---

#### <kbd>property</kbd> description





---

#### <kbd>property</kbd> id





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> owner





---

#### <kbd>property</kbd> privacy







---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L253"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create`

```python
create(
    name: 'str',
    description: 'str' = None,
    privacy: 'str' = 'PUBLIC',
    client: 'PinterestSDKClient' = None,
    **kwargs
) → Board
```

Create a board owned by the "operation user_account". 


- By default, the "operation user_account" is the token user_account. 



**Args:**
 
 - <b>`name`</b> (str):  Board name. 
 - <b>`description`</b> (str, optional):  Board description. Defaults to None. 
 - <b>`privacy`</b> (str, optional):  Enum: `"PUBLIC"`, `"PROTECTED"`, `"SECRET"`. Defaults to "PUBLIC". 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object, uses the default client, if not provided. 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`Board`</b>:  Board object 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L425"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_section`

```python
create_section(name: 'str') → BoardSection
```

Create a board section on a board owned by the "operation user_account" - or on a group board that has been shared with this account. 


- By default, the "operation user_account" is the token user_account. 



**Args:**
 
 - <b>`name`</b> (str):  Name for the board section. 



**Returns:**
 
 - <b>`BoardSection`</b>:  The created board section. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L295"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `delete`

```python
delete(board_id: 'str', client: 'PinterestSDKClient' = None) → bool
```

Delete a board owned by the "operation user_account". 


- By default, the "operation user_account" is the token user_account. 



**Args:**
 
 - <b>`board_id`</b> (str):  Unique identifier of a board. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object. Uses the default client, if not provided. 



**Returns:**
 
 - <b>`bool`</b>:  If the board was deleted successfully. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L465"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_section`

```python
delete_section(section_id: 'str') → None
```

Delete a board section on a board owned by the "operation user_account" - or on a group board that has been shared with this account. 


- By default, the "operation user_account" is the token user_account. 



**Args:**
 
 - <b>`section_id`</b> (str):  Unique identifier of a board section. 



**Returns:**
 None 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L323"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get_all`

```python
get_all(
    privacy: 'str' = None,
    page_size: 'int' = None,
    bookmark: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → tuple[list[Board], Bookmark]
```

Get a list of the boards owned by the "operation user_account" + group boards where this account is a collaborator 

Optional: Specify a privacy type (public, protected, or secret) to indicate which boards to return. 


- If no privacy is specified, all boards that can be returned (based on the scopes of the token and ad_account role if applicable) will be returned. 





**Args:**
 
 - <b>`privacy`</b> (str, optional):   Enum: `"PUBLIC"`, `"PROTECTED"`, `"SECRET"`. Defaults to "PUBLIC". 
 - <b>`page_size`</b> (int[1..100], optional):  Maximum number of items to include in a single page of the response.  See documentation on Pagination for more information. Defaults to None which will  return default page size campaigns. 
 - <b>`bookmark`</b> (str, optional):  Cursor used to fetch the next page of items. Defaults to None. 
 - <b>`client`</b> (PinterestSDKClient, optional):  _description_. Defaults to None. 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`list[Board]`</b>:  List of Board Objects 
 - <b>`Bookmark`</b>:  Bookmark for pagination if present, else None. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L518"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_pins`

```python
list_pins(
    section_id: 'str' = None,
    page_size: 'int' = None,
    bookmark: 'str' = None,
    **kwargs
) → tuple[list[Pin], Bookmark]
```

Get a list of the Pins on a board owned by the "operation user_account" - or on a group board that has been shared with this account. 


- By default, the "operation user_account" is the token user_account. 



**Args:**
 
 - <b>`section_id`</b> (str, optional):  Unique identifier of a board section. If not passed in, all pins under  the board will be listed. 
 - <b>`page_size`</b> (int[1..100], optional):  Maximum number of items to include in a single page of the response.  See documentation on Pagination for more information. Defaults to None which will  return default page size campaigns. 
 - <b>`bookmark`</b> (str, optional):  Cursor used to fetch the next page of items. Defaults to None. 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`list[Pin]`</b>:  List of Pin Objects 
 - <b>`Bookmark`</b>:  Bookmark for pagination if present, else None. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L484"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_sections`

```python
list_sections(
    page_size: 'int' = None,
    bookmark: 'str' = None,
    **kwargs
) → tuple[list[BoardSection], Bookmark]
```

Get a list of all board sections from a board owned by the "operation user_account" - or a group board that has been shared with this account. 

By default, the "operation user_account" is the token user_account. 





**Args:**
 
 - <b>`page_size`</b> (int[1..100], optional):  Maximum number of items to include in a single page of the response.  See documentation on Pagination for more information. Defaults to None which will  return default page size campaigns. 
 - <b>`bookmark`</b> (str, optional):  Cursor used to fetch the next page of items. Defaults to None. 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`list[BoardSection]`</b>:  List of BoardSection Objects 
 - <b>`Bookmark`</b>:  Bookmark for pagination if present, else None. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L407"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `make_public`

```python
make_public() → bool
```

Change the privacy of the board to `PUBLIC`. 



**Returns:**
 
 - <b>`bool`</b>:  If the board was successfully made public. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L416"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `make_secret`

```python
make_secret() → bool
```

Change the privacy of the board to `SECRET`. 



**Returns:**
 
 - <b>`bool`</b>:  If the board was successfully made secret. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L380"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_fields`

```python
update_fields(**kwargs) → bool
```

Update the board fields using any attributes. 

Keyword Args:  Any valid campaign fields with valid values 



**Returns:**
 
 - <b>`bool`</b>:  If board fields were successfully updated 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/organic/boards.py#L444"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_section`

```python
update_section(section_id: 'str', name: 'str') → BoardSection
```

Update a board section on a board owned by the "operation user_account" - or on a group board that has been shared with this account. 


- By default, the "operation user_account" is the token user_account. 



**Args:**
 
 - <b>`section_id`</b> (str):  Unique identifier of a board section. 
 - <b>`name`</b> (str):  Name for the board section. 



**Returns:**
 
 - <b>`BoardSection`</b>:  The created board section. 


