import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
time.sleep(1)
button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary").click()


#
wind = browser.window_handles[1]
browser.switch_to.window(wind)

value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
answer = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(value))
submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
time.sleep(5)