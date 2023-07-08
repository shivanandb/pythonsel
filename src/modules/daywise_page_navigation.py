from modules.provide_values_input_page import *
from modules.verify_results_summary_page import *
from selenium.webdriver.support.ui import WebDriverWait
from common.common_methods import *
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.action_chains import ActionChains
config_variables = load_config_file()
input_values = load_input_values_json_file()
"""
Contains logic for verifying few text fields in results page
"""
class DaywisePage(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        "verify_summary_tab": ('XPATH', '//a[text()=" Summary "]'),
        "update_button":('XPATH', '(//button[@class="btn primary_btn_icon"])[2]'),
        "export_btn":('XPATH','//span[text()="Export"]'),
        "update_button_cancel":('XPATH','(//button[text()=" Cancel "])[1]'),
        "day1_tab":('XPATH','//a[text()=" Day 0 "]'),
        "results_tab":('XPATH','//a[text()=" Results "]'),
        "design_space_tab":('XPATH','//a[text()=" Design Space "]'),
        "simulate_button":('XPATH','//span[text()="Simulate"]'),
        "cell_line":('XPATH','//strong[text()=" CHO "]'),
        "export_text":('XPATH','//strong[text()="Export to PDF"]'),
        "daywise_export_button":('XPATH','(//span[text()="Export"])[1]'),
        "checkbox_export_simulation":('XPATH','(//span[@class="checkbox_label"])[1]'),
        "confirm_export_button":('XPATH','(//span[text()="Export"])[2]'),
        "cancel_btn":('XPATH','(//span[text()="Cancel"])[1]")'),
        "export_name":('ID','nameCalculationFolder'),
        "simulation_header":('XPATH','//strong[text()="Target scale - Simulation 1"]')
    }
    
    def day_wise_page_navigation_verify_values_simulate(self):
        day_tabs=self.driver.find_elements(By.XPATH, "//li[@class='nav-item ng-star-inserted']")
        get_tabs_count_actual=len(day_tabs)-1
        for item in range(get_tabs_count_actual):
            ActionChains(self.driver).move_to_element(day_tabs[item+1]).click(day_tabs[item+1]).perform()
            assert self.results_tab.get_text()=="Results"
            assert self.design_space_tab.get_text()=="Design Space"
            assert self.driver.find_element(By.XPATH, "//div[text()='"+input_values[0]['ref_working_volume']+"']").text==input_values[0]['ref_working_volume']
            assert self.driver.find_element(By.XPATH, "//div[text()='"+input_values[0]['ref_rpm']+"']").text==input_values[0]['ref_rpm']
            assert self.cell_line.get_text()=="CHO"
            self.day_wise_page_verify_values()
            self.driver.execute_script("window.scrollTo(0, 1000)")
            wait_for_clickable_element(self.driver, 100, "//span[text()='Simulate']")
            self.simulate_button.click_button()
            assert self.simulation_header.get_text()==config_variables["simulation_name_text"]
            wait_for_visibility_element(self.driver, 50, "//strong[contains(text(),'Target scale - Simulation')]")            
            item=item+1
        self.driver.execute_script("window.scrollTo(0, -1000)")
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Results']")))
        
    def day_wise_page_verify_values(self):
        wait_for_visibility_element(self.driver, 60, "//strong[text()='Comparison chart']")
        assert self.driver.find_element(By.XPATH, "//strong[text()='Comparison chart']").text=="Comparison chart"
        assert self.driver.find_element(By.XPATH, "//div[text()='"+input_values[0]['ref_bioreactor_name']+"']").text==input_values[0]['ref_bioreactor_name']
        assert self.driver.find_element(By.XPATH, "//div[text()='"+input_values[0]['tar_bioreactor_name']+"']").text==input_values[0]['tar_bioreactor_name']
        assert self.driver.find_element(By.XPATH, "//div[text()='"+input_values[0]['ref_working_volume']+"']").text==input_values[0]['ref_working_volume']
        assert self.driver.find_element(By.XPATH, "//div[text()='"+input_values[0]['ref_rpm']+"']").text==input_values[0]['ref_rpm']
        assert self.driver.find_element(By.XPATH, "//th[@class='TblReferenceColor']").text=="Reference scale"
        assert self.driver.find_element(By.XPATH, "//th[@class='TblTargetColor']").text=="Target scale - Standard"
        assert self.driver.find_element(By.XPATH, "//strong[text()='Model versions']").text=="Model versions"
        assert self.driver.find_element(By.XPATH, "//td[text()='"+" "+input_values[0]['ref_bioreactor_name']+" "+"']").text==input_values[0]['ref_bioreactor_name']
        assert self.driver.find_element(By.XPATH, "//td[text()='"+" "+input_values[0]['tar_bioreactor_name']+" "+"']").text==input_values[0]['tar_bioreactor_name']
        assert self.driver.find_element(By.XPATH, "//div[@class='feedbackHead']").text=="Feedback"
        ref_pri_sparger=input_values[0]['ref_pri_sparger']
        tar_pri_sparger=input_values[0]['tar_pri_sparger']
        if(config_variables["is_docker_headless"]=="True"):
            assert self.driver.find_element(By.XPATH, "//div[text()='"+ref_pri_sparger+"']").text==ref_pri_sparger
        else:    
            decoded_value=ref_pri_sparger.encode('latin1').decode('utf8')
            assert self.driver.find_element(By.XPATH,"//div[text()='"+decoded_value+"']").text==decoded_value
        
        if(config_variables["is_docker_headless"]=="True"):
            assert self.driver.find_element(By.XPATH, "//div[text()='"+tar_pri_sparger+"']").text==tar_pri_sparger
        else:    
            decoded_value=tar_pri_sparger.encode('latin1').decode('utf8')
            assert self.driver.find_element(By.XPATH,"//div[text()='"+decoded_value+"']").text==decoded_value
        assert self.cell_line.get_text()=="CHO"
        
    def perform_daywise_export(self):
        if(config_variables["is_premium"]=="True"):
            self.driver.execute_script("window.scrollTo(0, -1000)")
            wait_for_clickable_element(self.driver, 20, "//span[text()='Results']")
        else:
            self.driver.execute_script("window.scrollTo(0, 800)")           
            wait_for_clickable_element(self.driver, 200, "(//span[text()='Export'])[1]")
            
        wait_for_visibility_element(self.driver, 40, "(//span[text()='Export'])[1]")
        self.daywise_export_button.click_button()
        wait_for_visibility_element(self.driver, 20, "//strong[text()='Export to PDF']")
        assert self.export_text.get_text()=="Export to PDF"
        if(config_variables["is_premium"]=="True"):
            self.checkbox_export_simulation.click_button()
        self.export_name.set_text(config_variables['new_calculation_name'])
        self.confirm_export_button.click_button()
        wait_for_pdf_generation(self.driver)
        verify_pdf_exists(config_variables["new_calculation_name"]+".pdf")

    def verify_daywise_tab_count(self):
        tabs_count=self.driver.find_elements(By.XPATH, "//li[@class='nav-item ng-star-inserted']")
        input_page = InputPage(self.driver)
        if(config_variables["is_premium"]=="True"):
            get_tabs_count_actual=len(tabs_count)-1
        else:
            get_tabs_count_actual=len(tabs_count)
            print(get_tabs_count_actual)
            print(input_page.get_row_count())
        assert get_tabs_count_actual == input_page.get_row_count()