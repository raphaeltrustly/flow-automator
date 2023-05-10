from selenium.webdriver.common.by import By

class AchSimulatorEventLocators():
    actions_select = (By.ID, "paymentStatus")
    submit = (By.ID, "submit")
    return_code_input = (By.ID, 'statusReturnCode')
