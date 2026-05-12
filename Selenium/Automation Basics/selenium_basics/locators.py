import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Edge()
# driver.get("https://www.google.com")

#id--
# srch_ind = driver.find_element(By.ID,"APjFqb")
# srch_ind.send_keys("selenium")
#
# time.sleep(3)
# srch_ind.clear()
# time.sleep(2)

#name --
# srch_input = driver.find_element(By.NAME,"q")
# srch_input.send_keys("locators")
# time.sleep(5)

# google_btn = driver.find_element(By.NAME,"btnK")
# google_btn.click()
# time.sleep(3)

#class name --
# imfl_btn = driver.find_element(By.CLASS_NAME,'RNmpXc')
# imfl_btn.click()
# time.sleep(3)


#tag -- printing all the href's
# href_ele = driver.find_elements(By.TAG_NAME,"a")
# for ele in href_ele:
#     print(f'{ele.text} - {ele.get_attribute("href")}')

#linktext --
# img_link = driver.find_element(By.LINK_TEXT,"Images")
# img_link.click()
# time.sleep(5)

# partial linktext --
# img_link = driver.find_element(By.PARTIAL_LINK_TEXT,"ma")
# img_link.click()
# time.sleep(5)

#css selector --
# search_input = driver.find_element(By.CSS_SELECTOR,'div > textarea')
# search_input.send_keys('selenium')
# time.sleep(5)

#
# driver.get("https://the-internet.herokuapp.com/tables")
# time.sleep(3)

# #and oper:
# and_eg = driver.find_element(By.XPATH,"//td[text()='Tim' and @class='first-name']")
# print(f"AND -- found BOTH condition: {and_eg.text}")
# #or oper:
# or_eg = driver.find_element(By.XPATH,"//td[text()='Tim' or text()='Frank']")
# print(f"OR -- found BOTH condition: {or_eg.text}")
#
#

# #child: select all id elements (dir child of row)
# rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr/td")
# print(f"Child Eg FOUND: {len(rows)} columns in first table. ")
#
# #parents:(to get parent row of particular cell)
# email_cell = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='jdoe@hotmail.com']")
# parent_row = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='jdoe@hotmail.com']/parent::tr")
#
# print(f"Parent eg -- email: '{email_cell.text}' belongs to row with frst name: "
#       f"{parent_row.find_element(By.XPATH,'./td[2]').text}")
#

# #ancestor:
# ancestor_table = driver.find_element(By.XPATH,"//td[text()='jsmith@gmail.com']/ancestor::table")
# print(f"Ancestor eg - Table ID: {ancestor_table.get_attribute('id')}")
#
# #desendant:
# descendants = driver.find_elements(By.XPATH,"//table[@id='table1']/descendant::td")
# print(f"Descendant eg - FOUND: {len(descendants)} descendants cells.")

#relative locator

driver.get("https://www.saucedemo.com/")
time.sleep(3)

username = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.ID,"password")
login = driver.find_element(By.ID,"login-button")

#above
ele_above_password = driver.find_element(
    locate_with(By.TAG_NAME,"input").above(password)
)
print(f"Above eg -- text above password: {ele_above_password.get_attribute('placeholder')}")
ele_above_password.send_keys('standard_user')
time.sleep(3)

#below
ele_below_username = driver.find_element(
    locate_with(By.TAG_NAME,"input").below(username)
)
print(f"Below eg -- placeholder below username: {ele_below_username.get_attribute('placeholder')}")
ele_below_username.send_keys('secret_sauce')
time.sleep(3)
login.click()
time.sleep(2)

# right
twitter_ico = driver.find_element(By.LINK_TEXT,"Twitter")
facebook_ico = driver.find_element(locate_with(By.TAG_NAME,"a").to_right_of(twitter_ico))
print(f"The right side of twitter icon is: {facebook_ico.get_attribute('href')}")

# to left of
left_ico = driver.find_element(locate_with(By.TAG_NAME,"a").to_left_of(facebook_ico))
print(f"The left of the icon is: {left_ico.get_attribute('href')}")

#near
near_ico= driver.find_element(locate_with(By.TAG_NAME,"a").near(facebook_ico))

print(f"Near Element: {near_ico.get_attribute('href')}")
time.sleep(5)

driver.quit()

