<!-- markdownlint-disable -->

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/utils/bookmark.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `utils.bookmark`
Bookmark Model 



---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/utils/bookmark.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Bookmark`
Bookmark Model used as a utilty to improve pagination experience for user. 

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/utils/bookmark.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    bookmark_token: 'str',
    model: 'object',
    model_fn: 'str',
    model_fn_args: 'dict',
    client: 'PinterestSDKClient'
)
```

Initialize a Bookmark object. 



**Args:**
 
 - <b>`bookmark_token`</b> (str):  Bookmark pagination token. 
 - <b>`model`</b> (PinterestBaseModel):  The SDK Model where function was called. 
 - <b>`model_fn`</b> (str):  The model's function which returns a bookmark. 
 - <b>`model_fn_args`</b> (dict):  Arguments passed to the function. 
 - <b>`client`</b> (PinterestSDKClient):  Client used to make the SDK call. 




---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/utils/bookmark.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_bookmark_token`

```python
get_bookmark_token() → str
```

Returns the bookmark pagination token in string format. 



**Returns:**
 
 - <b>`str`</b>:  pagination or continuatiuon token 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/utils/bookmark.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_next`

```python
get_next() → tuple[list[object], Bookmark]
```

Function used to get the next page of items using Bookmark Pagination Token. 



**Returns:**
 
 - <b>`list[PinterestBaseModel]`</b>:  List of SDK Model Objects 
 - <b>`Bookmark`</b>:  Bookmark Object for pagination if present, else None. 


