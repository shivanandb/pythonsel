import base64
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from common.common_methods import *
from selenium.webdriver.common.action_chains import ActionChains

"""
Contains logic for launching chrome browser and login with valid credentials
"""
class LoginPage(PageFactory):

    def __init__(self,driver):
        self.driver = driver

    locators = {
        "sct_userName": ('NAME', 'username'),
        "sct_password": ('NAME', 'password'),
        "sign_in_button":('XPATH', '//button[text()=" Login "]')
    }
         
    def login(self):
        config_variables = load_config_file()

        wait_for_clickable_element(self.driver, 30, "//button[text()=' Login ']")

        username=config_variables["premium_user_name"]

        user_password = config_variables["premium_user_password_encrypted"]

        self.sct_userName.set_text(username)              
        asciiPassword = user_password.encode('ascii')
        decryptPassword = base64.b64decode(asciiPassword)
        decodePassword = decryptPassword.decode('ascii')
        self.sct_password.set_text(decodePassword)
        self.sign_in_button.click_button()
        wait_for_visibility_element(self.driver, 50, "//h6[text()='Dashboard']")
        #assert self.driver.find_element(By.XPATH, "//p[text()='Paul Collings']").text == "Paul Collings"

