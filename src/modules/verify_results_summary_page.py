import time
from selenium.webdriver.support.ui import Select
from modules.provide_values_input_page import *
from selenium.webdriver.support.ui import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.action_chains import ActionChains
from common.common_methods import *
config_variables = load_config_file()
"""
This code verifies the below points :
a. After successful calculation, Summary page for  bioreactors and spargers values
b. Verifying match for number of daywise tabs versus number of row input count 
c. Verifies executive summary table present or not with few table values
d. Clicks Summary export 
e. Expands and contracts all 3 graphs with calculation name validation 
f. Changes R & T toggles for every graph

"""
no_exception="False"

class SummaryPage(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        "verify_summary_tab": ('XPATH', '//a[text()=" Summary "]'),
        "update_button":('XPATH', '(//button[@class="btn primary_btn_icon"])[2]'),
        "export_btn":('XPATH','//span[text()="Export"]'),
        "update_button_cancel":('XPATH','(//button[text()=" Cancel "])[1]'),
        "executive_summary_working_volume":('XPATH','(//span[text()="Working volume (L)"])[3]'),
        "executive_summary_agitation":('XPATH','(//span[text()="Agitation (rpm)"])[2]'),
        "executive_simulation":('XPATH','(//div[@col-id="Name"][@role="gridcell"][@aria-colindex="2" and contains(text(),"Simulation")])[1]')
    }
    
    def check_summary_page_bioreactors_spargers(self):
            #Below code verifies bioreactor, sparger values expected (from input json file) vs actucal (get text from UI)
            self.driver.execute_script("window.scrollTo(0, -1000)")
            input_values = load_input_values_json_file()
            assert self.verify_summary_tab.get_text()=="Summary"
            assert self.driver.find_element(By.XPATH, "//strong[text()='"+input_values[0]['ref_bioreactor_name']+"']").text==input_values[0]['ref_bioreactor_name']
            assert self.driver.find_element(By.XPATH,"//strong[text()='"+input_values[0]['tar_bioreactor_name']+"']").text==input_values[0]['tar_bioreactor_name']
            assert self.driver.find_element(By.XPATH,"//li[text()=' "+config_variables['new_calculation_name']+"']").text==" "+config_variables['new_calculation_name']
            if(config_variables["is_docker_headless"]=="True"):
                assert self.driver.find_element(By.XPATH,"//div[text()='Primary sparger: "+input_values[0]['ref_pri_sparger']+"']").text=='Primary sparger: '+input_values[0]['ref_pri_sparger']
                assert self.driver.find_element(By.XPATH,"//div[text()='Primary sparger: "+input_values[0]['tar_pri_sparger']+"']").text=='Primary sparger: '+input_values[0]['tar_pri_sparger']
            else:
                assert self.driver.find_element(By.XPATH,"//div[text()='Primary sparger: "+input_values[0]['ref_pri_sparger'].encode('latin1').decode('utf8')+"']").text=='Primary sparger: '+input_values[0]['ref_pri_sparger'].encode('latin1').decode('utf8')
                assert self.driver.find_element(By.XPATH,"//div[text()='Primary sparger: "+input_values[0]['tar_pri_sparger'].encode('latin1').decode('utf8')+"']").text=='Primary sparger: '+input_values[0]['tar_pri_sparger'].encode('latin1').decode('utf8')
    def verify_executive_summary(self):
            #Below code verifies summary table values expected vs actual (get text from UI)
            assert self.executive_summary_working_volume.get_text()=="Working volume (L)"
            assert self.executive_summary_agitation.get_text()=="Agitation (rpm)"
            executive_summary_table_elements = self.driver.find_elements(By.XPATH,"//div[@col-id='volume'][@role='gridcell'][@aria-colindex='3']")
            input_values = load_input_values_json_file()
            grid_working_volume=[]
            for item in executive_summary_table_elements:
                grid_working_volume.append(item.text)  
            assert input_values[0]['tar_working_volume'] in grid_working_volume
        
    def click_executive_summary_update(self):
            wait_for_clickable_element(self.driver, 30, "(//button[@class='btn primary_btn_icon'])[2]")
            self.update_button.click_button()
            select_simulation=self.driver.find_elements(By.XPATH,"//div[@col-id='select'][@role='gridcell'][@aria-colindex='3']")
            select_simulation[3].click()
            self.driver.find_element(By.XPATH,"(//button[@type='submit'])[1]").click()
            assert self.executive_simulation.get_text() == "Target - Simulation 1"
    
    def summary_table_update_and_assert_values(self):
            time.sleep(3)#UI becomes ready even before undetermined time the backend gets available, hence sleep statement mandatorily required
            wait_for_clickable_element(self.driver, 30, "(//button[@class='btn primary_btn_icon'])[2]")
            self.update_button.click_button()
            executive_summary_table_elements = self.driver.find_elements(By.XPATH,"//div[@col-id='volume'][@role='gridcell'][@aria-colindex='5']")
            input_values = load_input_values_json_file()
            grid_working_volume=[]
            for executive_summary_table_element in executive_summary_table_elements:
                grid_working_volume.append(executive_summary_table_element.text)  
            assert input_values[0]['ref_working_volume'] in grid_working_volume
            assert input_values[0]['tar_working_volume'] in grid_working_volume
            grid_working_volume.clear()
            self.update_button_cancel.click_button()
        
    def click_export_button(self, test_name):
            try:
                self.driver.execute_script("window.scrollTo(0, 1000)")
                wait_for_clickable_element(self.driver, 100, "//span[text()='Export']")
                summary_export_button=self.driver.find_element(By.XPATH,"//span[text()='Export']")
                ActionChains(self.driver).click(summary_export_button).perform()
                wait_for_pdf_generation(self.driver)
                verify_pdf_exists("CytivaBioreactorScalerResult_"+config_variables['new_calculation_name']+".pdf")
                self.driver.execute_script("window.scrollTo(0, -1000)")

            except Exception as exception:
                assert no_exception == "True"
                save_failure_status( test_name, exception, self.driver)   
            
    def change_graph_dropdown_parameter(self, test_name):
            try:         
                graph_axes=self.driver.find_elements(By.XPATH,"//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @class='highcharts-axis-title']")
                assert graph_axes[0].text=="VVM total (1/min)"
                
                assert graph_axes[1].text=="P/V (W/m³)"
                self.driver.execute_script("window.scrollTo(0, -1000)")
                
                WebDriverWait(self.driver, 200).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='P/V']"))).click()
                WebDriverWait(self.driver, 200).until(EC.element_to_be_clickable((By.XPATH, "//span[text()=' Tip speed ']"))).click()
                WebDriverWait(self.driver, 200).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='VVM total']"))).click()
                time.sleep(1)
                WebDriverWait(self.driver, 200).until(EC.element_to_be_clickable((By.XPATH, "//span[text()=' kLa total ']"))).click()
                WebDriverWait(self.driver, 160).until(EC.visibility_of_element_located((By.XPATH, "//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and text()='kLa total (1/hour)']")))
                graph_axes=self.driver.find_elements(By.XPATH,"//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @class='highcharts-axis-title']")
                assert graph_axes[0].text=="kLa total (1/hour)"
                assert graph_axes[1].text=="Tip speed (m/sec)"

            except Exception as exception:
                assert no_exception == "True"
                save_failure_status( test_name, exception, self.driver )   
                
    def chart_expand_and_contract(self):
            #high-charts validation included using svg xpath method 
            chart_expand_buttons=self.driver.find_elements(By.XPATH,"//img[@id='chartExpansionIcon']")
            assert len(chart_expand_buttons) == 3
            count=0
            for chart_expand_button in chart_expand_buttons:
                chart_expand_button.click()
                element_graph= self.driver.find_element(By.XPATH,"//span[@class='bg-white p-3 pr-5 m-0']")
                assert element_graph.is_displayed()==True
                assert self.driver.find_element(By.XPATH,"//span[text()='"+config_variables['new_calculation_name']+"']").text==config_variables['new_calculation_name']
                wait_for_clickable_element(self.driver, 30, "//img[@alt='Exit fullscreen chart']")
                exit_full_screen=self.driver.find_element(By.XPATH,"//img[@alt='Exit fullscreen chart']")
                assert exit_full_screen.is_displayed()==True
                if (count==0):
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @text-anchor='start'])[3]").text=="Reference"
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @text-anchor='start'])[4]").text=="Target"
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @class='highcharts-axis-title'])[4]").text == "P/V (W/m³)"
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @class='highcharts-axis-title'])[3]").text == "VVM total (1/min)"
                    take_screenshot('single_paramenter', self.driver)
                elif(count==1):
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @text-anchor='start'])[11]").text=="Reference-Agitation"
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @text-anchor='start'])[12]").text=="Target-Agitation"
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @text-anchor='start'])[13]").text=="Reference-P/V"
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @text-anchor='start'])[14]").text=="Target-P/V"
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @class='highcharts-axis-title'])[7]").text == "Agitation (rpm)"
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @class='highcharts-axis-title'])[6]").text == "Day of culture"
                    take_screenshot('2_parameter_graph'+'_'+str(count), self.driver)
                elif(count==2):
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @text-anchor='start'])[19]").text=="Reference-VVM total"
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @text-anchor='start'])[20]").text=="Target-VVM total"
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @text-anchor='start'])[21]").text=="Reference-OTR total"
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @text-anchor='start'])[22]").text=="Target-OTR total"
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @class='highcharts-axis-title'])[10]").text == "VVM total (1/min)"
                    assert self.driver.find_element(By.XPATH,"(//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @class='highcharts-axis-title'])[9]").text == "Day of culture"
                    take_screenshot('2_parameter_graph'+'_'+str(count), self.driver)
                    
                self.driver.find_element(By.XPATH,"//img[@alt='Exit fullscreen chart']").click()  
                count=count+1 
         
    def click_toggle_buttons_R_and_T(self):
            #high-charts validation included using svg xpath method 
            self.driver.execute_script("window.scrollTo(0, -1000)")
            wait_for_clickable_element(self.driver, 50, "//span[@class='mat-slide-toggle-bar']")
            graph_legends_before=self.driver.find_elements(By.XPATH,"//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @y='15']")
            assert graph_legends_before[0].text == "Reference"
            assert graph_legends_before[1].text == "Target"
            wait_for_clickable_element(self.driver, 50, "//span[@class='mat-slide-toggle-bar']")
            toggle_elements=self.driver.find_elements(By.XPATH,"//span[@class='mat-slide-toggle-bar']")
            toggle_elements[0].click()
            graph_legends_after=self.driver.find_elements(By.XPATH,"//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @y='15']")
            assert graph_legends_after[0].text == "Target"
            if(toggle_elements[1].is_enabled()):
                toggle_elements[0].click()
            toggle_elements[1].click()
            if(toggle_elements[0].is_enabled()):
                graph_legends_after=self.driver.find_elements(By.XPATH,"//*[name()='svg']//*[local-name()='g']//*[local-name()='text' and @y='15']")
                assert graph_legends_after[0].text == "Reference"
            self.driver.execute_script("window.scrollTo(0, -1000)")
            wait_for_clickable_element(self.driver, 30, "//a[text()=' Summary ']")