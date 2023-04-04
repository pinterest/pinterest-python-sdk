"""
Bookmark Model
"""
from __future__ import annotations

from pinterest.client import PinterestSDKClient

class Bookmark:
    """
    Bookmark Model used as a utilty to improve pagination experience for user.
    """
    def __init__(
        self,
        bookmark_token:str,
        model:object,
        model_fn:str,
        model_fn_args:dict,
        client:PinterestSDKClient
        ):
        # pylint: disable=too-many-arguments
        """
        Initialize a Bookmark object.

        Args:
            bookmark_token (str): Bookmark pagination token.
            model (PinterestBaseModel): The SDK Model where function was called.
            model_fn (str): The model's function which returns a bookmark.
            model_fn_args (dict): Arguments passed to the function.
            client (PinterestSDKClient): Client used to make the SDK call.
        """
        self.bookmark_token = bookmark_token
        self.model = model
        self.model_fn = model_fn
        self.model_fn_args = model_fn_args
        self.client = client

    def get_next(self) -> tuple[list[object], Bookmark]:
        """
        Function used to get the next page of items using Bookmark Pagination Token.

        Returns:
            list[PinterestBaseModel]: List of SDK Model Objects
            Bookmark: Bookmark Object for pagination if present, else None.
        """
        self.model_fn_args['bookmark'] = self.bookmark_token
        if self.client:
            self.model_fn_args['client'] = self.client
        if 'kwargs' in self.model_fn_args:
            kwargs = self.model_fn_args.get('kwargs')
            del self.model_fn_args['kwargs']
            self.model_fn_args.update(kwargs)
        return getattr(self.model, self.model_fn)(**self.model_fn_args)

    def get_bookmark_token(self) -> str:
        """
        Returns the bookmark pagination token in string format.

        Returns:
            str: pagination or continuatiuon token
        """
        return self.bookmark_token
