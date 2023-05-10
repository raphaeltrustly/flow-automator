from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.ach_simulator_payments_locators import AchSimulatorPaymentsLocators

class AchSimulatorPaymentsPage():
    URL = 'http://localhost:7003/ach-crb-simulator/payment'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def get_event_id_by_ptx(self, ptx):
        table = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AchSimulatorPaymentsLocators.table))
        rows = WebDriverWait(table, 10).until(EC.presence_of_all_elements_located(AchSimulatorPaymentsLocators.rows))
        for row in rows:
            cols = WebDriverWait(row, 10).until(EC.presence_of_all_elements_located(AchSimulatorPaymentsLocators.cols))
            if (cols[2].text == ptx):
                return cols[0].text
