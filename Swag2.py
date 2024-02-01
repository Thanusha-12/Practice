from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep, time

# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
# Define items to add to cart
items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt"]
# Add items to cart
for item in items_to_add:
    add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "shopping_cart_link fa-layers fa-fw")
    for btn in add_to_cart_btns:
        if btn.get_attribute("inventory_item_name") is not None and item in btn.get_attribute("inventory_item_name"):
            btn.click()
            break
# Check cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
#assert len(cart_items) == len(items_to_add)
#driver.quit()
sleep(10)
