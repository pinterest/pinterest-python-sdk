"""
module with the function `load_json_config` that parse a config.json file and then load all the variables found as
environment variables.
"""
import json
import os

__all__ = ['load_json_config', 'load_json_config_from_single_env_var']

_PREFIX = 'PINTEREST_'


def load_json_config():
    """Parse a config.json file and then load all the variables found as environment variables."""
    current_dir = _get_current_dir()

    config_json_file_path = _find_config_json_path(current_dir)
    if not config_json_file_path:
        return

    config_json = _load_json_file(config_json_file_path)

    for attribute, value in config_json.items():
        _set_as_environment_variables(f'{_PREFIX}{attribute.upper()}', str(value))

def load_json_config_from_single_env_var():
    """
    Parse PINTEREST_JSON_ENV_VARIABLES environment variable to split long JSON string into
    individual environment variables.
    """
    config_json = os.environ.get('PINTEREST_JSON_ENV_VARIABLES')
    if not config_json:
        return

    config_json = json.loads(config_json)

    for attribute, value in config_json.items():
        os.environ[attribute] = str(value)


def _get_current_dir():
    return os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))


def _find_config_json_path(path: str, file_name: str = 'config.json'):
    for root, _, files in os.walk(path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None


def _load_json_file(file_path: str) -> dict:
    with open(file_path, 'r', encoding='UTF-8') as jsonfile:
        return json.load(jsonfile)


def _set_as_environment_variables(key: str, value: str):
    os.environ[key] = value
