import logger

from features.steps.signup_locators import SignupLocators
from utils.waits import WaitUtils
from utils.logger import LogGen

logger = LogGen.loggen()

class SignupPage:
    def __init__(self, driver):
        self.driver = driver



    def click_signup_menu(self):
        logger.info("Clicking Login Menu")
        WaitUtils.wait_for_element_clickable(
            self.driver, SignupLocators.SIGNUP_MENU
        ).click()

    def enter_username(self, username):
        logger.info(
            f"Entering Username : {username}"
        )
        element = WaitUtils.wait_for_element_visible(
            self.driver,
            SignupLocators.USERNAME
        )
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        logger.info("Entering Password")
        element = WaitUtils.wait_for_element_visible(
            self.driver,
            SignupLocators.PASSWORD
        )
        element.clear()
        element.send_keys(password)

    def click_login_button(self):
        logger.info("Clicking Login Button")
        WaitUtils.wait_for_element_clickable(
            self.driver,
            SignupLocators.LOGIN_BUTTON
        ).click()