"""
This script has functions for generating a new ACCESSTOKEN using the REFRESHTOKEN
"""

from base64 import b64encode
import json
import urllib3

from pinterest.utils.sdk_exceptions import SdkException


def get_new_access_token(
    app_id: str,
    app_secret: str,
    refresh_access_token: str,
    host: str,
    ) -> str:
    """
    Function used to retrieve a new access token for a user using the refresh token.
    Args:
        app_id (str): APP_ID or CLIENT_ID
        app_secret (str): APP_SECRET
        refresh_access_token (str): Refresh access token retrieved from oauth.
        host (str): base url of the host
    Returns:
        str: New access token
    """
    refresh_auth_token = b64encode(
    s=(f"{app_id}:{app_secret}").encode()
    ).decode("utf-8")

    headers = {
        'Authorization': f'Basic {refresh_auth_token}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = f'grant_type=refresh_token&refresh_token={refresh_access_token}'

    response = urllib3.PoolManager().request(
        method='POST',
        url=f'{host}/oauth/token',
        headers=headers,
        body=data,
        timeout=5
    )
    if response.status == 401:
        raise SdkException(
            status=response.status,
            reason=response.reason,
            body="Authentication error. " +
            "Kindly check if the following variables are correct: [PINTEREST_ACCESS_TOKEN] or " +
            "[PINTEREST_APP_ID, PINTEREST_APP_SECRET, PINTEREST_REFRESH_ACCESS_TOKEN]. " +
            f"Response from server: {response.data}",
            http_resp=response
            )
    if response.status != 200:
        raise SdkException(http_resp=response)

    data = json.loads(response.data)

    if not data.get('access_token'):
        raise KeyError(f"`access_token` not found in response body. response={data}."+
            "Kindly check input arguments or update PINTEREST_REFRESH_TOKEN")

    return data.get('access_token')
