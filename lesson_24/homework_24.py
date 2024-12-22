import logging
import pytest
import requests

# source .venv/bin/activate
# python cars_app.py

url = 'http://127.0.0.1:8080'
username = "test_user"
password = "test_pass"


@pytest.fixture(scope='class')
def get_auth_headers():
    response = requests.post(url=f'{url}/auth', auth=(username, password))
    if response.status_code == 200:
        token = response.json().get('access_token')
        headers = {'Authorization': f'Bearer {token}'}
        return headers
    else:
        logging.error(f'Ошибка при логине {response.status_code}, {response.text}')
        pytest.exit('Не удалось выполнить авторизацию')




