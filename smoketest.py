from common.common_methods import *
from modules.navigate_admin_page import *
from modules.launch_chrome_and_login_app import *
config_variables = load_config_file()
"""
Functional smoke test 
"""

def chrome_launch_and_hrm_login(driver):
    test_name={'name':'chrome_launch_and_hrm_login'}
    try:
        app_login = LoginPage(driver)
        app_login.login()       
        save_success_status( test_name)
    except Exception as exception:      
        save_failure_status( test_name, exception, driver )

def search_admin(driver):
    test_name={'name':'search_admin'}
    try:
        home_page = HomePage(driver)
        home_page.search_and_choose_admin()       
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
    chrome_launch_and_hrm_login(driver)
    search_admin(driver)
    tear_down(driver)
    
else:
   print("***Unable to invoke test, restart again***")