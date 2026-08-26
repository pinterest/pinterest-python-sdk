"""
Util error handling function
"""
from pinterest.utils.sdk_exceptions import SdkException


def _get_field(obj, field):
    """
    Read `field` off either a raw dict response or a generated model object
    """
    if isinstance(obj, dict):
        return obj.get(field)
    return getattr(obj, field, None)


def _get_first_exception(response):
    """
    Return the first exception reported in `response`, or None if there is none.

    Bulk endpoints return one element per requested entity. Depending on the endpoint that
    element's `exceptions` field is either a list of exceptions (campaigns, ad groups) or a
    single exception object (ads).
    """
    items = _get_field(response, 'items')
    if not items:
        return None

    exceptions = _get_field(items[0], 'exceptions')
    if not exceptions:
        return None

    if isinstance(exceptions, list):
        return exceptions[0]
    return exceptions


def verify_api_response(response) -> bool:
    """
    Verify that there are no errors in `response` received from api

    Args:
        response: Response received from api request

    Returns:
        bool: If the `response` is without any exceptions
    """
    exception = _get_first_exception(response)
    if exception is None:
        return True

    code = _get_field(exception, 'code')
    message = _get_field(exception, 'message')
    if code and message:
        raise SdkException(
            status=f"Failed with code {code}",
            reason=message,
        )

    return True
