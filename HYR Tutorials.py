import time
from time import sleep

import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/")
driver.find_element(BY.ID,'')
#select.("Selenium Practice")
#select.select_by_value("XPath Practice")
#Select = Select(driver. findElement(By. xpath("//*[@id='oldSelectMenu']")))
time.sleep(5)


































































































# # Set the path to your ChromeDriver executable
# driver.get("C:/Users/Thanusha Kotaprolu/Downloads/ThanushaKotaprolu-SeleniumPython/chromedriver_win32.zipcom/")  # Replace with your actual path
# driver = webdriver.Chrome(executable_path="C:/Chrome/chromedriver.exe")
# # Open the HTML page
# url = 'file:///path/to/your/html/file.html'  # Replace with the actual path to your HTML file
# driver.get(url)
#
# try:
#     # Click on the "Edureka Courses" button
#     courses_button = driver.find_element(By.XPATH, '//button[text()="Edureka Courses"]')
#     courses_button.click()
#
#     # Click on the "Display Alert" button
#     alert_button = driver.find_element(By.ID, 'alert')
#     alert_button.click()
#
#     # Handle the alert
#     alert = Alert(driver)
#     alert_text = alert.text
#     print(f"Alert text: {alert_text}")
#     alert.accept()
#
#     # Prompt user for input
#     user_input = driver.execute_script('return prompt("Enter your input:");')
#     print(f"User input: {user_input}")
#
#     # Confirm popup with OK and Cancel button
#     confirm_result = driver.execute_script('return confirm("Confirm pop up with OK and Cancel button");')
#     print(f"Confirm result: {confirm_result}")
#
# finally:
#     # Close the browser window
#     driver.quit()
