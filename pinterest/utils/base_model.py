"""
Pinterest Base Model
"""
from pinterest.client import PinterestSDKClient
from pinterest.generated.client.exceptions import ApiTypeError


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

    def __getattr__(self, name):
        try:
            return self.__dict[name]
        except KeyError:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'") # pylint: disable=raise-missing-from

    def __str__(self):
        model_dict = self.__dict__.copy()
        del model_dict['_client']
        del model_dict['_generated_api']
        del model_dict['_generated_api_get_fn']
        del model_dict['_generated_api_get_fn_args']
        del model_dict['_model_attribute_types']
        model_id = model_dict.get('_id', '')
        return f"{self.__class__.__name__} <{model_id}> Model: {model_dict}"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self._id})"

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
            if not self._model_attribute_types.get(field) :
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

    @classmethod
    def _get_client(cls):
        return PinterestSDKClient.create_default_client()
