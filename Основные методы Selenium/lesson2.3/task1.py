import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/alert_accept.html")
time.sleep(1)

button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

#
alert = browser.switch_to.alert.accept()

value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
answer = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(value))
submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

time.sleep(5)