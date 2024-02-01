from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.implicitly_wait(5)

# URL launch
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Identify element
button = driver.find_element_by_xpath("//button[text()='Click for JS Prompt']")
button.click()

# Switch to alert
alert = Alert(driver)

# Get alert text
alert_text = alert.text
print("Alert text is:", alert_text)

# Input text to alert
alert.send_keys("Selenium")

# Dismiss alert
alert.dismiss()

button.click()

# Accept alert
alert.accept()

# Quit the driver
driver.quit()