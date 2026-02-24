import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Явное ожидание пока текст элемента не покажет $100 в течении 20 секунд код не пойдет дальше
price = WebDriverWait(browser, 20).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element(By.ID, "book").click()


submit = browser.find_element(By.CSS_SELECTOR, "#solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
answern = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
submit.click()

time.sleep(5)





time.sleep(5)
