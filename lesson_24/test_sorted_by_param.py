import logging
import pytest
from lesson_24.homework_24 import get_auth_headers
from lesson_24.test_sort_cars import SortCars


@pytest.mark.parametrize('filter', ['year', 'price', 'engine_volume'])
def test_sorted_by_param(get_auth_headers, filter):
    headers = get_auth_headers
    cars = SortCars.login(headers=headers, sort_by=filter)
    len_cars = len(cars)
    for num in range(1, len_cars):
        if not cars[num][filter] >= cars[num-1][filter]:
            logging.error(f"Ошибка сортировки по {filter}: {cars[num][filter]} не меньше {cars[num-1][filter]}")
        assert cars[num][filter] >= cars[num-1][filter]
