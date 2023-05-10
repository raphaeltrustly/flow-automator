from selenium.webdriver.common.by import By

class LoginAchLocators():
    user_input = (By.XPATH, "//input[@name='userId']")
    pass_input = (By.CSS_SELECTOR, 'body > div > div.row > div > form > div:nth-child(4) > div > input')