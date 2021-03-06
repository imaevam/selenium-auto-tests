from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    input1 = browser.find_element_by_tag_name('button')
    input1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
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