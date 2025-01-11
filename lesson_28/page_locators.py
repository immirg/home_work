from selenium.webdriver.common.by import By


class PageLocators:
    sign_in_button = (By.XPATH, '//button[@class="btn btn-outline-white header_signin"]')
    registration_button = (By.XPATH, '//button[contains(text(), "Registration")]')
    reg_name = (By.XPATH, '//input[@name="name"]')
    reg_last_name = (By.XPATH, '//input[@name="lastName"]')
    reg_email = (By.XPATH, '//input[@name="email"]')
    reg_password = (By.XPATH, '//input[@name="password"]')
    reg_repeat_password = (By.XPATH, '//input[@name="repeatPassword"]')
    registration_new_user_button = (By.XPATH, '//button[@class="btn btn-primary"]')
    garage_page = (By.XPATH, '//h1[contains(text(), "Garage")]')

    short_name = 'Name has to be from 2 to 20 characters long'
    short_last_name = 'Last name has to be from 2 to 20 characters long'
    incorrect_email = 'Email is incorrect'
    passwords_dont_match = 'Passwords do not match'
    short_password = 'Password has to be from 8 to 15 characters long and contain at least one integer, one capital, ' \
                     'and one small letter'

    name_err = (By.XPATH, f'//p[contains(text(), "{short_name}")]')
    last_name_err = (By.XPATH, f'//p[contains(text(), "{short_last_name}")]')
    email_err = (By.XPATH, f'//p[contains(text(), "{incorrect_email}")]')
    password_dont_match = (By.XPATH, f'//p[contains(text(), "{passwords_dont_match}")]')
    wrong_password = (By.XPATH, f'//p[contains(text(), "{short_password}")]')

