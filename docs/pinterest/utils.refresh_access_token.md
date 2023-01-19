<!-- markdownlint-disable -->

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/utils/refresh_access_token.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `utils.refresh_access_token`
This script has functions for generating a new ACCESSTOKEN using the REFRESHTOKEN 


---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/utils/refresh_access_token.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_new_access_token`

```python
get_new_access_token(
    app_id: str,
    app_secret: str,
    refresh_access_token: str,
    host: str
) → str
```

Function used to retrieve a new access token for a user using the refresh token. 

**Args:**
 
 - <b>`app_id`</b> (str):  APP_ID or CLIENT_ID 
 - <b>`app_secret`</b> (str):  APP_SECRET 
 - <b>`refresh_access_token`</b> (str):  Refresh access token retrieved from oauth. 
 - <b>`host`</b> (str):  base url of the host 

**Returns:**
 
 - <b>`str`</b>:  New access token 


