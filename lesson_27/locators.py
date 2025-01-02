from selenium.webdriver.common.by import By


class TrackingPageLocators:
    track_field = (By.XPATH, "//input[@id='en']")
    button_search = (By.XPATH, "//input[@type='submit']")
    text_parcel_not_found = (By.XPATH, "//span[@data-v-d383c0c2]")
