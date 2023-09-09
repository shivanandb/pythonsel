import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from Screenshot import Screenshot_Clipping
import datetime
import os
from os import path
import json
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

"""
This class contains common reusable methods for basic operations
"""
current_directory = os.getcwd()
screenshot_folder_path=current_directory+"/output_screenshots"
logs_folder_path=current_directory+"/run_logs"
#normal_pdf_folder_path=current_directory+"\\PDF_files"
#docker_pdf_folder_path=current_directory+"/PDF_files"

ss = Screenshot_Clipping.Screenshot()

with open('resources/config_variables.json') as file:
        data = json.load(file)
        log_file_name=data["log_file_name"]
        a=str(datetime.datetime.now())
        a=a.replace(':','-')
        a=a.replace('.','-')
        log_file_name=log_file_name+'_'+a+".log"
        while not os.path.exists(logs_folder_path):
                os.makedirs(logs_folder_path)
        log_file_path=os.path.join(logs_folder_path, log_file_name)

def initialize_chromedriver():
        config_variables = load_config_file()
        empty_folder_contents(screenshot_folder_path)
        empty_folder_contents(logs_folder_path)
        op = webdriver.ChromeOptions()
        #pdf_folder_path=set_pdf_folder_path()
        #op.add_experimental_option('prefs', {"download.default_directory": pdf_folder_path})
        if(config_variables["is_docker_headless"]=="True"):
                #empty_pdf_folder_contents(pdf_folder_path)
                #op.add_experimental_option('prefs', {"download.default_directory": "/tmp"})
                op.add_argument("--headless=new")
                op.add_argument("--no-sandbox")
                op.add_argument('--disable-dev-shm-usage')
                op.add_argument("--disable-gpu")
                op.add_argument('--ignore-ssl-errors=yes')
                op.add_argument('--ignore-certificate-errors')
                driver = webdriver.Remote(command_executor='http://'+config_variables['docker_ip']+':4444/wd/hub', options=op )

        elif(config_variables["is_normal_headless"]=="True"):
                #empty_folder_contents(pdf_folder_path)
                op.add_argument("--no-sandbox")
                op.add_argument("--headless=new")
                op.add_argument("--start-maximized")
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=op)
        else:
                #empty_folder_contents(normal_pdf_folder_path)
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=op)
                
        Url = data["url"]
        driver.maximize_window()
        driver.get(Url)
        driver.implicitly_wait(10)
        return driver

def update_status( test_name, key_name, state):
        test_name[key_name]=state

def append_test_status_file(test_name):
        answ=os.path.exists(log_file_path)
        with open(log_file_path, "a+" if answ else "w") as f:
                f.write(str(test_name))
                f.write('\n')
                f.close
            
def save_failure_status(test_name, E, driver): 
        print(str(E))
        print("Fail : ", test_name)
        update_status(test_name, 'status', 'Fail')
        update_status(test_name, 'exception', str(E))
        append_test_status_file(test_name)
        take_screenshot(test_name['name'], driver)            
            
def save_success_status(test_name):  
        print("Pass : ", test_name)
        update_status(test_name, 'status', 'Pass')
        append_test_status_file(test_name)
        
def empty_folder_contents(mydir):
        try:
            for f in os.listdir(mydir):
                os.remove(os.path.join(mydir, f))
            print ('\n Deletion completed for folder : ')
            print(mydir)
        except:
            print ('\n Unable to delete folder contents : ')
            print(mydir)
            pass

def calculate_test_time():
    named_tuple = time.localtime() # get struct_time
    test_run_time = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    print(test_run_time)

def take_screenshot(screen_name, driver):
        while not os.path.exists(screenshot_folder_path):
                os.makedirs(screenshot_folder_path)
        driver.save_screenshot(screenshot_folder_path+"/"+screen_name+'.png')

def take_screenshot_full_screen(ss, screen_name, driver):#this feature creates screenshot in blurr manner, keeping for investigation
        ss.full_Screenshot(driver, save_path=r'.\output_screenshots\\' , image_name=screen_name+'.png')

def load_input_values_json_file():
        with open('resources/input_values.json') as file:
            input_values = json.load(file)
        return input_values

def load_config_file():
        with open('resources/config_variables.json') as file:
            config_variables = json.load(file)
        return config_variables

def verify_pdf_exists(file_pdf):
        pdf_folder_path=set_pdf_folder_path()
        pdf_file_path=os.path.join(pdf_folder_path, file_pdf)
        while not os.path.exists(pdf_file_path):        
                time.sleep(1)
        assert path.exists(pdf_file_path)==True

def wait_for_pdf_generation(driver):
        report_generating_status=driver.find_element(By.XPATH, "//div[text()='Generating report....']")
        while report_generating_status.is_displayed()==True:
            WebDriverWait(driver, 1000).until(EC.invisibility_of_element_located((By.XPATH, "//div[text()='Generating report....']")))
            break

def wait_until_condition_met(driver, xpath):
        save_button_enable_status=driver.find_element(By.XPATH, xpath)
        while save_button_enable_status.is_displayed()==True:
                wait_for_clickable_element(driver, 1000, xpath)
                break

def wait_for_visibility_element(driver, duration, path_element):
        WebDriverWait(driver, duration).until(EC.visibility_of_element_located((By.XPATH, path_element)))
        
def wait_for_clickable_element(driver, duration, path_element):
        WebDriverWait(driver, duration).until(EC.element_to_be_clickable((By.XPATH, path_element)))