from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(val):

    return str(math.log(abs(12*math.sin(int(val)))))


browser = webdriver.Chrome()


try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element(By.CSS_SELECTOR, "[id = book]")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[id=price]"), "$100"))
    button.click()
    input_form = browser.find_element(By.CSS_SELECTOR, "[id = answer]")
    browser.execute_script("return arguments[0].scrollIntoView(true)", input_form)
    x = int(browser.find_element(By.ID, "input_value").text)
    input_form.send_keys(calc(x))
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(5)
    browser.quit()