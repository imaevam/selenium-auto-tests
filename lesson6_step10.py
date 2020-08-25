from selenium import webdriver
import os
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(link)
    browser.find_element_by_name('firstname').send_keys('M')
    browser.find_element_by_name('lastname').send_keys('I')
    browser.find_element_by_name('email').send_keys('b')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_id('file').send_keys(file_path)
    browser.find_element_by_css_selector('button[type="submit"]').click()
finally:
    time.sleep(30)
    c