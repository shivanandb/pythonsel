from modules.provide_values_input_page import *
from common.common_methods import *
from seleniumpagefactory.Pagefactory import PageFactory

"""
Contains logic for verifying few text fields in results page
"""
class HomePage(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        "home_btn":('XPATH','//span[text()="Home"]'),
        "help_link":('XPATH','//span[text()="Help"]'),
        "notification_link":('XPATH','//span[text()="Notifications"]'),
        "logout_link":('XPATH','//span[text()="Logout"]')
    }
    def verify_presence_of_header_menu_elements(self):
        config_variables = load_config_file()
        if(config_variables["is_premium"]==True):
            wait_for_clickable_element(self.driver, 50, "//button[text()='New calculation']")
            assert self.home_btn.get_text()=="Home"
        assert self.help_link.get_text()=="Help"
        assert self.notification_link.get_text()=="Notifications"
        assert self.logout_link.get_text()=="Logout"