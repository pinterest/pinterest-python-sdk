# Pinterest SDK for Python
[![build](https://github.com/pinterest/pinterest-python-sdk/actions/workflows/build.yml/badge.svg)](https://github.com/pinterest/pinterest-python-sdk/actions/workflows/build.yml)

### Introduction

The Pinterest SDK currently offers a Python library that supports campaign management and simplifies authentication and error handling. We will be adding functionality supporting organic Pins, shopping, analytics, and more over time. If you have specific feedback about the SDK or requests for additional functionality, please [let us know](https://docs.google.com/forms/d/e/1FAIpQLSf2bA8gyC7kCp_Mgt1jCOvgp22K2EQWg3SEcMxyVRVzddYeMw/viewform?usp=sf_link).

## Pre-requisites
  * Python 3.7+
  * a registered application (see below)
  * an access token (see below)

### Register an App

In order to use the SDK, you must have registered an app on [developers.pinterest.com](https://developers.pinterest.com)

The steps to create an app can be found in the [Set up app](https://developers.pinterest.com/docs/getting-started/set-up-app/) section of the [docs](https://developers.pinterest.com/docs/) on the [Developers' Site](https://developers.pinterest.com/).

### Get Access Token

Follow the instructions outlined on the Pinterest Developer Platform's [Authentication](https://developers.pinterest.com/docs/getting-started/authentication/) Section to retreive an **Access Token** and **Refresh Token**

## Install package

**NOTE**: For Python3, use ``python3`` and ``pip3`` instead.

**NOTE**: If the commands below result in a permissions error (which may happen if you are using a system-installed Python), use ``sudo``.

To install pip, please refer to [pip installation guide](https://pip.pypa.io/en/stable/installation/).

[_Recommended_] Create a virtual environment:

```bash
# Create environment
$ python -m venv .venv

# Activate environment
$ source .venv/bin/activate

```

Install SDK:

```bash
$ pip install pinterest-api-sdk
```

Alternatively, you can check out the repository from GitHub. Once the package is downloaded and unzipped, install it:

```bash
$ python setup.py install
```

You can now use the SDK.

## Getting Started

For use the client you need set basic variables for that you have two option setup environment variables (using a 
.env file or set in your OS) or create a config.json.

### Setting up environment variables

To configure the client using environment variables, you must create a **.env** file using [.env.example](.env.example)
as a template. For basic configuration and usage you need to set the following environment variables in the **.env** file:

```
PINTEREST_APP_ID=<app id>
PINTEREST_APP_SECRET=<app secret>
PINTEREST_REFRESH_ACCESS_TOKEN='<refresh token>'

**or**

PINTEREST_ACCESS_TOKEN='<access token>'
```

Once you have established the environment variables, the client will be instantiated for you automatically.

**NOTE**: 
 * Setting the `PINTEREST_ACCESS_TOKEN` (which is valid for thirty days) will require the token value to be replaced when it expires. You will need to manually reinsantiate the client when the **access_token** expires. 
 * Setting the `PINTEREST_REFRESH_ACCESS_TOKEN` (which is valid for a year) will allow the SDK to regenerate the new access token whenever it is required. 

### Setting up config.json

To configure the client using config.json, you must create a **config.json** file using [config.json.example](config.json.example)
as a template. For basic configuration and usage you need to set the following key in the **config.json** file:

```json
{
  "app_id": "<app id>",
  "app_secret": "<app secret>",
  "refresh_access_token": "<refresh token>"
}
```

**or**

```json
{
  "access_token": "<access token>"
}
```

Once you have established the keys, the client will be instantiated for you automatically. 

**NOTE**: 
 * Setting up environment variables and config.json will result in the environment variables overriding the keys in config.json
 * Setting the `access_token` (which is valid for thirty days) will require the token value to be replaced when it expires. You will need to manually reinsantiate the client when the **access_token** expires. 
 * Setting the `refresh_access_token` (which is valid for a year) will allow the SDK to regenerate the new access token whenever it is required. 

For more information visit the [Authentication](https://developers.pinterest.com/docs/getting-started/authentication/#Refreshing%20an%20access%20token) page.

## Samples

### Initializing Models

**Use Case**: 

* Initialize a Campaign object using an existing Ad Account ID and Campaign ID.

```python
from pinterest.ads.campaigns import Campaign

campaign = Campaign(
    ad_account_id="123456789",
    campaign_id="987654321",
)
```

### Examples of Campaign Management using SDK

**Use Case**:

* Create a new Ad
* Assign the Ad to an existing Ad Group
* Activate the Ad Group's parent Campaign
* Change the Campaign's budget

```python
from pinterest.ads.campaigns import Campaign
from pinterest.ads.ad_groups import AdGroup
from pinterest.ads.ads import Ad

## Create a new Ad
new_ad = Ad.create(
    ad_account_id="123456789",
    ad_group_id="999999999",
    creative_type="REGULAR",
    pin_id="111111111",
    name="SDK Example Ad",
    status="ACTIVE",
    is_pin_deleted=False,
    is_removable=False,
)

## Initialize existing paused Campaign
campaign = Campaign(
    ad_account_id="123456789",
    campaign_id="987654321",
)

## Activate campaign
getattr(campaign, '_status')
>>> 'PAUSED'

campaign.activate()
>>> True

getattr(campaign, '_status')
>>> 'ACTIVE'

## Change campaign's lifetime budget
campaign.set_lifetime_budget(
    new_spend_cap=250000000
)
>>> True
```

**Note**: More examples of usage are located in the ``examples/`` folder.

## Documentation

* Documentation is hosted on [Developer Site](https://developers.pinterest.com/docs/sdk/).


## Exceptions

See `pinterest.utils.sdk_exceptions` for a list of exceptions which may be thrown by the SDK.

## Debugging

If the SDK is not working as expected there might be an issue with the SDK or the Pinterest API server itself. In order to debug and identify the issue, the environment variables for debugging and logging can be enabled.

```bash
PINTEREST_DEBUG = True
PINTEREST_LOG_FILE = /tmp/log.txt
PINTEREST_LOGGER_FORMAT = '%(asctime)s %(levelname)s %(message)s'
```

When `PINTEREST_DEBUG` is enabled, all the API raw requests and responses will be printed to the console and to the log file in the requested format.

## Issues

For any issues or questions related to the SDK you are welcome to submit them through [GitHub Issues](https://github.com/pinterest/pinterest-python-sdk/issues) using the following templates:
  * [Bug Report Template](https://github.com/pinterest/pinterest-python-sdk/blob/main/.github/ISSUE_TEMPLATE/bug_report.md)
  * [Feature Request Template](https://github.com/pinterest/pinterest-python-sdk/blob/main/.github/ISSUE_TEMPLATE/feature_request.md)

**Note**: There is no guaranteed SLA for responding to or resolving issues.

For any general issues related to the Pinterest API (or other Pinterest products) you can contact support at [help.pinterest.com](https://help.pinterest.com)

## Other Resources

Additional information on the Pinterest SDK can be found [here](https://developers.pinterest.com/docs/sdk/intro/).
Additional information about campaigns and campaign management can be found in:
  * The [ads management](https://developers.pinterest.com/docs/features/ads-management/) section of the API documentation
  * The [campaign structure](https://help.pinterest.com/en/business/article/campaign-structure) help article
  * The [create and edit a campaign](https://help.pinterest.com/en/business/article/set-up-your-campaign) help article
  * The [campaign objectives](https://help.pinterest.com/en/business/article/campaign-objectives) help article
  * The [campaign budgets](https://help.pinterest.com/en/business/article/set-up-campaign-budgets) help article

## Advanced Options

### Importing the PinterestSDKClient

In order to access or use the client you can import the *PinterestSDKClient* and call the `create_default_client()` classmethod:

```python
from pinterest.client import PinterestSDKClient
default_client = PinterestSDKClient.create_default_client()
```

This will allow you to use the SDK Models without passing a **PinterestSDKClient** Object.

### Creating custom Pinterest SDK Clients

In order to create an object of the [**PinterestSDKClient**](./pinterest/client/__init__.py) you need to pass the access token inside the python code every time you wish to create a client or a combination of the refresh token, app id and app secret. This option is more useful if you wish to work with multiple accounts or clients at the same time.

```python
from pinterest.client import PinterestSDKClient

# Access Token for Client 1
pinterest_access_token_1 = <access token 1>

# Refresh Token for Client 2
pinterest_refresh_token_2 = <refresh token 2>
pinterest_app_id_2 = <app id 2>
pinterest_app_secret_2 = <app secret 2>

client_1 = PinterestSDKClient.create_client_with_token(
    access_token=pinterest_access_token_1,
)
client_2 = PinterestSDKClient.create_client_with_refresh_token(
    refresh_token=pinterest_access_token_2,
    app_id=pinterest_app_id_2,
    app_secret=pinterest_app_secret_2,
)
```

## License

Pinterest Python SDK is licensed under the [LICENSE](https://github.com/pinterest/pinterest-python-sdk/blob/main/LICENSE) file in the root directory of this source tree.
