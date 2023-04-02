from loginpage import Loginpage
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import unittest
#testcase to use unittest func
from homepage import Homepage

#test
class LoginTest(unittest.TestCase):
    #@classmethod is used when your md has "class" in it
    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(service=Service('C://chromedriver.exe'))
        cls.driver.implicitly_wait(5)

    def test_login_valid(self):
        driver = self.driver

        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    #calling class loginpage here
        login = Loginpage(driver)
        login.enter_username("admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = Homepage(driver)
        homepage.classname()
        homepage.logout()


        # self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys('Admin')
        # self.driver.find_element(By.XPATH,"//input[@type='password']").send_keys('admin123')
        # self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        #
        # self.driver.find_element(By.CLASS_NAME,"oxd-userdropdown-img").click()
        # self.driver.find_element(By.LINK_TEXT,"Logout").click()
        time.sleep(2)

        #tearDownClass will run one after once test is completed,

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("test completed")