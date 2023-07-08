from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.common_methods import *
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.action_chains import ActionChains
import time
"""
Contains logic for performing a New calcualtion
"""
class NewCalculationPage(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        "new_calculation_xpath": ('XPATH', '//button[text()="New calculation"]'),
        "verify_new_calculation": ('XPATH', '//strong[text()="New calculation name"]'),
        "fill_new_calculation_name": ('XPATH', '//input[@id="newCalculationId"]'),
        "confirm_new_calculation": ('XPATH', '(//span[text()="Confirm"])[2]'),
    }

    def create_new_calculation(self):
            wait_for_clickable_element(self.driver, 30, "//button[text()='New calculation']")
            self.driver.execute_script("window.scrollTo(0, -1000)")
            self.new_calculation_xpath.click_button()
            wait_for_clickable_element(self.driver, 30, "//strong[text()='New calculation name']")
            assert self.verify_new_calculation.get_text() =="New calculation name"
            self.fill_new_calculation_name.clear_text()
            config_variables = load_config_file()
            self.fill_new_calculation_name.set_text(config_variables['new_calculation_name'])
            self.confirm_new_calculation.click_button()
            wait_for_clickable_element(self.driver, 30, "//select[@id='bioreactornameRefId']")