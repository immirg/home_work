import requests
import logging
url = 'http://127.0.0.1:8080'


class SortCars:

    @staticmethod
    def login(headers, limit=None, sort_by=None):
        if not headers:
            logging.error('Ошибка аунтетификации')
            return
        params = {
            "sort_by": sort_by,
            "limit": limit
        }
        response = requests.get(url=f'{url}/cars', params=params, headers=headers)
        return response.json()
