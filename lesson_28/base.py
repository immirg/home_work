from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:

    def __init__(self, driver):
        self.driver = driver

    def elem_available(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find_elem(self, locator):
        return self.driver.find_element(*locator)
