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
class AboutPage(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        "input_search": ('XPATH', '//input[@class="oxd-input oxd-input--active"]'),
        "admin_page_link":('XPATH', '//span[text()="Admin"]'),
        "add_button":('XPATH', '//button[text()=" Add "]'),
        "job_header":('XPATH', '//span[text()="Job "]'),
        "user_mgmt":('XPATH', '//span[text()="User Management "]')
    }
            
    def verify_about(self):
        wait_for_clickable_element(self.driver, 50, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
        self.driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
        wait_for_clickable_element(self.driver, 50, "(//a[@class='oxd-userdropdown-link'])[1]")
        profile_items=self.driver.find_elements(By.XPATH, "//a[@class='oxd-userdropdown-link']")
        for profile_item in profile_items:
            assert profile_item.text in ['About', 'Support', 'Change Password', 'Logout']
    
    def verify_each_menu(self):
        menu_main=self.driver.find_elements(By.XPATH, "//ul[@class='oxd-main-menu']")
        for each_menu_main in menu_main:
            if(each_menu_main.text == "Directory"):
                self.driver.execute_script("window.scrollTo(0, -1000)")
            assert each_menu_main.text in ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Claim', 'Buzz']

    def check_collapse(self):
        self.driver.find_element(By.XPATH, "//button[@class='oxd-icon-button oxd-main-menu-button']").click()
        self.driver.find_element(By.XPATH, "//button[@class='oxd-icon-button oxd-main-menu-button']").click()
