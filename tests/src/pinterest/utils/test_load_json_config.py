"""
Test Load Json Config
"""
import os
from unittest import TestCase, mock

import pinterest.utils.load_json_config as load_json_config_module


def _get_var_value():
    # pylint: disable=import-outside-toplevel
    """this import are for testing purpose"""
    return os.environ.get('PINTEREST_DUMMY', '1234567890')


class TestLoadJsonConfig(TestCase):
    """
    Test Load Json Config
    """

    def setUp(self) -> None:
        super().setUp()
        # pylint: disable=protected-access
        # Mock ._find_config_json_path and _load_json_file to return a dummy path to test
        load_json_config_module._find_config_json_path = lambda x: r'\foo\config.json'
        load_json_config_module._load_json_file = lambda x: {'state': '1234567890'}

    @mock.patch.dict(os.environ, {"PINTEREST_STATE": "1234567890"})
    def test_load_json_config(self):
        """
        Verify if the function successfully load config.json
        """
        load_json_config_module.load_json_config()
        self.assertEqual(_get_var_value(), '1234567890')

    def test_not_load_json_config(self):
        """
        Verify if the function not load config.json
        """
        prev_load_value = _get_var_value()
        load_json_config_module.load_json_config()
        post_load_value = _get_var_value()
        self.assertNotEqual(prev_load_value, '12345678901234')
        self.assertEqual(prev_load_value, post_load_value)
