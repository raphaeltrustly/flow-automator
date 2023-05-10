from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.login_ach_locators import LoginAchLocators

class LoginAchPage():
    URL = 'http://localhost:7003/ach-crb-simulator/'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def authenticate(self, login_data):
        user_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginAchLocators.user_input))
        pass_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginAchLocators.pass_input))
        user_input.send_keys('admin')
        pass_input.send_keys('superadmin' + Keys.ENTER)