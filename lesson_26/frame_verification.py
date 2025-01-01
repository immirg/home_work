from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

# http://localhost:8000/dz.html
# python -m http.server 8000
# source .venv/bin/activate


def verify_frame_content(driver, frame, input, frame_secret):
    iframe = driver.find_element(By.XPATH, f"//iframe[@id='{frame}']")
    driver.switch_to.frame(iframe)

    input_text = driver.find_element(By.XPATH, f"//input[@id='{input}']")
    input_text.send_keys(frame_secret)

    button_check = driver.find_element(By.XPATH, f"//button[@onclick=\"verifyInput('{input}')\"]")
    button_check.click()

    return get_text_alert(driver=driver)


def get_text_alert(driver):
    alert = Alert(driver)
    alert_text = alert.text
    alert.accept()
    driver.switch_to.default_content()
    return alert_text
