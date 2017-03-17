__author__ = 'xueyan'
# coding:utf-8
import unittest
import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from Page.BaseLoginPage import BaseLogin
from Page.homePage import HomePage
from model import Model
from Page.createGroupPage import CreateGroupPage
# from model.Model import  DataHelper
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from  selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoAlertPresentException
from  selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.logConsole import  LogConsole
import  logging

class GroupDemo(BaseLogin,  HomePage):

    def testcreateGroup_001(self):
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'首页')]")).perform()
        self.wait
        # 点击我的意向客户
        click = driver.find_element_by_xpath("//*[@id='LeadsStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        locator=(By.XPATH,"//a[@ng-click='showImportModal()']")
        try:
            WebDriverWait(driver, 0.02, 0.02).until(EC.presence_of_element_located(locator))
        except Exception as e:
            driver.get_screenshot_as_file('../Report/image/add_001.png')
            logging.error("找不到【新增】按钮元素")
        print("test")

if __name__ == '__main__':
    unittest.main(verbosity=2)
