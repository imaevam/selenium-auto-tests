from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_id('num1')
input2 = browser.find_element_by_id('num2')
n1 = input1.text
n2 = input2.text
x = int(n1)
y = int(n2)
total = int(x) + int(y)
total = str(int(x) + int(y))

select = Select(browser.find_element_by_tag_name('select'))
select.select_by_value(total)

button = browser.find_element_by_css_selector('button.btn')
button.click()

time.sleep(30)



