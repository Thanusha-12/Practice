import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launching the application
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://devwinde1webapp1dev.azurewebsites.net/Account/SignIn?ReturnUrl=%2F")
driver.implicitly_wait(3)

#########LOGIN###################
email_input = driver.find_element(By.ID, "Username")
# email_input.clear()# Clear any pre-filled text (if any)
email_input.send_keys("thanusha.kataprolu@clientek.com", Keys.RETURN)
driver.implicitly_wait(5)
password_input = driver.find_element(By.ID,"Password")
password_input.send_keys("Cognine@12",Keys.RETURN)
time.sleep(3)

###################Design Pressures##############
try:
    # Wait for the element with visible text to be clickable
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Design Pressures')]"))
    )
    # Click the element
    element.click()
finally:
    time.sleep(3)
address= driver.find_element(By.XPATH, '//*[@id="address"]')
address.send_keys('Miami, FL, USA')
asceEdition=driver.find_element(By.XPATH, '//*[@id="asceEdition"]')
# Create a Select object to interact with the <select> element
select = Select(asceEdition)
select.select_by_visible_text('ASCE 7-10')
riskCategory=driver.find_element(By.XPATH, '//*[@id="riskCategory"]')
select = Select(riskCategory)
select.select_by_visible_text('II')
exposureCategory=driver.find_element(By.XPATH, '//*[@id="exposureCategory"]')
select = Select(exposureCategory)
select.select_by_visible_text('C')
buildingHeight = driver.find_element(By.ID, "buildingHeight")
buildingHeight_value = "60"
buildingHeight_value_int = int(buildingHeight_value)  # Convert to integer
if buildingHeight_value_int > 60:
    unitHeight = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "unitHeight"))
    )
    # Ensure the unitHeight element is interactable
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "unitHeight"))
    )
    unitHeight.send_keys("35")
else:
    driver.execute_script("arguments[0].value = arguments[1];", buildingHeight, buildingHeight_value)
unitsize =driver.find_element(By.ID, "unitSize")
unitsize.send_keys("56")
checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "IsManualcheck")))
driver.execute_script("arguments[0].click();", checkbox)
wind_speed_input = driver.find_element(By.ID, "manualWindSpeed")
wind_speed_input.send_keys("150")
driver.find_element(By.XPATH, '//*[@id="savebtn"]').click()
time.sleep(3)


# button = driver.find_element(By.XPATH, "//button[contains(@class, 'btnOrange')]")
# button.click()
