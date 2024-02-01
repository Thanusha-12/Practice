from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.swiggy.com/")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "r2iyh").click()
