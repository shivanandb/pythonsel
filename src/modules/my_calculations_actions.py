from modules.provide_values_input_page import *
from common.common_methods import *
from seleniumpagefactory.Pagefactory import PageFactory

"""
Contains logic for verifying few text fields in results page
"""
class MyCalculationsPage(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        "home_btn":('XPATH','//span[text()="Home"]'),
        "home_header":('XPATH','//span[text()="My calculations"]'),
        "copy_icon":('XPATH','//span[@class="icon_copy"]'),
        "copy_header_text":('XPATH','//strong[text()="Copy as"]'),
        "copy_name":('ID','copyCalculation'),
        "copy_button":('XPATH','//span[text()="Copy"]'),
        "copy_success":('XPATH','//strong[text()="Copy successful"]')
    }
        
    def navigate_to_my_calculations(self):
            self.driver.execute_script("window.scrollTo(0, -1000)")
            self.home_btn.click_button()
            assert self.home_header.get_text()=="My calculations"
        
    def perform_copy_calculation(self):
            menu = self.driver.find_elements(By.XPATH, "//div[@class='more_vert']")
            menu[0].click()
            self.copy_icon.click_button()
            assert self.copy_header_text.get_text()=="Copy as"
            self.copy_name.clear_text()
            self.copy_name.set_text("test_smoke")
            self.copy_button.click_button()
            wait_for_visibility_element(self.driver, 30, "//strong[text()='Copy successful']")
            assert self.copy_success.get_text()=="Copy successful" #assert the copy success banner text message