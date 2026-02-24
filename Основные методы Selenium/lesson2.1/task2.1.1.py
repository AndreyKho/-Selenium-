import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/get_attribute.html")
time.sleep(2)

synduk = browser.find_element(By.CSS_SELECTOR, '#treasure')
value = synduk.get_attribute("valuex")

answerv = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(value))


checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
radiobatton = browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()

time.sleep(5)