<!-- markdownlint-disable -->

# API Overview

## Modules

- [`ads`](./ads.md#module-ads)
- [`ads.ad_accounts`](./ads.ad_accounts.md#module-adsad_accounts): AdAccount Class for Pinterest Python SDK
- [`ads.ad_groups`](./ads.ad_groups.md#module-adsad_groups): High level module class for AdGroup object
- [`ads.ads`](./ads.ads.md#module-adsads): Ads high level model
- [`ads.audiences`](./ads.audiences.md#module-adsaudiences): High level module class for Audience object
- [`ads.campaigns`](./ads.campaigns.md#module-adscampaigns): Campaign Class for Pinterest Python SDK
- [`ads.conversion_events`](./ads.conversion_events.md#module-adsconversion_events): Conversion Event Class for Pinterest Python SDK
- [`ads.conversion_tags`](./ads.conversion_tags.md#module-adsconversion_tags): Conversion Class for Pinterest Python SDK
- [`ads.customer_lists`](./ads.customer_lists.md#module-adscustomer_lists): High level module class for Customer List object
- [`ads.keywords`](./ads.keywords.md#module-adskeywords): High level module class for Keyword object
- [`client`](./client.md#module-client): Pinterest Client
- [`organic`](./organic.md#module-organic)
- [`organic.boards`](./organic.boards.md#module-organicboards): Board Class for Pinterest Python SDK
- [`organic.pins`](./organic.pins.md#module-organicpins): Pin Class for Pinterest Python SDK
- [`utils`](./utils.md#module-utils)
- [`utils.base_model`](./utils.base_model.md#module-utilsbase_model): Pinterest Base Model
- [`utils.bookmark`](./utils.bookmark.md#module-utilsbookmark): Bookmark Model
- [`utils.error_handling`](./utils.error_handling.md#module-utilserror_handling): Util error handling function
- [`utils.load_json_config`](./utils.load_json_config.md#module-utilsload_json_config): module with the function `load_json_config` that parse a config.json file and then load all the variables found as
- [`utils.refresh_access_token`](./utils.refresh_access_token.md#module-utilsrefresh_access_token): This script has functions for generating a new ACCESSTOKEN using the REFRESHTOKEN
- [`utils.sdk_exceptions`](./utils.sdk_exceptions.md#module-utilssdk_exceptions): SDK Exceptions for error handling in the models.

## Classes

- [`ad_accounts.AdAccount`](./ads.ad_accounts.md#class-adaccount): Ad Account model used to create, update its attributes and list its different entities.
- [`ad_groups.AdGroup`](./ads.ad_groups.md#class-adgroup): AdGroup model used to view, create, update its attributes and list its different entities.
- [`ads.Ad`](./ads.ads.md#class-ad): Ad model used to view, create, update its attributes
- [`audiences.Audience`](./ads.audiences.md#class-audience): High level model class to manage audiences for an AdAccount
- [`campaigns.Campaign`](./ads.campaigns.md#class-campaign): Campaign model used to view, create, update its attributes and list its different entities.
- [`conversion_events.Conversion`](./ads.conversion_events.md#class-conversion): Conversion Event Model used to send conversion events to Pinterest API
- [`conversion_tags.ConversionTag`](./ads.conversion_tags.md#class-conversiontag): Conversion Tag model used to view, create, update its attributes and list its different entities
- [`customer_lists.CustomerList`](./ads.customer_lists.md#class-customerlist): High level model class to manage customer_lists for an CustomerList
- [`keywords.Keyword`](./ads.keywords.md#class-keyword): High level model class to manage keywords
- [`client.PinterestSDKClient`](./client.md#class-pinterestsdkclient): Wrapper API client for SDK high level models
- [`boards.Board`](./organic.boards.md#class-board): Board model used to view, create, update its attributes and list its different entities.
- [`boards.BoardSection`](./organic.boards.md#class-boardsection): Board Section model used as a helper model for `BOARD`
- [`pins.Pin`](./organic.pins.md#class-pin): Pin model used to view, create, update its attributes and list its different entities.
- [`base_model.PinterestBaseModel`](./utils.base_model.md#class-pinterestbasemodel): Base Model for all other Higher Level Models in the Python Client
- [`bookmark.Bookmark`](./utils.bookmark.md#class-bookmark): Bookmark Model used as a utilty to improve pagination experience for user.
- [`sdk_exceptions.SdkException`](./utils.sdk_exceptions.md#class-sdkexception): Raises an exception for Model's Errors

## Functions

- [`error_handling.verify_api_response`](./utils.error_handling.md#function-verify_api_response): Verify that there are no errors in `response` received from api
- [`load_json_config.load_json_config`](./utils.load_json_config.md#function-load_json_config): Parse a config.json file and then load all the variables found as environment variables.
- [`load_json_config.load_json_config_from_single_env_var`](./utils.load_json_config.md#function-load_json_config_from_single_env_var): Parse PINTEREST_JSON_ENV_VARIABLES environment variable to split long JSON string into
- [`refresh_access_token.get_new_access_token`](./utils.refresh_access_token.md#function-get_new_access_token): Function used to retrieve a new access token for a user using the refresh token.
