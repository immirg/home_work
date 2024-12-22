import logging
import pytest
from lesson_24.homework_24 import get_auth_headers
from lesson_24.test_sort_cars import SortCars


@pytest.mark.parametrize('limit, expected', [(3, 2), (3, 4)])
def test_negative_check_limit_param(get_auth_headers, limit, expected):
    headers = get_auth_headers
    cars = SortCars.login(headers=headers, limit=limit)
    if len(cars) == expected:
        logging.error(f'Ожидаемое количество {limit}, фактическое {expected}')
    assert len(cars) != expected
