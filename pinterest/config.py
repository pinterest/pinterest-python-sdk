"""
Pinterest config
"""
import os as _os
from dotenv import load_dotenv as _load_env_vars
from pinterest.version import __version__
from pinterest.utils.load_json_config import load_json_config as _load_json,\
    load_json_config_from_single_env_var as _load_json_single_variable

_load_env_vars()
_load_json()
_load_json_single_variable()

PINTEREST_DEBUG = _os.environ.get('PINTEREST_DEBUG', "False").lower() == "true"
PINTEREST_PORT = _os.environ.get('PINTEREST_PORT', 0)
PINTEREST_APP_ID = _os.environ.get('PINTEREST_APP_ID', 0)
PINTEREST_APP_SECRET = _os.environ.get('PINTEREST_APP_SECRET', '')
PINTEREST_CLIENT_ID = _os.environ.get('PINTEREST_CLIENT_ID', '')
PINTEREST_REDIRECT_URI = _os.environ.get('PINTEREST_REDIRECT_URI', '')
PINTEREST_RESPONSE_TYPE = _os.environ.get('PINTEREST_RESPONSE_TYPE', '')
PINTEREST_SCOPE = _os.environ.get('PINTEREST_SCOPE', '')
PINTEREST_STATE = _os.environ.get('PINTEREST_STATE', '')
PINTEREST_ACCESS_TOKEN_JSON_PATH = _os.environ.get('PINTEREST_ACCESS_TOKEN_JSON_PATH', '')
PINTEREST_ACCESS_TOKEN = _os.environ.get('PINTEREST_ACCESS_TOKEN')
PINTEREST_REFRESH_ACCESS_TOKEN = _os.environ.get('PINTEREST_REFRESH_ACCESS_TOKEN')
PINTEREST_API_URI = _os.environ.get('PINTEREST_API_URI', 'https://api.pinterest.com/v5')
PINTEREST_LOG_FILE = _os.environ.get('PINTEREST_LOG_FILE', None)
DEFAULT_DISABLE_VALIDATIONS = ",".join([
    'multipleOf', 'maximum', 'exclusiveMaximum',
    'minimum', 'exclusiveMinimum', 'maxLength',
    'minLength', 'pattern', 'maxItems', 'minItems',
])
PINTEREST_DISABLED_CLIENT_SIDE_VALIDATIONS = _os.environ.get(
    'PINTEREST_DISABLED_CLIENT_SIDE_VALIDATIONS',
    DEFAULT_DISABLE_VALIDATIONS
)
PINTEREST_LOGGER_FORMAT = _os.environ.get('PINTEREST_LOGGER_FORMAT', '%(asctime)s %(levelname)s %(message)s')
PINTEREST_SDK_VERSION = __version__
PINTEREST_USER_AGENT = f'pins-sdk/python/v{PINTEREST_SDK_VERSION}'
