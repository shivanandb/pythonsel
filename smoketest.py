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
    tear_down(driver)
    
else:
   print("***Unable to invoke test, restart again***")