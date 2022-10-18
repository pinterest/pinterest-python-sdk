from unittest.mock import patch
import unittest
from pinterest.bin import get_config


class GetConfigTest(unittest.TestCase):
    @patch('builtins.print')
    def test_output_contains_pinterest_variables(self, mock_stdout):
        get_config.main([])
        self.assertIn('PINTEREST_', str(mock_stdout.call_args))

