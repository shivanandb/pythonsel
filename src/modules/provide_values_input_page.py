from common.common_methods import *
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
config_variables = load_config_file()
"""
Contains logic for filling input page with pre-defined values and calculate
"""
class InputPage(PageFactory):

    def __init__(self,driver):
        self.driver = driver
        
    locators = {
        "choose_ref_bioreactor": ('XPATH', "//select[@id='bioreactornameRefId']"),
        "choose_ref_primary_sparger": ('XPATH', "//select[@id='primarySpargerRefId']"),
        "choose_tar_bioreactor": ('XPATH', '//select[@id="bioreactorTgtId"]'),
        "choose_tar_primary_sparger": ('XPATH', '//select[@id="primarySpargerTgtId"]'),
        "click_scale_strategy":('XPATH','//strong[text()="Scaling strategy"]')
    } 
             
    def choose_bioreactor_and_sparger(self):
        input_values = load_input_values_json_file()
        self.choose_dropdown_value( "//select[@id='bioreactornameRefId']", input_values[0]['ref_bioreactor_name'])
        self.choose_dropdown_value( "//select[@id='primarySpargerRefId']", input_values[0]['ref_pri_sparger'])
        self.choose_dropdown_value( "//select[@id='bioreactorTgtId']", input_values[0]['tar_bioreactor_name'])
        self.choose_dropdown_value("//select[@id='primarySpargerTgtId']", input_values[0]['tar_pri_sparger'])
                    
    def choose_cell_line(self):        
        try:
            el = Select(self.driver.find_element(By.XPATH, "//select[@id='SelectCell']"))
            el.select_by_visible_text("CHO")
        except StaleElementReferenceException as Exception:
            self.choose_ref_bioreactor.click_button()
            el = Select(self.driver.find_element(By.XPATH,"//select[@id='SelectCell']"))
            el.select_by_visible_text("CHO")
         
    def enter_values_parameter_table(self):
        input_values = load_input_values_json_file()
        i=0
        grid_elements = self.driver.find_elements(By.XPATH, "//div[@col-id='dayOfculture'][@role='gridcell']")
        for item in grid_elements:
            self.driver.find_element(By.XPATH,"//div[@row-index='" + str(i) + "']//div[@col-id='dayOfculture']").send_keys(str(i))
            wait_for_clickable_element(self.driver, 60, "//div[@row-index='" + str(i) + "']//div[@col-id='volume']")
            self.driver.find_element(By.XPATH,"//div[@row-index='" + str(i) + "']//div[@col-id='volume']").send_keys(input_values[0]['ref_working_volume'])
            wait_for_clickable_element(self.driver, 30, "//div[@row-index='" + str(i) + "']//div[@col-id='rpm']")
            self.driver.find_element(By.XPATH,"//div[@row-index='" + str(i) + "']//div[@col-id='rpm']").send_keys(input_values[0]['ref_rpm'])
            wait_for_clickable_element(self.driver, 30, "//div[@row-index='" + str(i) + "']//div[@col-id='airPrimary']")
            self.driver.find_element(By.XPATH,"//div[@row-index='" + str(i) + "']//div[@col-id='airPrimary']").send_keys(input_values[0]['ref_air_primary'])
            self.driver.find_element(By.XPATH,"//div[@row-index='" + str(i) + "']//div[@col-id='o2Primary']").send_keys(input_values[0]['ref_o2_primary'])
            self.driver.find_element(By.XPATH,"//div[@row-index='" + str(i) + "']//div[@col-id='targetParametersVolume']").send_keys(input_values[0]['tar_working_volume'])
            i=i+1
        
    def get_row_count(self):
        grid_elements = self.driver.find_elements(By.XPATH,"//div[@col-id='dayOfculture'][@role='gridcell']")
        return len(grid_elements)
            
    def click_calculate(self):
        self.click_scale_strategy.click_button()
        self.driver.execute_script("window.scrollTo(0, 1000)")
        #above 2 lines are required, as by default it scrolls to the top one finish entering grid table values
        wait_for_clickable_element(self.driver, 30, "//span[@class='icon_calculate']")
        calculate_button=self.driver.find_element(By.XPATH, "//span[text()='Calculate']")        
        ActionChains(self.driver).click(calculate_button).perform()
       
    def choose_dropdown_value(self, path, dvalue):
            wait_for_clickable_element(self.driver, 30, "//select[@id='bioreactornameRefId']")
            dropdown_values = Select(self.driver.find_element(By.XPATH, path))
            if(config_variables["is_docker_headless"]=="False"):
                dropdown_values = Select(self.driver.find_element(By.XPATH, path))
                dvalue=dvalue.encode('latin1').decode('utf8') 
            #Note: If you are executing locally then follow this instruction
            # value has an extra character '2 Âµm' instead of '2 µm' hence using utf-8 (latin-1) encoding and decoding below
            # latin-1 encoding in Python implements ISO_8859-1:1987 which maps all possible byte values to the first 256 Unicode code points
            for dropdown_value in dropdown_values.options:
                dropdown_values.select_by_visible_text(dvalue)  
 
            
           