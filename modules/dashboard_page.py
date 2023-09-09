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
class DashboardPage(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        "dashboard_header": ('XPATH', '//h6[text()="Dashboard"]'),
        "punch_header_text": ('XPATH', '//p[text()="Punched In"]'),
        "my_actions_header_text": ('XPATH', '//p[text()="My Actions"]'),
        "quick_launch_header_text": ('XPATH', '//p[text()="Quick Launch"]'),
        "chart_emp_dist_title": ('XPATH', '//p[text()="Employee Distribution by Sub Unit"]'),
        "button_punch":('XPATH', '//i[@class="oxd-icon bi-stopwatch"]')
    }

    def dashboard_verify(self):
        assert self.dashboard_header.text == "Dashboard"
        assert self.punch_header_text.text == "Punched In"
        assert self.my_actions_header_text.text == "My Actions"
        assert self.quick_launch_header_text.text == "Quick Launch"
        self.driver.execute_script("window.scrollTo(0, 500)")
        wait_for_clickable_element(self.driver, 50, "//span[@title='Engineering']")

    def dashboard_click_links(self):
        wait_for_visibility_element(self.driver, 50, "//p[text()='Employee Distribution by Sub Unit']")
        assert self.chart_emp_dist_title.text == "Employee Distribution by Sub Unit"
        dash_links=self.driver.find_elements(By.XPATH, "//span[@class='oxd-text oxd-text--span']")
        for dash_link in dash_links:
            dash_link.click()

        
