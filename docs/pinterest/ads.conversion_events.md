<!-- markdownlint-disable -->

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/conversion_events.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `ads.conversion_events`
Conversion Event Class for Pinterest Python SDK 



---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/conversion_events.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Conversion`
Conversion Event Model used to send conversion events to Pinterest API 




---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/conversion_events.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create_conversion_event`

```python
create_conversion_event(
    event_name: 'str',
    action_source: 'str',
    event_time: 'int',
    event_id: 'str',
    user_data: 'dict',
    custom_data: 'dict',
    event_source_url: 'str' = None,
    partner_name: 'str' = None,
    app_id: 'str' = None,
    app_name: 'str' = None,
    app_version: 'str' = None,
    device_brand: 'str' = None,
    device_carrier: 'str' = None,
    device_model: 'str' = None,
    device_type: 'str' = None,
    os_version: 'str' = None,
    language: 'str' = None,
    **kwargs
) → ConversionEventsData
```

Create Conversion Event Data to be sent. 



**Args:**
 
 - <b>`event_name`</b> (str):  The type of the user event, Enum: "add_to_cart", "checkout", "custom",  "lead", "page_visit", "search", "signup", "view_category", "watch_video" 
 - <b>`action_source`</b> (str):  The source indicating where the conversion event occurred, Enum:  "app_adroid", "app_ios", "web", "offline" 
 - <b>`event_time`</b> (int):  The time when the event happened. Unix timestamp in seconds 
 - <b>`event_id`</b> (str):  The unique id string that identifies this event and can be used for deduping  between events ingested via both the conversion API and Pinterest tracking 
 - <b>`user_data`</b> (dict):  Object containing customer information data. Note, it is required at least  one of 1) em, 2) hashed_maids or 3) pair client_ip_address + client_user_agent. 
 - <b>`custom_data`</b> (dict):  Object containing other custom data. 
 - <b>`event_source_url`</b> (str, optional):  URL of the web conversion event 
 - <b>`partner_name`</b> (str, optional):  The third party partner name responsible to send the event to  Conversion API on behalf of the adverstiser. Only send this field if Pinterest has worked  directly with you to define a value for partner_name. 
 - <b>`app_id`</b> (str, optional):  The app store app ID. 
 - <b>`app_name`</b> (str, optional):  Name of the app. 
 - <b>`app_version`</b> (str, optional):  Version of the app. 
 - <b>`device_brand`</b> (str, optional):  Brand of the user device. 
 - <b>`device_carrier`</b> (str, optional):  User device's model carrier. 
 - <b>`device_model`</b> (str, optional):  Model of the user device. 
 - <b>`device_type`</b> (str, optional):  Type of the user device. 
 - <b>`os_version`</b> (str, optional):  Version of the device operating system. 
 - <b>`language`</b> (str, optional):  Two-character ISO-639-1 language code indicating the user's language. 



**Returns:**
 
 - <b>`ConversionEventsData`</b>:  ConversionEventData to be sent 

---

<a href="https://github.com/pinterest/pinterest-python-sdk/blob/main/pinterest/ads/conversion_events.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `send_conversion_events`

```python
send_conversion_events(
    ad_account_id: 'str',
    conversion_events: 'list[ConversionEventsData]',
    test: 'bool' = False,
    client: 'PinterestSDKClient' = None,
    **kwargs
) → tuple(int, int, list[ConversionApiResponseEvents])
```

Send conversion events to Pinterest API for Conversions. 

Note: Highly recommend to use create_client_with_token (with Conversion Access Token) to create different client for this functionality. 


