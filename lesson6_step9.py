from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
try: 
    browser.get(link)
    x_element = browser.find_element_by_id('input_value').text #найти значение для икса
    y = calc(x_element) #передать значение переменной в функцию и поместить результат выполнения в y
    input1 = browser.find_element_by_id('answer') #найти окно для ввода результата
    input1.send_keys(y) #вписать результат в окно ввода
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_id('robotCheckbox').click() #поставить галочку напротив i'm the robot
    browser.find_element_by_id('robotsRule').click()
    button.click()

finally:
    time.sleep(30)
    browser.quit()

#button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click()
#input1 = browser.find_element_by_tag_name('input')
#input1.send_keys(y)

