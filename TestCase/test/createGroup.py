__author__ = 'xueyan'
# coding:utf-8
import unittest
import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from Page.BaseLoginPage import BaseLogin
from Page.homePage import HomePage
from model import Model
from Page.createGroupPage import createGroupPage
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


class GroupDemo(BaseLogin, createGroupPage, HomePage):

    def testcreateGroup_001(self):
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        # 点击一对多管理
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[3]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        self.wait
        driver.find_element_by_xpath("//a[contains(text(),'添加一对多')]").click()
        self.wait
        self.createGroup("班组新增",1,2)
        self.assertEqual("创建学生班组成功", self.getLoginErrorDiv())
    def testcreateGroup_002(self):
        driver = self.driver
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        # 点击一对多管理
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[3]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        self.wait
        driver.find_element_by_xpath("//a[contains(text(),'添加一对多')]").click()
        self.wait
        self.createSelectGroup("班组查询新增",2,1,"班组01","21321221",3)
        # self.assertEqual("创建学生班组成功", self.getLoginErrorDiv())
    def testcreateGroup_003(self):
        driver = self.driver
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[3]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        driver.find_element_by_xpath("//input[@placeholder='班组名称查询']").send_keys("班组新增")
        self.wait
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        driver.find_element_by_xpath("//a[@ng-click='addCoursePlanInfo(row,2)']").click()
        self.wait

if __name__ == '__main__':
    unittest.main(verbosity=2)
