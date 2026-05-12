import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(2)

txt_input = driver.find_element(By.ID,"my-text-id")
txt_input.clear()
txt_input.send_keys("Selenium WebDriver Demo")
time.sleep(2)

pass_input = driver.find_element(By.NAME,"my-password")
pass_input.clear()
pass_input.send_keys("secret123")
time.sleep(2)

#text area
txt_area = driver.find_element(By.NAME,"my-textarea")
txt_area.clear()
txt_area.send_keys("this is just a sample !")
time.sleep(2)

#chck-box
chck_box = driver.find_element(By.ID,"my-check-2")
chck_box.click()
time.sleep(2)

#radio button
radio = driver.find_element(By.ID,"my-radio-2")
radio.click()
time.sleep(1)

# dropdown button
drop_select = driver.find_element(By.NAME,"my-select")
drop_select.click()
time.sleep(1)

opt = driver.find_element(By.CSS_SELECTOR,"select[name='my-select'] option[value='2']")
opt.click()
time.sleep(2)

#drop_default
multi_select = driver.find_element(By.NAME,"my-datalist")
multi_select.send_keys("New York")
time.sleep(2)

#file--upload
file = driver.find_element(By.NAME,"my-file")
file.send_keys("C:\\Wipro Training\\Selenium\\Automation Basics\\selenium_basics\\navigation.py")
time.sleep(2)

#range slider
range_slide = driver.find_element(By.NAME,"my-range")
driver.execute_script("arguments[0].value = 10;",range_slide)
time.sleep(2)

#colour picker
colour_picker = driver.find_element(By.NAME,"my-colors")
colour_picker.send_keys("#00ff00")


#date pick
date_chck = driver.find_element(By.NAME,"my-date")
date_chck.send_keys("2025-12-25")
time.sleep(2)

#submit button
sub_btn = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
time.sleep(10)
sub_btn.submit()

time.sleep(10)


driver.quit()