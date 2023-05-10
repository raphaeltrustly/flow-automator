from selenium.webdriver.common.by import By

class GlobexLocators():
    custom_data_select = (By.NAME, "customer")
    vip_input = (By.ID, "vip")
    custom_data_button = (By.ID, "customer-set")
    bank_list_frame = (By.ID, "paywithmybank-iframe-widget-container")
    bank_list_button = (By.ID, "wdt-bankTiles-openAllBanks")
    select_bank_frame = (By.ID, "paywithmybank-iframe")
    bank_name_input = (By.ID, "lbx-listBank-inputSearch")
    selected_bank_div = (By.ID, 'lbx-listBank-select200005501')
    bank_data_frame = (By.ID, "paywithmybank-iframe")
    popup_frame = (By.ID, "slider-button")
    login_frame = (By.ID, "lbx-iframeAuthenticate")
    username_input = (By.ID, "lbx-formAuthenticate-authFields-inputusername")
    password_input = (By.ID, "lbx-formAuthenticate-authFields-inputpassword")
    account_frame = (By.ID, "paywithmybank-iframe")
    submit_buttom = (By.ID, "lbx-accountList-submit")
