import math
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

#Открытие брузера --> сайта 
driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/math.html")
time.sleep(2)

#Функция для решения задачи
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Чтобы забрать значение из селектора используется .text
value = driver.find_element(By.CSS_SELECTOR, '#input_value').text

#Чтоыб вставить текст в поле ввода используется .send_keys()
text_area = driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(value))

check_box = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
radio_batton = driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
submit = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

time.sleep(5)