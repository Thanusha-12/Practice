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
driver.get("https://www.instacart.com/")
time.sleep(3000)

# # driver.find_element(By.CLASS_NAME, "ctp-checkbox-label").click()
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='0']kbox-checkmark']")))
#
#
#
# WebDriverWait(driver, 10)
# driver.get("https://www.instacart.com")
# WebDriverWait(driver, 10).until(EC.presenceOfElementLocated(By.cssSelector("iframe[tabindex='0']")));
# driver.switchTo().frame(webdriver)
# if (webdriver != 0):
#     time.sleep(100)
# print("Iframe with specified tabindex found")
# print(driver.getPageSource())
# WebElementcheckBox = driver.findElement(By.xpath("//input[@type='checkbox']"))
# if (WebElementcheckBox != 0):
# 	print("found")
# 	(webdriver).executeScript("arguments[0].click();", WebElementcheckBox)
# elseif:
# 	print("not found")
# else:
# 	print("Iframe with specified tabindex not found")
#
#
# # #Identify the iframe
# # iframe_locator = (By.ID, "turnstile-wrapper")
# #
# # #Switch to that iframe
# #
# # driver.switch_to.frame("driver.find_element()iframe_locator")
# #
# # element_inside_iframe = driver.find_element(By.XPATH,"//input[@id='cf-chl-widget-86vza_response']")
#
# # class="ctp-checkbox-label"
# # type="checkbox"
#
#
#
#
#
#
#
#

# # print(driver.current_url)
# # driver.get("https://www.instacart.com/")
# # #driver.find_element(By.CLASS_NAME,'ctp-checkbox-label').click()


#
#
# # first import the module
# import webbrowser
#
# # then make a url variable
# url = "https://www.instacart.com/"
#
# # getting path
# chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
#
# # First registers the new browser
# webbrowser.register('chrome', None,
#                     webbrowser.BackgroundBrowser(chrome_path))
#
# # after registering we can open it by getting its code.
# webbrowser.get('chrome').open(url)