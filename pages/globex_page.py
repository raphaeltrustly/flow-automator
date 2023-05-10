from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.globex_locators import GlobexLocators

class GlobexPage():
    URL = 'http://localhost:7000/merchant-demo/globex'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def fill_custom_data(self, custom_data):
        # Seleciona o User: Custom
        custom_data_select = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.custom_data_select))
        user_select = Select(custom_data_select)
        user_select.select_by_visible_text('Custom')
        
        # Preenche os dados
        vip_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.vip_input))
        vip_input.send_keys(custom_data["vipTier"])

        # Clica em Set
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.custom_data_button)).click()

    def show_bank_list(self):
        # Pega o iframe dos bancos
        iframe = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.bank_list_frame))
        self.driver.switch_to.frame(iframe)

        # Clica para mostrar todos os bancos
        open_all_banks_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.bank_list_button))
        open_all_banks_btn.click()

        self.driver.switch_to.default_content()

    def select_bank(self, selected_bank):
        # Pega o iframe da listagem
        bank_list_frame = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.select_bank_frame))
        self.driver.switch_to.frame(bank_list_frame)

        # Digita o nome do banco
        bank_name_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.bank_name_input))
        bank_name_input.send_keys(selected_bank + Keys.ENTER)

        selected_bank_div = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.selected_bank_div))
        selected_bank_div.send_keys(Keys.ENTER)

        self.driver.switch_to.default_content()

    def bank_login(self, bank_credentials):
        # Pega o iframe dos dados bancários
        bank_data_frame = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.bank_data_frame))
        self.driver.switch_to.frame(bank_data_frame)

        # Recusa o popup
        popup_frame = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.popup_frame))
        popup_frame.click()

        # Pega o iframe do login
        loginFrame = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.login_frame))
        self.driver.switch_to.frame(loginFrame)

        username_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.username_input))
        username_input.send_keys(bank_credentials["username"])
        password_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.password_input))
        password_input.send_keys(bank_credentials["password"] + Keys.ENTER)

        account_frame = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.account_frame))
        self.driver.switch_to.frame(account_frame)

        submit_buttom = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GlobexLocators.submit_buttom))
        submit_buttom.click()