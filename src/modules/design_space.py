import time
from modules.provide_values_input_page import *
from selenium.webdriver.support.ui import WebDriverWait
from common.common_methods import *
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.action_chains import ActionChains
config_variables = load_config_file()
SCALING_PARAMETER_INDEX=0
SCALING_PARAMETER_OTR=0
AGITATION_INDEX=1
AERATION_INDEX=2 
"""
Contains logic for verifying few text fields in results page
"""
class DesignSpacePage(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        "design_space_tab":('XPATH','//a[text()=" Design Space "]'),
        "simulation_header":('XPATH','//span[text()="Simulations table"]'),
        "apply_button":('XPATH','//button[@type="submit"]'),
        "close_button":('XPATH','//button[@class="btn close-btn tertiary_outline_btn_icon"]'),
        "summary_tab":('XPATH','//a[text()=" Summary "]'),
        "free_user_design_space_text":('XPATH','(//div[@class="d-flex justify-content-center align-items-center"])[4]'),
        "free_user_design_space_contact":('XPATH','//div[@class="d-flex justify-content-center align-items-center my-2"]'),
        "contact_email_id":('XPATH','(//a[@class="pagelink"])[4]')
    }
            
    def navigate_to_design_space_and_edit_constraints(self):
        if(config_variables["is_premium"]=="True"):#This code executes if user is premium
            self.driver.execute_script("window.scrollTo(0, -1000)")
            daywise_pages=self.driver.find_elements(By.XPATH, "//li[@class='nav-item ng-star-inserted']")
            get_tabs_count_actual=len(daywise_pages)-1
            for item in range(get_tabs_count_actual):
                wait_for_visibility_element(self.driver, 50, "(//a[@class='nav-link notDisabledTab active'])[1]")
                ActionChains(self.driver).move_to_element(daywise_pages[item+1]).click(daywise_pages[item+1]).perform()
                wait_for_visibility_element(self.driver, 100, "//a[text()=' Results ']")
                design_space_tab=self.driver.find_element(By.XPATH, "//a[text()=' Design Space ']")
                ActionChains(self.driver).click(design_space_tab).perform()
                design_space_constraint=self.driver.find_element(By.XPATH, "//span[text()='Design space constraints']")
                while design_space_constraint.is_displayed()==True:
                    ActionChains(self.driver).click(design_space_tab).perform()
                    break
                wait_for_visibility_element(self.driver, 50, "//span[text()='Design space constraints']")
                edit_buttons=self.driver.find_elements(By.XPATH, "//span[text()='Edit']")
                #Below click operation is for Scaling parameters - Design space constraints
                self.edit_constraint(edit_buttons, SCALING_PARAMETER_INDEX)
                self.enable_constraint_radio_button(SCALING_PARAMETER_OTR)
                self.move_constraint_slider( "//span[@class='ngx-slider-span ngx-slider-pointer ngx-slider-pointer-max']", "//button[@type='submit']")
                
        else:#This code executes if user is not premium
            self.driver.execute_script("window.scrollTo(0, -1000)")
            print("1")
            wait_for_visibility_element(self.driver, 150, "//a[text()=' Results ']")
            design_space_tab=self.driver.find_element(By.XPATH, "//a[text()=' Design Space ']")
            ActionChains(self.driver).click(design_space_tab).perform()
            wait_for_clickable_element(self.driver, 50, "(//div[@class='d-flex justify-content-center align-items-center'])[4]")
            assert self.free_user_design_space_text.get_text()==config_variables["free_user_design_space_message"]
            print("2")
            wait_for_clickable_element(self.driver, 50, "(//div[@class='d-flex justify-content-center align-items-center'])[4]")
            contact_element = self.driver.find_element(By.XPATH, "(//a[@class='pagelink'])[4]")
            assert contact_element.is_displayed()==True
            print("3")
            wait_for_clickable_element(self.driver, 60, "(//a[@class='pagelink'])[4]")
            assert self.contact_email_id.get_text()==config_variables["email_address_free_user"]
            print("4")
    
    def edit_constraint(self, edit_buttons, index):
        edit_buttons[index].click()
        
    def enable_constraint_radio_button(self, index):
        if index ==AGITATION_INDEX or index ==AERATION_INDEX:
            wait_for_clickable_element(self.driver,30, "(//span[@class='mat-slide-toggle-thumb-container'])[1]")
            self.driver.find_element(By.XPATH, "(//span[@class='mat-slide-toggle-thumb-container'])[1]").click()
              
    def move_constraint_slider(self, slider_path, submit_btn):
        move = ActionChains(self.driver)
        slider_button=self.driver.find_elements(By.XPATH, slider_path)
        move.click_and_hold(slider_button[0]).move_by_offset(1, 0).release().perform()
        self.driver.find_element(By.XPATH, submit_btn).click()
        wait_for_clickable_element(self.driver, 20, submit_btn)
        self.close_button.click_button()
        wait_for_visibility_element(self.driver, 20, "//span[text()='Simulations table']")

    def navigate_summary_page(self):
            self.driver.execute_script("window.scrollTo(0, -1000)")
            wait_for_clickable_element(self.driver, 20, "//a[text()=' Summary ']")
            self.summary_tab.click_button()
    
    def save_design_space_simulation(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[@class='action-button icon_save_black']").click()
        wait_for_clickable_element(self.driver, 500, "//span[@class='action-button delete icon_delete']")
        assert self.driver.find_element(By.XPATH, "(//strong[contains(text(),'saved as Target - Simulation')])[1]").text == "Min Agitation saved as Target - Simulation 2"
        
    def verify_design_space_simulation(self):
        WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, "(//strong[contains(text(),'saved as Target - Simulation')])[1]")))
        self.driver.execute_script("window.scrollTo(0, 1000)")
        assert self.driver.find_element(By.XPATH, "//span[text()='Saved Simulations']").text == "Saved Simulations"
        text_simulation=self.driver.find_element(By.XPATH, "//span[text()='Target - Simulation 2']").text
        assert text_simulation== "Target - Simulation 2"        
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ag-selection-checkbox'])[4]"))).click()
        assert self.driver.find_element(By.XPATH, "//*[name()='svg']//*[local-name()='g']//*[local-name()='path' and @class='highcharts-tracker-line']").is_displayed()==True
        self.driver.execute_script("window.scrollTo(0, -1000)")
        assert self.driver.find_element(By.XPATH, "//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and text()='Target - Simulation 2']").text == "Target - Simulation 2"