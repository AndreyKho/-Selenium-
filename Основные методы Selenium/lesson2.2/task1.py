import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/selects1.html")
time.sleep(1)

num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text

value = (int(num1) + int(num2))

answer = browser.find_element(By.CSS_SELECTOR, f"[value='{value}']").click()

submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
time.sleep(5)