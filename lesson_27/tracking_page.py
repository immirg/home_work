from lesson_27.base_page import BasePage
from lesson_27.locators import TrackingPageLocators


class TrackingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = "https://tracking.novaposhta.ua/#/uk"
        self.locators = TrackingPageLocators()

    def search_field_for_parcel_by_number(self, timeout=3):
        self.element_located(self.locators.track_field), timeout
        return self

    def parcel_search_button(self, timeout=3):
        self.element_clickable(self.locators.button_search), timeout
        return self

    def text_error(self, timeout=3):
        self.element_located(self.locators.track_field), timeout
        return self

    def page_element(self, locator):
        return self.find_element(locator)
