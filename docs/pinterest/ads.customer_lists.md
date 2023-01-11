<!-- markdownlint-disable -->

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/customer_lists.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ads.customer_lists`
High level module class for Customer List object 



---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/customer_lists.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CustomerList`
High level model class to manage customer_lists for an CustomerList 

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/customer_lists.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(ad_account_id, customer_list_id, client=None, **kwargs)
```






---

#### <kbd>property</kbd> ad_account_id





---

#### <kbd>property</kbd> created_time





---

#### <kbd>property</kbd> exceptions





---

#### <kbd>property</kbd> id





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> num_batches





---

#### <kbd>property</kbd> num_removed_user_records





---

#### <kbd>property</kbd> num_uploaded_user_records





---

#### <kbd>property</kbd> status





---

#### <kbd>property</kbd> type





---

#### <kbd>property</kbd> updated_time







---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/customer_lists.py#L245"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_record`

```python
add_record(record)
```

Add records to an existing customer list, the system scans the additions for existing Pinterest accounts; those are the records that will be added to your “CUSTOMER_LIST” audience. 

Your original list of records to add will be deleted when the matching process is complete. 



**Args:**
 
 - <b>`record`</b> (str):  Records list. Can be any combination of emails, MAIDs, or IDFAs. Emails must be lowercase and can be plain text or hashed using SHA1, SHA256, or MD5. MAIDs and IDFAs must be hashed with SHA1, SHA256, or MD5. 



**Returns:**
 
 - <b>`bool`</b>:  If record was added to the customer list fields were successfully updated 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/customer_lists.py#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create`

```python
create(
    ad_account_id: 'str',
    name: 'str',
    records: 'str',
    list_type: 'str' = 'EMAIL',
    client: 'PinterestSDKClient' = None,
    **kwargs
)
```

Create a customer list from your records(hashed or plain-text email addresses, or hashed MAIDs or IDFAs). 

A customer list is one of the four types of Pinterest audiences: for more information, see <a href="https://help.pinterest.com/en/business/article/audience-targeting">Audience targeting</a> or the <a href="https://developers.pinterest.com/docs/features/ads-management/#Audiences">Audiences</a> section of the ads management guide. 

Please review our <a href="https://help.pinterest.com/en/business/article/audience-targeting#section-13341">requirements</a> for what type of information is allowed when uploading a customer list. 

When you create a customer list, the system scans the list for existing Pinterest accounts; the list must include at least 100 Pinterest accounts. Your original list will be deleted when the matching process is complete. The filtered list – containing only the Pinterest accounts that were included in your starting list – is what will be used to create the audience. 

Note that once you have created your customer list, you must convert it into an audience (of the “CUSTOMER_LIST” type) using the <a href="https://developers.pinterest.com/docs/api/v5/#operation/create_audience_handler">create audience endpoint</a> before it can be used. 





**Args:**
 
 - <b>`ad_account_id`</b> (str):  Unique identifier of an ad account. 
 - <b>`name`</b> (str):  Customer list name. 
 - <b>`records`</b> (str):  Records list. Can be any combination of emails, MAIDs, or IDFAs. Emails must be lowercase  and can be plain text or hashed using SHA1, SHA256, or MD5. MAIDs and IDFAs must be hashed with SHA1, SHA256, or MD5. 
 - <b>`list_type`</b> (str, optional):  User list type. Possible Enum: "EMAIL" "IDFA" "MAID" "LR_ID" "DLX_ID" "HASHED_PINNER_ID". Defaults to "EMAIL". 
 - <b>`client`</b> (PinterestSDKClient, optional):  Defaults to default_api_client. 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`CustomerList`</b>:  CustomerList object 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/customer_lists.py#L192"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `get_all`

```python
get_all(
    ad_account_id: 'str',
    page_size: 'int' = None,
    order: 'str' = None,
    bookmark: 'str' = None,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → tuple[list[CustomerList], Bookmark]
```

Get a list of the customer lists in the AdAccount, filtered by the specified arguments 



**Args:**
 
 - <b>`ad_account_id`</b> (str):  Campaign's Ad Account ID. 
 - <b>`page_size`</b> (int, optional):  Maximum number of items to include in a single page of the response.  See documentation on Pagination for more information. Defaults to None which will  return default page size customer lists. 
 - <b>`order`</b> (str, optional):  _description_. Defaults to None. 
 - <b>`bookmark`</b> (str, optional):  Cursor used to fetch the next page of items. Defaults to None. 
 - <b>`client`</b> (PinterestSDKClient, optional):  PinterestSDKClient Object 

Keyword Args: Any valid keyword arguments or query parameters for endpoint. 



**Returns:**
 
 - <b>`list[CustomerList]`</b>:  List of CustomerList Objects 
 - <b>`Bookmark`</b>:  Bookmark for pagination if present, else None. 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/customer_lists.py#L266"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `remove_record`

```python
remove_record(record)
```

Remove records to an existing customer list. 



**Args:**
 
 - <b>`record`</b> (str):  Records list. Can be any combination of emails, MAIDs, or IDFAs. Emails must be lowercase and can be plain text or hashed using SHA1, SHA256, or MD5. MAIDs and IDFAs must be hashed with SHA1, SHA256, or MD5. 



**Returns:**
 
 - <b>`bool`</b>:  If record was removed to the customer list fields were successfully updated 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/docs/pinterest/ads/customer_lists.py#L171"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_fields`

```python
update_fields(**kwargs)
```

Update customer lists fields with valid values 

Keywords Args:  Any valid customer list field with valid value 


