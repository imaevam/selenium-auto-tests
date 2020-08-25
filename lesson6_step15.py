from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("I")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("P")
    input3 = browser.find_element_by_css_selector(".form-control.city")
    input3.send_keys("S")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("R")
    button = browser.find_element_by_xpath("//button[contains(text(), 'Submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
