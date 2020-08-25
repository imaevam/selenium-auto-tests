from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    input1 = browser.find_element_by_id('book')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    input1.click()
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input2 = browser.find_element_by_tag_name('input')
    input2.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

