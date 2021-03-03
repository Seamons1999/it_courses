import unittest
import sys
import os
from ticky_check import analyze_syslog


syslog_location = os.path.join(os.getcwd(), 'syslog.log')
result_dictionaries = analyze_syslog(syslog_location)


class TestAnalyzeSyslog(unittest.TestCase):

    def test_number_of_return_values(self):
        error_count_by_msg = sum(result_dictionaries[0].values())
        error_count_by_user = sum(result_dictionaries[1].values()) # Values is now list, this needs to be fixed
        self.assertEqual(error_count_by_msg, error_count_by_user)


if __name__ == '__main__':
    unittest.main()

