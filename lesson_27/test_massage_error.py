from selenium.webdriver import Chrome
import pytest
from lesson_27.locators import TrackingPageLocators
from lesson_27.tracking_page import TrackingPage

message = "Ми не знайшли посилку за таким номером. Якщо ви шукаєте інформацію про посилку, " \
          "якій більше 3 місяців, будь ласка, зверніться у контакт-центр: 0 800 500 609"

parsel_num = "00000000000"
url = "https://tracking.novaposhta.ua/#/uk"


@pytest.fixture()
def driver():
    driver = Chrome()
    yield driver
    driver.close()


def test_massage_error(driver):
    driver.get(url)
    tracking_page = TrackingPage(driver)

    tracking_page.search_field_for_parcel_by_number().page_element(TrackingPageLocators.track_field).send_keys(parsel_num)
    tracking_page.parcel_search_button().page_element(TrackingPageLocators.button_search).click()
    err_text = tracking_page.text_error().page_element(TrackingPageLocators.text_parcel_not_found).text

    assert err_text == message
