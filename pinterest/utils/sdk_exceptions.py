"""
SDK Exceptions for error handling in the models.
"""

class SdkException(Exception):
    """Raises an exception for Model's Errors"""
    def __init__(self, status=None, reason=None, http_resp=None, body=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = body
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = f"({self.status})\n"\
                        f"Reason: {self.reason}\n"
        if self.headers:
            error_message += f"HTTP response headers: {self.headers}\n"

        if self.body:
            error_message += f"HTTP response body: {self.body}\n"
        return error_message
