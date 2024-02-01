import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path="C:\\Users\\Thanusha Kotaprolu\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
# driver.maximize_window()
# # driver = webdriver.Chrome(service=service_obj)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(5)
# Open the URL
driver.get("https://example.com")
# Find the element that triggers the alert
c = driver.find_element(By.XPATH, "your_xpath_here")
c.click()
# Switch to the alert
alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
# Get the text from the alert
s = alert.text
print("Alert text is:", s)
# Send keys to the alert
alert.send_keys("Selenium")
# Dismiss the alert
alert.dismiss()
# Click the element again
c.click()
# Accept the alert
alert.accept()
# Close the browser
driver.quit()

