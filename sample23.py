import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)
driver.get("https://www.instacart.com/")

iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[tabindex='0']")))
driver.switch_to.frame(iframe)

if iframe is not None:
    time.sleep(10)
    print("Iframe with specified tabindex found")
    # print(driver.page_source)
    checkBox = driver.find_element(By.XPATH, "//*[@type='checkbox']")
    if checkBox is not None:
        print("found")
        driver.execute_script("arguments[0].click();", checkBox)
    else:
        print("not found")
else:
    print("Iframe with specified tabindex not found")
time.sleep(20)