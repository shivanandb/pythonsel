from common.common_methods import *
from modules.create_new_calculation import *
from modules.design_space import *
from modules.launch_chrome_and_login_sct import *
from modules.accept_license import *
from modules.my_calculations_actions import *
from modules.home_page import *
from modules.provide_values_input_page import *
from modules.verify_results_summary_page import *
from modules.daywise_page_navigation import *
config_variables = load_config_file()
"""
Prodigy functional smoke test (SCT - Scale Calculation Tool web application) 
To perform a multiday calculation, for given data combination 
(available under src/resources/input_values.json)
"""

def chrome_launch_and_sct_login(driver):
    test_name={'name':'chrome_launch_and_sct_login'}
    try:
        sct_login = LoginPage(driver)
        sct_login.login()       
        save_success_status( test_name)
    except Exception as exception:      
        save_failure_status( test_name, exception, driver )

def accept_license(driver):
    test_name={"name":"accept_license"}
    license_page=License(driver)
    try:
        license_page.click_accept_license()
        save_success_status(test_name)
    except Exception as exception:
        save_failure_status(test_name, exception, driver)
        
def home_page_verify_links(driver):
        test_name={"name":"check_header_menu_elements"}
        home_page=HomePage(driver)
        try:
            home_page.verify_presence_of_header_menu_elements()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)
        
def perform_new_calculation(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"perform_new_calculation"}
        new_calculation_page=NewCalculationPage(driver)
        try:
            new_calculation_page.create_new_calculation()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)
            
def select_cell_line(driver):
    test_name={"name":"select_cell_line"}
    input_page = InputPage(driver)
    try:
        input_page.choose_cell_line()
        save_success_status(test_name)
    except Exception as exception:      
        save_failure_status(test_name, exception, driver)
        
def select_bioreactors_and_spargers(driver):
    test_name={"name":"select_bioreactors_and_spargers"}
    input_page = InputPage(driver)
    try:
        input_page.choose_bioreactor_and_sparger()
        save_success_status(test_name)
    except Exception as exception:      
        save_failure_status(test_name, exception, driver)

def provide_grid_inputs(driver):
    test_name={"name":"provide_grid_inputs"}
    input_page = InputPage(driver)
    try:
        input_page.enter_values_parameter_table()
        save_success_status(test_name)
    except Exception as exception:
        save_failure_status(test_name, exception, driver)
        
def click_calculate(driver):
    test_name={"name":"click_calculate"}
    input_page = InputPage(driver)
    try:
        input_page.click_calculate()
        save_success_status(test_name)
    except Exception as exception:
        save_failure_status(test_name, exception, driver)

def verify_summary_page_bioreactors_spargers(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"verify_summary_page_bioreactors_spargers"}
        summary_page = SummaryPage(driver)
        try:
            summary_page.check_summary_page_bioreactors_spargers()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)
        
def verify_executive_summary_table(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"verify_executive_summary_table"}
        summary_page = SummaryPage(driver)
        try:
            summary_page.verify_executive_summary()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)
            
def click_summary_page_update_verify_values(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"click_summary_page_update_verify_values"}
        summary_page = SummaryPage(driver)
        try:
            summary_page.summary_table_update_and_assert_values()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)
    
def perform_summary_export_pdf(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"perform_summary_export_pdf"}
        summary_page = SummaryPage(driver)
        try:
            summary_page.click_export_button(test_name)
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)

def charts_expand_contract(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"charts_expand_contract"}
        summary_page = SummaryPage(driver)
        try:
            summary_page.chart_expand_and_contract()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)

def change_graph_parameter(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"change_graph_parameter"}
        summary_page = SummaryPage(driver)
        try:
            summary_page.change_graph_dropdown_parameter(test_name)
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)

def slide_R_T_toggle_buttons(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"slide_R_T_toggle_buttons"}
        summary_page = SummaryPage(driver)
        try:
            summary_page.click_toggle_buttons_R_and_T()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)

def verify_summary_page_daywise_tab_count(driver):
    test_name={"name":"verify_summary_page_daywise_tab_count"}
    daywise_page = DaywisePage(driver)
    try:
        daywise_page.verify_daywise_tab_count()
        save_success_status(test_name)
    except Exception as exception:
        save_failure_status(test_name, exception, driver)
    
