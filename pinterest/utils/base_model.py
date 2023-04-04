"""
Pinterest Base Model
"""
from typing import Callable

from openapi_generated.pinterest_client.exceptions import ApiTypeError

from pinterest.client import PinterestSDKClient

from pinterest.utils.error_handling import verify_api_response
from pinterest.utils.bookmark import Bookmark



class PinterestBaseModel:
    """
    Base Model for all other Higher Level Models in the Python Client
    """

    def __init__(
            self,
            _id: str,
            generated_api: object,
            generated_api_get_fn: str,
            generated_api_get_fn_args: dict,
            model_attribute_types: dict,
            client=None,
    ):
        # pylint: disable=too-many-arguments
        self._id = _id
        self._client = client
        if self._client is None:
            self._client = PinterestBaseModel._get_client()
        self._generated_api = generated_api(self._client)
        self._generated_api_get_fn = generated_api_get_fn
        self._generated_api_get_fn_args = generated_api_get_fn_args
        self._model_attribute_types = model_attribute_types

        self._property_dict = dict((k, getattr(self, k))
                        for k, v in self.__class__.__dict__.items()
                        if isinstance(v, property))

    def __str__(self):
        return f"{self.__class__.__name__} <{self._id}> Model: {self._property_dict}"

    def __repr__(self):
        args_string = ""
        for arg, arg_val in self._generated_api_get_fn_args.items():
            args_string += f"{arg}={arg_val}"
        return f"{self.__class__.__name__}({args_string})"

    def _populate_fields(self, **kwargs):
        """
        Populate all fields as model attributes
        """
        _model_data = kwargs.get('_model_data')
        if not _model_data:
            _model_data = getattr(
                self._generated_api,
                self._generated_api_get_fn
            )(**self._generated_api_get_fn_args).to_dict()

        for field in _model_data:
            if not self._model_attribute_types.get(field):
                continue

            if _model_data.get(field) is None:
                attribute_value = None
            else:
                try:
                    attribute_value = (self._model_attribute_types.get(field)[0])(_model_data.get(field))
                except ApiTypeError:
                    attribute_value = (self._model_attribute_types.get(field)[0])(**_model_data.get(field))
                except TypeError:
                    attribute_value = type(self._model_attribute_types.get(field)[0])(_model_data.get(field))

            setattr(
                self,
                f"_{field}",
                attribute_value
            )

    def __eq__(self, obj):
        return isinstance(self, type(obj)) and getattr(self, "id") == getattr(obj, "id")

    @classmethod
    def _get_client(cls, client = None):
        if not client:
            client = PinterestSDKClient.create_default_client()
        return client

    @classmethod
    def _get_api_instance(
        cls,
        api,
        client: PinterestSDKClient = None
    ):
        return api(api_client=cls._get_client(client))

    @classmethod
    def _call_method(
        cls,
        instance,
        function,
        params,
        **kwargs
    ):
        return getattr(instance, function)(**params, **kwargs)

    @classmethod
    def _list(
            cls,
            params: [any] = None,
            page_size: int = None,
            order: str = None,
            bookmark: str = None,
            api: type = None,
            list_fn: Callable = None,
            map_fn: Callable = None,
            bookmark_model_cls: object = None,
            bookmark_model_fn: Callable = None,
            client: PinterestSDKClient = None,
            **kwargs
    ):
        # pylint: disable=too-many-arguments

        if page_size:
            kwargs["page_size"] = page_size
        if order:
            kwargs["order"] = order
        if bookmark:
            kwargs["bookmark"] = bookmark

        items = []
        bookmark = None

        http_response = cls._call_method(
            cls._get_api_instance(api, client),
            list_fn.__name__,
            params,
            **kwargs
        )

        verify_api_response(http_response)

        items = http_response.get('items', [])
        bookmark = http_response.get('bookmark', None)

        # Set the new bookmark
        if bookmark is not None:
            kwargs["bookmark"] = bookmark

        if not bookmark_model_cls:
            kwargs.update(params)
        bookmark_model = Bookmark(
                bookmark_token=bookmark,
                model=cls if not bookmark_model_cls else bookmark_model_cls,
                model_fn='get_all' if not bookmark_model_fn else bookmark_model_fn.__name__,
                model_fn_args=kwargs,
                client=client if not bookmark_model_cls else None,
            ) if bookmark else None

        return [map_fn(item) for item in items], bookmark_model

    @classmethod
    def _create(
            cls,
            params: [any] = None,
            api: type = None,
            create_fn: Callable = None,
            map_fn: Callable = lambda x: x,
            client: PinterestSDKClient = None,
            **kwargs
    ):
        # pylint: disable=too-many-arguments, unused-argument
        http_response = cls._call_method(
            cls._get_api_instance(api, client),
            create_fn.__name__,
            params,
            **kwargs
        )
        verify_api_response(http_response)
        return map_fn(http_response)

    def _update(
            self,
            params: [any] = None,
            api: type = None,
            update_fn: Callable = None,
            map_fn: Callable = None,
            client: PinterestSDKClient = None,
            **kwargs
    ):
        # pylint: disable=too-many-arguments, protected-access
        http_response = self.__class__._call_method(
            self.__class__._get_api_instance(api, client),
            update_fn.__name__,
            params,
        )

        verify_api_response(http_response)

        if map_fn:
            self._populate_fields(_model_data=map_fn(http_response))
        else:
            self._populate_fields()

        for arg, value in kwargs.items():
            if getattr(self, f'_{arg}') != value:
                raise AssertionError(f"Expected {arg} is {value}"
                                     + f" Actual value is {getattr(self, f'_{arg}')}")

        return True
