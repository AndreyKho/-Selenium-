import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/file_input.html")
time.sleep(1)
firstname = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys("Andrey")
lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys("Khor")
email = browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('andrey@mail.ru')

#Загрузка файла с помощью указания пути 
file = browser.find_element(By.CSS_SELECTOR, "#file").send_keys('/Users/andrej/Desktop/Python/Selenium Python/Основные методы Selenium/lesson2.2/exemple.txt')

#

submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
time.sleep(5)