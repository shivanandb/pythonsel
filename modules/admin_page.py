import time
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
        "add_button":('XPATH', '//button[text()=" Add "]'),
        "job_header":('XPATH', '//span[text()="Job "]'),
        "user_mgmt":('XPATH', '//span[text()="User Management "]')
    }

    def search_and_choose_admin(self):
        self.input_search.set_text("Admin")
        wait_for_clickable_element(self.driver, 20, "//span[text()='Admin']")
        self.admin_page_link.click_button()
        wait_for_visibility_element(self.driver, 30, "//h6[text()='Admin']")
        assert self.driver.find_element(By.XPATH, "//h6[text()='Admin']").text == "Admin"
        assert self.driver.find_element(By.XPATH, "//h6[text()='User Management']").text == "User Management"

    def click_and_verify_user_management(self):
        self.user_mgmt.click_button()
        wait_for_clickable_element(self.driver, 60, "//a[text()='Users']")
        assert self.driver.find_element(By.XPATH, "//a[text()='Users']").text == "Users"
        self.user_mgmt.click_button()
    
    def verify_help_button(self):
        wait_for_clickable_element(self.driver, 40, "//button[@title='Help']")
        self.driver.find_element(By.XPATH, "//button[@title='Help']").click()
        p = self.driver.current_window_handle
        #obtain parent window handle
        parent = self.driver.window_handles[0]
        #obtain browser tab window
        chld = self.driver.window_handles[1]
        #switch to browser tab
        self.driver.switch_to.window(chld)
        print("Page title for browser tab:")
        print(self.driver.title)
        #//button[@title='Help']

    def verify_admin_header(self):
        header_menu_items=self.driver.find_elements(By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item']")
        for header_menu_item in header_menu_items:
            assert header_menu_item.text in ['User Management', 'Job', 'Organization', 'Qualifications', 'More']
    
    def add(self):
        wait_for_clickable_element(self.driver, 30, "//button[text()=' Add ']")
        self.add_button.click_button()
        assert self.driver.find_element(By.XPATH, "//h6[text()='Add User']").text == "Add User"