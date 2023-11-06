from time import sleep
from pages.payment_flow import PaymentFlow
from selenium.webdriver import Chrome

def run_payment_flow():
    driver = Chrome()
    flow_page = PaymentFlow(driver)
    flow_page.pay()
    sleep(3)
    driver.quit()

run_payment_flow()
