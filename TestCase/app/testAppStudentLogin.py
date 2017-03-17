#coding:utf-8
import  unittest
from appium import  webdriver
from selenium import  webdriver
import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)

from Page.basetestcase  import AppTestCase
from Page.appStudentLoginPage import AppStudentLoginPage
from model import Model
from model.Model import DataHelper


class AppStudentLoginTest(AppTestCase,AppStudentLoginPage):
    #@unittest.skip('test')
    def testLogin(self):
        username='18699123456'
        password='123456'
        self.wait
        my_loc = self.driver.find_element_by_id("com.youwinedu.student:id/r_three")
        my_loc.click()
        self.wait
        # WebDriverWait(self.driver,10000).until(EC.invisibility_of_element_located((By.ID,"com.youwinedu.student:id/rl_login_model")))
        loginLink_loc = self.driver.find_element_by_id("com.youwinedu.student:id/rl_login_model")
        loginLink_loc.click()
        self.wait
        self.login(username,password)
        self.wait
        valit_loc = self.driver.find_element_by_id("com.youwinedu.student:id/tv_use_name").text
        self.assertEqual('大虫自动化', valit_loc)
    @unittest.skip('test')
    def testLogout(self):
        self.wait
        my_loc = self.driver.find_element_by_id("com.youwinedu.student:id/r_three")
        my_loc.click()
        self.wait
        valit_loc = self.driver.find_element_by_id("com.youwinedu.student:id/tv_use_name").text
        self.wait
        sysSet_loc=self.driver.find_element_by_id('com.youwinedu.student:id/ll_sysset')
        sysSet_loc.click()
        self.wait
        logout_loc=self.driver.find_element_by_id('com.youwinedu.student:id/logon')
        logout_loc.click()
        self.wait
        valit_loc = self.driver.find_element_by_id("com.youwinedu.student:id/tv_home_login").text
        self.assertEqual('立即登录', valit_loc)
if __name__ == '__main__':
    unittest.main(verbosity=2)

