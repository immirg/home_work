from lesson_28.base import Base
from lesson_28.page_locators import PageLocators


class TrackingPages(Base):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = "https://qauto2.forstudy.space/"
        self.locators = PageLocators

    def page_elem(self, locator):
        return self.find_elem(locator)

    def search_button(self, button, timeout=7):
        self.elem_available(button, timeout)
        return self
