from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.ach_simulator_event_locators import AchSimulatorEventLocators

class AchSimulatorEventPage():
    URL = 'http://localhost:7003/ach-crb-simulator/event?id='

    def __init__(self, driver):
        self.driver = driver

    def load(self, event_id):
        self.driver.get(self.URL + event_id)

    def process(self, event):
        actions_select = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AchSimulatorEventLocators.actions_select))
        select = Select(actions_select)
        if (event is 'Returned'):
            select.select_by_visible_text('Returned')

            return_code_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AchSimulatorEventLocators.return_code_input))
            return_code_input.send_keys('R01')
        else:
            select.select_by_visible_text(event)

        submit_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AchSimulatorEventLocators.submit))
        submit_btn.click()
        sleep(1)
