from selenium import webdriver
import time


link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)
link = browser.find_element_by_partial_link_text('224592')
link.click()

try:
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("I")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("P")
    input3 = browser.find_element_by_css_selector(".form-control.city")
    input3.send_keys("S")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("R")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
