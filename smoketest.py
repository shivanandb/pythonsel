import time
from common.common_methods import *
from modules.navigate_admin_page import *
from modules.launch_chrome_and_login_app import *
from modules.dashboard_page import *
config_variables = load_config_file()

"""
Functional smoke test 
"""

def chrome_launch_and_hrm_login(driver):
    calculate_test_time()
    test_name={'name':'chrome_launch_and_hrm_login'}
    try:
        app_login = LoginPage(driver)
        app_login.login()       
        save_success_status( test_name)
        #print(test_name)
    except Exception as exception:      
        save_failure_status( test_name, exception, driver )
        #print(test_name)

def dashboard_test(driver):
    test_name={'name':'dashboard_test'}
    try:
        dashboard_page = DashboardPage(driver)
        dashboard_page.dashboard_verify()
        save_success_status( test_name)
    except Exception as exception:      
        save_failure_status( test_name, exception, driver )

def dashboard_click_link(driver):
    test_name={'name':'dashboard_click_link'}
    try:
        dashboard_page = DashboardPage(driver)
        dashboard_page.dashboard_click_links()
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

def admin_header_verification(driver):
    test_name={'name':'admin_header_verification'}
    try:
        home_page = HomePage(driver)
        home_page.verify_admin_header()      
        save_success_status( test_name)
    except Exception as exception:      
        save_failure_status( test_name, exception, driver )

def admin_add(driver):
    test_name={'name':'admin_add'}
    try:
        home_page = HomePage(driver)
        home_page.add()
        save_success_status( test_name)
    except Exception as exception:      
        save_failure_status( test_name, exception, driver )

def verify_about_dropdown(driver):
    test_name={'name':'verify_about_dropdown'}
    try:
        home_page = HomePage(driver)
        home_page.verify_about()
    
        save_success_status( test_name)
    except Exception as exception:      
        save_failure_status( test_name, exception, driver )

def verify_user_management(driver):
    test_name={'name':'verify_user_management'}
    try:
        home_page = HomePage(driver)
        home_page.click_and_verify_user_management()
        save_success_status( test_name)
    except Exception as exception:      
        save_failure_status( test_name, exception, driver )

def verify_job(driver):
    test_name={'name':'verify_job'}
    try:
        home_page = HomePage(driver)
        home_page.click_and_verify_job()
        home_page.check_collapse()
        save_success_status( test_name)
    except Exception as exception:      
        save_failure_status( test_name, exception, driver )

def tear_down(driver):
    test_name={"name":"tear_down"}
    try:
        driver.close()
        driver.quit()
        save_success_status(test_name)
        calculate_test_time()
    except Exception as exception:
        save_failure_status(test_name, exception, driver)


if __name__ == "__main__": 
    driver = initialize_chromedriver()
    if(config_variables["is_docker_headless"]=="True"):
        driver.set_window_size(1024, 768)
    chrome_launch_and_hrm_login(driver)
    dashboard_test(driver)
    dashboard_click_link(driver)
    search_admin(driver)
    admin_header_verification(driver)
    admin_add(driver)
    verify_about_dropdown(driver)
    verify_user_management(driver)
    verify_job(driver)
    tear_down(driver)
    
else:
   print("***Unable to invoke test, restart again***")