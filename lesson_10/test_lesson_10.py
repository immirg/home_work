import pytest
from additional_tests.task_2 import check_email, check_ip


class TestEmail:
    @pytest.mark.email
    @pytest.mark.parametrize('input_value, expected_result', [
        ('asd@asd.com', 'Mail is valid'),
        ('asd@asd.', 'Mail is not valid'),
        ('asd@.', 'Mail is not valid'),
        ('@asd.com', 'Mail is not valid'),
        ('a@asd.com', 'Mail is not valid')
    ])
    def test_email_missing_top_domain(self, input_value, expected_result):
        assert check_email(input_value) == expected_result


class TestIP:
    @pytest.mark.testIp
    @pytest.mark.parametrize('input_value, expected_result', [
        ('17.172.224.47', 'Correct IP address'),
        ('7.0.224.0', 'Correct IP address'),
        ('07.172.224.0', 'Incorrect IP address'),
        ('7.172.224.', 'Incorrect IP address'),
    ])
    def test_is_valid_ip(self, input_value, expected_result):
        assert check_ip(input_value) == expected_result



