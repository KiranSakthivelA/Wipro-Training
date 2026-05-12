import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

# driver.get("https://www.google.com")
driver.get("https://the-internet.herokuapp.com/tables")

#ID
# driver.get("https://www.google.com")
# search_input=driver.find_element(By.ID, "APjFqb")
# search_input.send_keys(("selenium"))
# time.sleep(3)

#ID
# search_input = driver.find_element(By.NAME, "q")
# search_input.send_keys("locators")
# time.sleep(5)
#Name
# googlesearch_button = driver.find_element(By.NAME, "btnK")
# googlesearch_button.click()
# time.sleep(30)

#classname
# imfl_button = driver.find_element(By.CLASS_NAME, "RNmpXc")
# imfl_button.click()
# time.sleep(3)


#tagname
# href_elements = driver.find_elements(By.TAG_NAME, "a")
# for elmt in href_elements:
#     print(f'{elmt.text} - {elmt.get_attribute("href")}')

#link
# images_link = driver.find_element(By.LINK_TEXT, "Images")
# images_link.click()
# time.sleep(3)

#particallink
# images_link = driver.find_element(By.PARTIAL_LINK_TEXT, "ma")
# images_link.click()
# time.sleep(3)

#CSSSelector
# search_input=driver.find_element(By.CSS_SELECTOR, 'div>textarea')
# search_input.send_keys("selenium")
# time.sleep(3)

#xpath

settings_text=driver.find_element(By.XPATH,  )
print(settings_text.text)
time.sleep(5)
