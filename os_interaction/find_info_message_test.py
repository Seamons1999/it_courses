import unittest
import sys
import os
from ticky_check import find_info_message


class TestAnalyzeSyslog(unittest.TestCase):
    def test_error_message(self):
        input_string = "Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)"
        expected = None
        self.assertEqual(find_info_message(input_string), expected)

    def test_info_message(self):
        input_string = "Jan 31 00:16:25 ubuntu.local ticky: INFO Closed ticket [#1754] (noel)"
        expected = "Closed ticket"
        self.assertEqual(find_info_message(input_string)[1], expected)

    def test_ticket_number(self):
        input_string = "Jan 31 00:16:25 ubuntu.local ticky: INFO Closed ticket [#1754] (noel)"
        expected = "1754"
        self.assertEqual(find_info_message(input_string)[2], expected)

    def test_user_id(self):
        input_string = "Jan 31 00:16:25 ubuntu.local ticky: INFO Closed ticket [#1754] (noel)"
        expected = "noel"
        self.assertEqual(find_info_message(input_string)[3], expected)

    def test_point_in_name(self):
        input_string = "Jan 31 19:59:06 ubuntu.local ticky: INFO Created ticket [#6361] (enim.non)"
        expected = "enim.non"
        self.assertEqual(find_info_message(input_string)[3], expected)


if __name__ == '__main__':
    unittest.main()