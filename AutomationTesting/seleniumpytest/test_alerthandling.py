import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    yield driver
    driver.quit()

def test_simple_js_alert(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    alert= driver.switch_to.alert
    assert alert.text == "I am a JS Alert", 'Alert text was wrong'
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "You successfully clicked an alert" in result, 'Result text was wrong'

