import unittest
import sys
import os
from ticky_check import find_error_message


class TestAnalyzeSyslog(unittest.TestCase):
    def test_error_message(self):
        input_string = "Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)"
        expected = "The ticket was modified while updating"
        self.assertEqual(find_error_message(input_string)[1], expected)

    def test_user_id(self):
        input_string = "Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)"
        expected = "breee"
        self.assertEqual(find_error_message(input_string)[2], expected)

    def test_info_message(self):
        input_string = "Jan 31 00:16:25 ubuntu.local ticky: INFO Closed ticket [#1754] (noel)"
        expected = None
        self.assertEqual(find_error_message(input_string), expected)

    def test_point_in_name(self):
        input_string = "Jan 31 19:20:22 ubuntu.local ticky: ERROR Timeout while retrieving information (mai.hendrix)"
        expected = "mai.hendrix"
        self.assertEqual(find_error_message(input_string)[2], expected)

    def test_single_quote(self):
        input_string = "Jan 31 02:55:31 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)"
        expected = "xlg"
        self.assertEqual(find_error_message(input_string)[2], expected)

    def test_xlg(self):
        input_string = 'Jan 31 14:41:18 ubuntu.local ticky: ERROR Timeout while retrieving information (xlg)'
        expected = 'Timeout while retrieving information'
        self.assertEqual(find_error_message(input_string)[1], expected)


if __name__ == '__main__':
    unittest.main()