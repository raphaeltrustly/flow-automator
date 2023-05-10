from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.ach_processor_file_locators import AchProcessorFileLocators

class AchProcessorFilePage():
    URL = "http://localhost:9002/admin-console/achproEntries?fileId="

    def __init__(self, driver):
        self.driver = driver

    def load(self, file_id):
        self.driver.get(self.URL + file_id)
    
    def find_all_transaction_ptx(self):
        ptx_list = []
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AchProcessorFileLocators.trx_table))
        for table in self.driver.find_elements(By.XPATH, '//*[@id="sortabletable"]/tbody/tr/td[4]'):
            if (table.text.startswith("ptx")):
                ptx_list.append(table.text)

        return ptx_list
