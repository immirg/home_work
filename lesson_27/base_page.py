from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def element_located(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_clickable(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)
