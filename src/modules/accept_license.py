from seleniumpagefactory.Pagefactory import PageFactory
from common.common_methods import *
from selenium.common.exceptions import NoSuchElementException
"""
Contains logic for accepting Terms and conditions 
"""
class License(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
            "proceed_button": ('XPATH', '//input[@id="proceed"]'),
            "agree_and_proceed": ('XPATH', '//span[text()="Agree and proceed"]')
        }
    def click_accept_license(self):

            try:
                proceed_checkbox = self.driver.find_element(By.XPATH, "//input[@id='proceed']")
                wait_for_clickable_element(self.driver, 30, "//input[@id='proceed']")
                self.proceed_button.click_button()
                wait_for_clickable_element(self.driver, 30, "//span[text()='Agree and proceed']")
                self.agree_and_proceed.click_button()
            except NoSuchElementException:
                print("User already accepted terms and condition in last login, if needed it should be reset from Api")
