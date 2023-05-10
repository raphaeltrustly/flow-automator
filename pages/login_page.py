from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.login_locators import LoginLocators

class LoginPage():
    URL = 'http://localhost:9002/admin-console/home/index'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def authenticate(self, login_data):
        user_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginLocators.user_input))
        pass_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginLocators.pass_input))
        user_input.send_keys(login_data["username"])
        pass_input.send_keys(login_data["password"] + Keys.ENTER)
