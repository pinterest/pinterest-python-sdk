"""
Util error handling function
"""
from pinterest.utils.sdk_exceptions import SdkException

def verify_api_response(response) -> bool:
    # pylint: disable=too-many-boolean-expressions
    """
    Verify that there are no errors in `response` received from api

    Args:
        response: Response received from api request

    Returns:
        bool: If the `response` is without any exceptions
    """
    if isinstance(response, dict):
        if (
                response.get('items')
                and len(response.get('items')) > 0
                and response.get('items')[0].get('exceptions')
                and isinstance(response.get('items')[0].get('exceptions'), list)
                and len(response.get('items')[0].get('exceptions')) > 0
                and response.get('items')[0].get('exceptions')[0].get('code')
                and response.get('items')[0].get('exceptions')[0].get('message')
        ):  # pylint: disable-msg=too-many-boolean-expressions
            raise SdkException(
                status=f"Failed with code {response.get('items')[0].get('exceptions')[0].get('code')}",
                reason=response.get('items')[0].get('exceptions')[0].get('message')
            )
    else:
        if (
                hasattr(response, "items")
                and response.items
                and len(response.items) > 0
                and hasattr(response.items[0], "exceptions")
                and response.items[0].exceptions
                and isinstance(response.items[0].exceptions, list)
                and len(response.items[0].exceptions) > 0
                and hasattr(response.items[0].exceptions[0], "code")
                and response.items[0].exceptions[0].code
                and hasattr(response.items[0].exceptions[0], "message")
                and response.items[0].exceptions[0].message
        ):
            raise SdkException(
                status=f"Failed with code {response.items[0].exceptions[0].code}",
                reason=response.items[0].exceptions[0].message
            )
    return True
