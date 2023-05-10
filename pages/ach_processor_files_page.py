from time import sleep
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.ach_processor_files_locators import AchProcessorFilesLocators

class AchProcessorFilesPage():
    URL = 'http://localhost:9002/admin-console/achpro/index'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def set_cutoff_for_next_minute(self):
        first_file = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AchProcessorFilesLocators.first_file))
        first_file.click()

        now = datetime.now()
        cutoff = now + timedelta(minutes=1)
        cutoff = cutoff.replace(second=0, microsecond=0)
        date_string = cutoff.strftime("%d/%m/%Y")
        time_string = cutoff.strftime("%H:%M")
        
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AchProcessorFilesLocators.div_modal))
        cutoff_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AchProcessorFilesLocators.cutoff_field))
        cutoff_field.send_keys(date_string + Keys.ARROW_RIGHT + time_string)

        save_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AchProcessorFilesLocators.btn_modal))
        save_btn.click()

        sleep((cutoff - now).total_seconds())

        first_file_id = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AchProcessorFilesLocators.first_file_id))
        return first_file_id.get_attribute("text")
