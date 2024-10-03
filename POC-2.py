import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define a Page Object for the Login Page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

# Define a Page Object for the Product Page
class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Cart']"))
        ).click()

# Define a Page Object for the Cart Page
class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_product_in_cart(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cart-item"))
        )

# Fixture to set up and tear down the WebDriver
@pytest.fixture(scope="module")
def driver():
    chrome_driver_path = r"C:C:\Users\Thanusha Kotaprolu\Downloads\chrome-win64\chrome-win64"
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.example-ecommerce.com")  # Replace with the actual URL
    yield driver
    driver.quit()

# Test case to check login and adding a product to the cart
def test_ecommerce_flow(driver):
    login_page = LoginPage(driver)
    login_page.login("test_user", "test_password")  # Replace with actual credentials

    product_page = ProductPage(driver)
    product_page.add_product_to_cart()

    cart_page = CartPage(driver)
    assert cart_page.verify_product_in_cart() is not None
