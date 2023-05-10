import pytest

from time import sleep
from pages.payment_flow import PaymentFlow
from selenium.webdriver import Chrome

@pytest.fixture
def driver():
    driver = Chrome()

    yield driver

    driver.quit()

def test_basic_payment_flow(driver):
    flow_page = PaymentFlow(driver)
    flow_page.pay()
    sleep(3)