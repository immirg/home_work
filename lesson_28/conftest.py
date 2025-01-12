import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    service = Service()
    web_driver = Chrome(service=service)
    yield web_driver
    web_driver.close()


@pytest.fixture
def login_page(driver):
    username = 'guest'
    password = 'welcome2qauto'
    url = f'https://{username}:{password}@qauto2.forstudy.space/'
    driver.get(url)
    return driver

