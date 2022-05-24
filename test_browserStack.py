
import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

## Locators
login_button=(MobileBy.ID,'com.upwork.android.apps.main:id/loginButton')
login_user=(MobileBy.ID,"login_username")
continue_button=(MobileBy.ID,'login_password_continue')
submit_button=(MobileBy.ID,'login_google_submit')
error_message=(MobileBy.ID,'username-message')


class calculator_test(unittest.TestCase):
    driver=None
    
    
    def setUp(self):
        print("setup")
        desired_caps={
        ## enter here your private user and access key 
        "browserstack.user" : "ahmed_inquRI",
        "browserstack.key" : "pr6CCCv1oB7WuHLrqyK3",   
        
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "Xiaomi Redmi Note 9",
        
        # upload your testing application via rest api
        # then get your application url
        "app": "bs://dce50069d6bb251352e6236afa924d3256bedf28"
        }
        self.driver=webdriver.Remote(command_executor="http://hub-cloud.browserstack.com/wd/hub", desired_capabilities=desired_caps)


    def teardown(self):
        print("teardown")
        self.driver.quit()

    def test_login(self):
        print("Login")
        ##wait until the app be clickable
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(*login_button))
        self.driver.find_element(*login_user).send_keys('AhmedMus')
        self.driver.find_element(*continue_button).click()
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(*error_message))
            message=self.driver.find_element(*error_message).text
            print(message)

        except TimeoutException as time_out:
            print('no element is existing , may be a bug here!')    


        

    
       
       