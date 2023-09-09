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
class TimePage(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        "button_punch":('XPATH', '//i[@class="oxd-icon bi-stopwatch"]')
    }

    def verify_punch(self):
        self.driver.execute_script("window.scrollTo(0, -500)")
        self.button_punch.click()
        wait_for_visibility_element(self.driver, 100, "//h6[text()='Attendance']")
        self.driver.find_element(By.XPATH, "//span[text()='Timesheets ']").click()
        wait_for_clickable_element(self.driver, 100, "//a[text()='My Timesheets']")
        timesheet_items=self.driver.find_elements(By.XPATH, "//a[@role='menuitem']")
        for timesheet_item in timesheet_items:
            assert timesheet_item.text in ['My Timesheets', 'Employee Timesheets']


        
