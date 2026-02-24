import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/execute_script.html")
time.sleep(1)

x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
answer = browser.find_element(By.CSS_SELECTOR, ".form-control").send_keys(calc(x))
checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()


radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
#Скролл страницы пока элемент не будет виден 
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
radiobutton.click()

#Cкролл страницы на опрделеноое колличетсво пикселей 
#browser.execute_script("window.scrollBy(0, 100);")


submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

time.sleep(5)

