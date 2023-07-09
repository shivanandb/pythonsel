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
        "sct_userName": ('ID', 'loginPage:loginForm:userName'),
        "sct_password": ('ID', 'loginPage:loginForm:sfid-password'),
        "sign_in_button":('ID', 'loginPage:loginForm:login-submit')
    }
         
    def login(self):
        config_variables = load_config_file()
        if(config_variables["is_premium"]=="True"):
            username=config_variables["premium_user_name"]
            user_password = config_variables["premium_user_password_encrypted"]
        else:
            username=config_variables["free_user_name"]
            user_password = config_variables["free_user_password_encrypted"]
            
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, 'loginPage:loginForm:login-submit')))
        self.sct_userName.set_text(username)              
        asciiPassword = user_password.encode('ascii')
        decryptPassword = base64.b64decode(asciiPassword)
        decodePassword = decryptPassword.decode('ascii')
        self.sct_password.set_text(decodePassword)
        self.sign_in_button.click_button()
