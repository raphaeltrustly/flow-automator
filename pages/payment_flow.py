from time import sleep
from pages.login_page import LoginPage
from pages.globex_page import GlobexPage
from pages.login_ach_page import LoginAchPage
from pages.ach_simulator_payments_page import AchSimulatorPaymentsPage
from pages.ach_simulator_event_page import AchSimulatorEventPage
from pages.ach_processor_file_page import AchProcessorFilePage
from pages.ach_processor_files_page import AchProcessorFilesPage
from pages.fi_gateway_processor_page import FiGatewayProcessorPage

class PaymentFlow():

    
    #custom_data = {'country': "CA"}
    #selected_bank = {'name': "Demo Bank of Canada"} # CA
    custom_data = {}
    selected_bank = {'name': "DEMO BANK"} # US
    bank_credentials = {'username': "a", 'password': "a"}
    login_data = {'username': "admin", 'password': "superadmin"}



    def __init__(self, driver):
        self.globex = GlobexPage(driver)
        self.login_page = LoginPage(driver)
        self.login_ach_page = LoginAchPage(driver)
        self.ach_processor_file = AchProcessorFilePage(driver)
        self.ach_processor_files = AchProcessorFilesPage(driver)
        self.ach_simulator_event = AchSimulatorEventPage(driver)
        self.ach_simulator_payments = AchSimulatorPaymentsPage(driver)
        self.fi_gateway_processor_page = FiGatewayProcessorPage(driver)

    def pay(self):
        self.__create_transaction(self.custom_data)
        self.__authenticate() # always
        file_id = self.__update_cutoff()
        ptx_list = self.__find_all_trx_ptx(file_id)
        self.__run_ach_processor()
        # Simulator
        self.__authenticate_crb_simulator()
        self.__simulate_event_in_crb(ptx_list, 'Sent')
        self.__simulate_event_in_crb(ptx_list, 'Received')
        # self.__simulate_event_in_crb(ptx_list, 'Rejected') # return by R01 (fixed)
        


    def __create_transaction(self, custom_data):
        self.globex.load()
        if (len(custom_data) > 0):
            self.globex.fill_custom_data(custom_data)
        self.globex.show_bank_list()
        self.globex.select_bank(self.selected_bank)
        sleep(4)
        self.globex.bank_login(self.bank_credentials)
        
    def __authenticate(self):
        self.login_page.load()
        self.login_page.authenticate(self.login_data)
        sleep(3)

    def __update_cutoff(self):
        self.ach_processor_files.load()
        return self.ach_processor_files.set_cutoff_for_next_minute()

    def __run_ach_processor(self):
        self.fi_gateway_processor_page.load()
        self.fi_gateway_processor_page.run_ach_processor()

    def __find_all_trx_ptx(self, file_id):
        self.ach_processor_file.load(file_id)
        return self.ach_processor_file.find_all_transaction_ptx()
    
    def __authenticate_crb_simulator(self):
        self.login_ach_page.load()
        self.login_ach_page.authenticate(self.login_ach_page)

    def __simulate_event_in_crb(self, ptx_list, event):
        event_ids = []
        for ptx in ptx_list:
            self.ach_simulator_payments.load()
            event_ids.append(self.ach_simulator_payments.get_event_id_by_ptx(ptx)) 
            sleep(1)           

        for event_id in event_ids:
            self.ach_simulator_event.load(event_id)
            self.ach_simulator_event.process(event)

        self.__run_ach_processor()
