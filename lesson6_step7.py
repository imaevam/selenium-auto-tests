from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_tag_name('img') #найти сундук
x_element = input1.get_attribute('valuex') # найти значение(число) которое находится в сундуке
y = calc(x_element)
input1 = browser.find_element_by_tag_name('input')
input1.send_keys(y)

option = browser.find_element_by_id('robotCheckbox') #поставить галочку напротив i'm the robot
option.click()
option2 = browser.find_element_by_id('robotsRule')
option2.click()
button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(30)

#оставить пустую строку в конце файла

