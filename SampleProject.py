from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()
driver = webdriver.Chrome(service=service_obj) #chrome,#FireFox
driver.maximize_window()
driver.get("https://www.google.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.google.com/search?q=swiggy+login&rlz=1C1CHBF_enIN1049IN1049&oq=sw&gs_lcrp=EgZjaHJvbWUqCQgBEAAYQxiKBTIGCAAQRRg5MgkIARAAGEMYigUyCQgCEAAYQxiKBTIVCAMQLhhDGIMBGMcBGLEDGNEDGIoFMgwIBBAAGEMYsQMYigUyCQgFEAAYQxiKBTIJCAYQABhDGIoFMgkIBxAAGEMYigUyCQgIEAAYQxiKBTINCAkQABiDARixAxiABNIBCDU0MjZqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8")
driver.back()
#driver.forward()
driver.refresh()
driver.minimize_window()
driver.close()
# service_obj = Service("C:/Users/Thanusha Kotaprolu/Downloads/ThanushaKotaprolu-SeleniumPython/chromedriver_win32.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.google.com/")

