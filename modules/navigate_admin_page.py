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
        "job_header":('XPATH', '//span[text()="Job "]')
    }

    def search_and_choose_admin(self):
        self.input_search.set_text("Admin")
        wait_for_clickable_element(self.driver, 20, "//span[text()='Admin']")
        self.admin_page_link.click_button()
        wait_for_visibility_element(self.driver, 30, "//h6[text()='Admin']")
        assert self.driver.find_element(By.XPATH, "//h6[text()='Admin']").text == "Admin"
        assert self.driver.find_element(By.XPATH, "//h6[text()='User Management']").text == "User Management"
        
    def verify_admin_header(self):
        menu_main=self.driver.find_elements(By.XPATH, "//ul[@class='oxd-main-menu']")
        for each_menu_main in menu_main:
            print(each_menu_main.text)
        header_menu_items=self.driver.find_elements(By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item']")
        for header_menu_item in header_menu_items:
            assert header_menu_item.text in ['User Management', 'Job', 'Organization', 'Qualifications', 'More']
        #self.job_header.click_button()
        #wait_for_clickable_element(self.driver, 100, "//span[text()='Job ']")
        #job_header_items=self.driver.find_elements(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
        #for job_header_item in job_header_items:
        #    assert job_header_item in ['Job Titles', 'Pay Grades', 'Employment Status', 'Job Categories', 'Work  Shifts']

    def add(self):
        self.add_button.click_button()
        assert self.driver.find_element(By.XPATH, "//h6[text()='Add User']").text == "Add User"
        #self.driver.find_element(By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[1]").click()
        #wait_for_clickable_element(self.driver, 30, "//div[text()='Admin']")
        #self.driver.find_element(By.XPATH, "//div[text()='Admin']").click()
            
    def verify_about(self):
        self.driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
        profile_items=self.driver.find_elements(By.XPATH, "//a[@class='oxd-userdropdown-link']")
        for profile_item in profile_items:
            assert profile_item in ['About', 'Support', 'Change Password', 'Logout']
