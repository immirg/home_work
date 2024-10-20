import unittest
from additional_tests.task_2 import palindrome_check, check_email, check_ip
import sys
import pathlib
import requests
import pytest

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))


class PalindromeTests(unittest.TestCase):

    def test_is_palindrome(self):
        actual_result = palindrome_check(word='121')
        expected_result = '+'
        self.assertEqual(actual_result, expected_result)

    def test_is_not_palindrome(self):
        actual_result = palindrome_check(word='abc')
        expected_result = '-'
        self.assertEqual(actual_result, expected_result)


class EmailTests(unittest.TestCase):

    def test_is_valid_emai(self):
        actual_result = check_email('asd@asd.com')
        expected_result = 'Mail is valid'
        self.assertEqual(actual_result, expected_result)

    def test_email_missing_top_domain(self):
        actual_result = check_email('asd@asd.')
        expected_result = 'Mail is not valid'
        self.assertEqual(actual_result, expected_result)

    def test_email_missing_domain(self):
        actual_result = check_email('asd@.')
        expected_result = 'Mail is not valid'
        self.assertEqual(actual_result, expected_result)

    def test_email_missing_username(self):
        actual_result = check_email('@asd.com')
        expected_result = 'Mail is not valid'
        self.assertEqual(actual_result, expected_result)

    def test_email_with_one_symbol_in_username_is_invalid(self):
        actual_result = check_email('a@asd.com')
        expected_result = 'Mail is not valid'
        self.assertEqual(actual_result, expected_result)


class IPTests(unittest.TestCase):

    def test_is_valid_ip(self):
        actual_result = check_ip('17.172.224.47')
        expected_result = 'Correct IP address'
        self.assertEqual(actual_result, expected_result)

    def test_ip_with_one_number_zero_is_valid(self):
        actual_result = check_ip('7.0.224.0')
        expected_result = 'Correct IP address'
        self.assertEqual(actual_result, expected_result)

    def test_ip_with_leading_zero_is_invalid(self):
        actual_result = check_ip('07.172.224.0')
        expected_result = 'Incorrect IP address'
        self.assertEqual(actual_result, expected_result)

    def test_incomplete_ip_is_invalid(self):
        actual_result = check_ip('7.172.224.')
        expected_result = 'Incorrect IP address'
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
    
