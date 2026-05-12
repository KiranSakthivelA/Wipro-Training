from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = input("Enter the desired browser: ")
match(browser.lower()):
    case 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    case 'edge':
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

    case _:
        print('Browser select properly!!!')

driver.get("https://www.google.com")

pagetitle = driver.title

if pagetitle == 'Google':
    print('Google HomePage loaded = Pass!!')

else:
    print('FAILED!!')

sleep(10)

driver.quit()