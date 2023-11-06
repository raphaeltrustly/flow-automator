from selenium.webdriver.common.by import By

class AchProcessorFilesLocators():
    first_file = (By.XPATH, '//*[@id="sortabletable"]/tbody/tr[1]/td[11]/a')
    cutoff_field = (By.ID, 'cutoffDate')
    div_modal = (By.ID, 'modalUpdateFile')
    btn_modal = (By.XPATH, '//*[@id="modalUpdateFile"]/div/div/div[4]/button[1]')
    first_file_id = (By.XPATH, '//*[@id="sortabletable"]/tbody/tr[1]/td[1]/a')
    
