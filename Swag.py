import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(5)
print("testing add to cart")
item="Sauce Labs Bolt T-Shirt"
products = driver.find_elements(By.CLASS_NAME, "inventory_item")
for product_element in products:
    product_name = product_element.find_element(By.CLASS_NAME, "inventory_item_name ").text
    if product_name == item:
        addtocart = product_element.find_element(By.CLASS_NAME, "btn_primary")
        addtocart.click()
time.sleep(5)
print("checking with cart items")
cart=driver.find_element(By.CLASS_NAME, "shopping_cart_container")
cart.click()
time.sleep(5)
cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
if len(cart_items) != 1:
    for item in cart_items:
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        # driver.execute_script("arguments[0].remove()", item)
        print(f"Removed {item_name} from cart")
# else:
#     checkout = driver.find_element(By.CLASS_NAME, "checkout_button")
#     checkout.click()
time.sleep(10)

# Checkout
assert len(cart_items) == 1
checkout=driver.find_element(By.CLASS_NAME, "checkout_button")
checkout.click()

# Add to Cart
add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
for btns in add_to_cart_btns[2:3]:
    btns.click()

driver.minimize_window()
driver.close()
