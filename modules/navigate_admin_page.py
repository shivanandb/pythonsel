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
        print("1")
        assert self.driver.find_element(By.XPATH, "//h6[text()='Admin']").text == "Admin"
        print("2")
        assert self.driver.find_element(By.XPATH, "//h6[text()='User Management']").text == "User Management"
        print("3")

    def click_and_verify_user_management(self):
        self.user_mgmt.click_button()
        wait_for_clickable_element(self.driver, 60, "//a[text()='Users']")
        assert self.driver.find_element(By.XPATH, "//a[text()='Users']").text == "Users"

    def click_and_verify_job(self):
        self.job_header.click_button()
        print("1")
        wait_for_clickable_element(self.driver, 120, "//a[text()='Job Titles']")
        print("2")
        job_headers=self.driver.find_elements(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
        print("3")
        for job_header_text in job_headers:
            print(job_header_text.text)
            print("4")
            #assert job_header_text.text in ['Job Titles', 'Pay Grades', 'Employment Status', 'Job Categories', 'Work Shifts']
            print("5")
        
    def verify_admin_header(self):
        header_menu_items=self.driver.find_elements(By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item']")
        for header_menu_item in header_menu_items:
            print(header_menu_item.text)
            assert header_menu_item.text in ['User Management', 'Job', 'Organization', 'Qualifications', 'More']
    
    def add(self):
        wait_for_clickable_element(self.driver, 30, "//button[text()=' Add ']")
        self.add_button.click_button()
        assert self.driver.find_element(By.XPATH, "//h6[text()='Add User']").text == "Add User"
            
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
