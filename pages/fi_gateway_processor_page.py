from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.fi_gateway_processor_locators import FiGatewayProcessorLocators

class FiGatewayProcessorPage():
    URL = 'http://localhost:9002/admin-console/services/figatewayprocessor'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def run_ach_processor(self):
        ach_processor_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(FiGatewayProcessorLocators.ach_processor_btn))
        ach_processor_btn.click()