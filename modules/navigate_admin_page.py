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
class HomePage(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        "input_search": ('XPATH', '//input[@class="oxd-input oxd-input--active"]'),
        "admin_page_link":('XPATH', '//span[text()="Admin"]'),
        "add_button":('XPATH', '//button[text()=" Add "]')
    }

    def search_and_choose_admin(self):
            self.input_search.set_text("Admin")
            wait_for_clickable_element(self.driver, 20, "//span[text()='Admin']")
            self.admin_page_link.click_button()
            wait_for_visibility_element(self.driver, 30, "//h6[text()='Admin']")
            assert self.driver.find_element(By.XPATH, "//h6[text()='Admin']").text == "Admin"
            assert self.driver.find_element(By.XPATH, "//h6[text()='User Management']").text == "User Management"
            self.add_button.click_button()
            