def daywise_page_navigate_verify_and_simulate(driver):
    if(config_variables["is_premium"]=="True"):
    #Unable to split the below method as 3 activities (navigate, verify values and simulate) depends on a for loop
        test_name={"name":"daywise_page_navigate_verify_and_simulate"}
        day_page = DaywisePage(driver)
        try:
            day_page.day_wise_page_navigation_verify_values_simulate()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)

def daywise_page_navigate_verify_free_user(driver):
    if(config_variables["is_premium"]=="False"):
        test_name={"name":"daywise_page_navigate_verify_free_user"}
        day_page = DaywisePage(driver)
        try:
            day_page.day_wise_page_verify_values()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)

def perform_daywise_export_pdf(driver):
    test_name={"name":"perform_daywise_export_pdf"}
    day_page = DaywisePage(driver)
    try:
        day_page.perform_daywise_export()
        save_success_status(test_name)
    except Exception as exception:
        save_failure_status(test_name, exception, driver)
        
def design_space_navigation(driver):
        test_name={"name":"design_space_navigation"}
        design_page = DesignSpacePage(driver)
        try:
            design_page.navigate_to_design_space_and_edit_constraints()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)

def save_simulation_design_space(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"save_simulation_design_space"}
        design_page = DesignSpacePage(driver)
        try:
            design_page.save_design_space_simulation()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)
            
def verify_simulation_design_space(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"verify_simulation_design_space"}
        design_page = DesignSpacePage(driver)
        try:
            design_page.verify_design_space_simulation()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)

def summary_page_navigation(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"summary_page_navigation"}
        design_page = DesignSpacePage(driver)
        try:
            design_page.navigate_summary_page()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)
            
def executive_summary_choose_simulation_verify(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"executive_summary_choose_simulation_verify"}
        summary_page =SummaryPage(driver)
        try:
            summary_page.click_executive_summary_update()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)
            
def my_calculations_page_navigation(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"home_page_navigation"}
        my_calculations_page = MyCalculationsPage(driver)
        try:
            my_calculations_page.navigate_to_my_calculations()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)
        
def copy_calculation(driver):
    if(config_variables["is_premium"]=="True"):
        test_name={"name":"copy_calculation"}
        my_calculations_page = MyCalculationsPage(driver)
        try:
            my_calculations_page.perform_copy_calculation()
            save_success_status(test_name)
        except Exception as exception:
            save_failure_status(test_name, exception, driver)
            
def tear_down(driver):
    test_name={"name":"tear_down"}
    try:
        driver.close()
        driver.quit()
        save_success_status(test_name)
    except Exception as exception:
        save_failure_status(test_name, exception, driver)


if __name__ == "__main__": 
    driver = initialize_chromedriver()
    if(config_variables["is_docker_headless"]=="True"):
        driver.set_window_size(1024, 768)
    chrome_launch_and_sct_login(driver)
    accept_license(driver)
    home_page_verify_links(driver)
    perform_new_calculation(driver)
    select_cell_line(driver)
    select_bioreactors_and_spargers(driver)
    provide_grid_inputs(driver)
    click_calculate(driver)
    verify_summary_page_bioreactors_spargers(driver)
    verify_executive_summary_table(driver)
    verify_summary_page_daywise_tab_count(driver)
    click_summary_page_update_verify_values(driver)
    perform_summary_export_pdf(driver)
    charts_expand_contract(driver)
    change_graph_parameter(driver)
    slide_R_T_toggle_buttons(driver)
    daywise_page_navigate_verify_and_simulate(driver)
    daywise_page_navigate_verify_free_user(driver)
    perform_daywise_export_pdf(driver)
    design_space_navigation(driver)
    save_simulation_design_space(driver)
    verify_simulation_design_space(driver)
    summary_page_navigation(driver)
    executive_summary_choose_simulation_verify(driver)
    my_calculations_page_navigation(driver)
    copy_calculation(driver)
    tear_down(driver)
    
else:
   print("***Unable to invoke test, restart again***")