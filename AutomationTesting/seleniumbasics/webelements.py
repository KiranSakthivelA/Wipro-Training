import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


driver = webdriver.Edge()        #service=Service('../resources/msedgedriver.exe')

driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(10)


text_input = driver.find_element(By.ID, "my-text-id")
text_input.clear()
text_input.send_keys("Selenium WebDriver Demo")

password_input = driver.find_element(By.NAME, "my-password")
password_input.clear()
password_input.send_keys("secret123")

textarea = driver.find_element(By.NAME, "my-textarea")
textarea.clear()
textarea.send_keys("This is a sample message")

checkbox = driver.find_element(By.ID, "my-check-2")
checkbox.click()

radio = driver.find_element(By.ID, "my-radio-2")
radio.click()

dropdown = driver.find_element(By.NAME, "my-select")
dropdown.click()
option=driver.find_element(By.CSS_SELECTOR, "select [name='my-select'] option [value='2']")
option.click()

multi_select = driver.find_element(By.NAME, "my-datalist")
multi_select.send_keys('New York')

file_upload = driver.find_element(By.NAME, "my-file")
file_upload.send_keys(r"C:\Wipro Training\AutomationTesting\seleniumbasics\waits.py")

range_slider = driver.find_element(By.NAME, "my-range")
driver.execute_script("arguments[0].value=10;", range_slider)

color_picker = driver.find_element(By.NAME, "my-color")
color_picker.send_keys("00ff00")

date_input = driver.find_element(By.NAME, "my-date")
date_input.send_keys("2025-12-05")

submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")




time.sleep(5)
driver.quit()
