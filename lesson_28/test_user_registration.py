import pytest
from lesson_28.page_locators import PageLocators
from lesson_28.conftest import driver
from lesson_28.tracking_page import TrackingPages
from faker import Faker

url = "https://qauto2.forstudy.space/"
fk = Faker()


def registration_page(login_page):
    driver = login_page
    tracking_page = TrackingPages(driver)

    # open popup log in
    tracking_page.page_elem(PageLocators.sign_in_button).click()
    # open pup up Registration
    tracking_page.page_elem(PageLocators.registration_button).click()
    return tracking_page


def filling_in_registration_fields(tracking_page, name, last_name, email, password1, password2):
    tracking_page.page_elem(PageLocators.reg_name).send_keys(name)
    tracking_page.page_elem(PageLocators.reg_last_name).send_keys(last_name)
    tracking_page.page_elem(PageLocators.reg_email).send_keys(email)
    tracking_page.page_elem(PageLocators.reg_password).send_keys(password1)
    tracking_page.page_elem(PageLocators.reg_repeat_password).send_keys(password2)
    tracking_page.page_elem(PageLocators.registration_new_user_button).click()


def test_registration_with_valid_data(login_page):
    name = fk.first_name()
    last_name = fk.last_name()
    email = fk.email()
    password = '@wOw123!nTu0o'

    tracking_page = registration_page(login_page)
    filling_in_registration_fields(
        tracking_page,
        name=name,
        last_name=last_name,
        email=email,
        password1=password,
        password2=password)

    assert tracking_page.search_button(PageLocators.garage_page).page_elem(PageLocators.garage_page)


@pytest.mark.parametrize('name, last_name, email, password1, password2, text, locator', [
    ('s', fk.last_name(), fk.email(), '@wOw123!nTu0o', '@wOw123!nTu0o', PageLocators.short_name, 'name_err'),
    (fk.first_name(), 'f', fk.email(), '@wOw123!nTu0o', '@wOw123!nTu0o', PageLocators.short_last_name, 'last_name_err'),
    (fk.first_name(), fk.last_name(), 'tst@tst', '@wOw123!nTu0o', '@wOw123!nTu0o', PageLocators.incorrect_email, 'email_err'),
    (fk.first_name(), fk.last_name(), fk.email(), '@wOw123!nT111', '@wOw123!nTu0o', PageLocators.passwords_dont_match, 'password_dont_match'),
    (fk.first_name(), fk.last_name(), fk.email(), '@wOw', '@wOw', PageLocators.short_password, 'wrong_password')],
    ids=['short_name', "short_last_name", "incorrect_email", "passwords_dont_match", "short_password"])
def test_registration_with_invalid_data(login_page, name, last_name, email, password1, password2, text, locator):
    tracking_page = registration_page(login_page)
    filling_in_registration_fields(
        tracking_page,
        name=name,
        last_name=last_name,
        email=email,
        password1=password1,
        password2=password2)

    error_message_element = tracking_page.page_elem(getattr(PageLocators, locator))
    assert error_message_element.text == text
