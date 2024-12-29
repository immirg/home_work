import chromedriver_autoinstaller
from selenium.webdriver import Chrome
import pytest


@pytest.fixture(scope='session')
def get_driver():
    chromedriver_autoinstaller.install()
    driver = Chrome()
    driver.get('http://localhost:8000/dz.html')
    yield driver
    driver.quit()
