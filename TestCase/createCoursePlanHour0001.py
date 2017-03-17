__author__ = 'xueyan'
# coding:utf-8
import  unittest
import sys,os,logging
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from Page.BaseLoginPage import BaseLogin
from Page.homePage import  HomePage
from Page.BasePage import WebUI
from model import Model
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.logConsole import  LogConsole
import  logging
from Page.singleCoursePlanHourPage import SingleCoursePlanHourPage
# from model.Model import  DataHelper
from ddt import  ddt,data,unpack
from selenium.webdriver.common.by import  By
from selenium.common.exceptions import  NoSuchElementException
from  selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions

class StudentHourCoursePlan60(BaseLogin,SingleCoursePlanHourPage):

    #通过学员管理入口进入排课
    #@unittest.skip('test')
    def testHourCoursePlan60_001(self):
        logging.info("-------通过学员管理入口进入排课------")
        studentName='一对一课时自动01'
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        #学员管理列表
        studentList_loc=(By.XPATH,"//*[@id='CustomerStudentManagement']/li[1]/a")
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(studentList_loc))
        except Exception as e:
            driver.get_screenshot_as_file('../Report/image/testHourCoursePlan60_001_01.png')
            logging.error("找不到【学员管理列表】元素")
        click =self.findElement(*studentList_loc)
        ActionChains(driver).click(click).perform()
        #学生姓名查询
        studenNameSe_loc=(By.XPATH,"//*[@id='noMar']")
        try:
            WebDriverWait(driver, 20, 0.2).until(EC.presence_of_element_located(studenNameSe_loc))
        except Exception as e:
            driver.get_screenshot_as_file('../Report/image/testHourCoursePlan60_001_02.png')
            logging.error("找不到【学员姓名】元素")
        self.findElement(*studenNameSe_loc).send_keys(studentName)
        ##查询按钮
        # buttonSe_loc=(By.XPATH,"//*[@id='keydown-query']")
        # try:
        #     WebDriverWait(driver, 10, 0.2).until(EC.presence_of_element_located(buttonSe_loc))
        # except Exception as e:
        #     driver.get_screenshot_as_file('../Report/image/testHourCoursePlan60_001_03.png')
        #     logging.error("找不到【查询】按钮元素")
        buttonSe_Click =driver.find_element_by_xpath("//*[@id='keydown-query']")
        ActionChains(driver).click(buttonSe_Click).perform()
        #学员列表操作
        oper_loc=(By.XPATH,"//a[@id='nw+0']/span")
        try:
            WebDriverWait(driver, 10, 2).until(EC.presence_of_element_located(oper_loc))
        except Exception as e:
            driver.get_screenshot_as_file('../Report/image/testHourCoursePlan60_001_04.png')
            logging.error("找不到【操作列】元素")
        self.findElement(*oper_loc).click()
        #点击排课操作
        coursePlan_loc=(By.XPATH,"//*[@id='body']/popup/div/div/div/ul/li[6]/a")
        try:
            WebDriverWait(driver, 10, 0.2).until(EC.presence_of_element_located(coursePlan_loc))
        except Exception as e:
            driver.get_screenshot_as_file('../Report/image/testHourCoursePlan60_001_04.png')
            logging.error("找不到【排课】元素")
        self.findElement(*coursePlan_loc).click()
        #调用公共一对一排课界面
        valitext=self.hourCours01()
        context_expxcted="排课成功!共排课1次(1小时)"
        self.assertEqual(context_expxcted, valitext)
    @unittest.skip('test')
    def testHourCoursePlan60_002(self):
        studentName='一对一课时自动01'
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        # 点击学员管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        driver.find_element_by_xpath("//*[@id='noMar']").send_keys(studentName)
        self.wait
        driver.find_element_by_xpath("//*[@id='keydown-query']").click()
        self.wait
        # 点击学员列表操作
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        # 点击排课操作
        driver.find_element_by_xpath("//*[@id='body']/popup/div/div/div/ul/li[6]/a").click()
        # driver.find_element_by_xpath("//a[contains(text(),'排课')]").click()
        self.wait
        #调用公共一对一排课界面
        valitext=self.hourCours02()
        context_expxcted="排课成功!共排课1次(1小时)"
        self.assertEqual(context_expxcted, valitext)
    @unittest.skip('test')
    def testHourCoursePlan60_003(self):
        studentName='一对一课时自动01'
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        self.wait
        # 点击学员管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        self.wait
        driver.find_element_by_xpath("//*[@id='noMar']").send_keys(studentName)
        self.wait
        driver.find_element_by_xpath("//*[@id='keydown-query']").click()
        self.wait
        # 点击学员列表操作
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        self.wait
        # 点击排课操作
        driver.find_element_by_xpath("//*[@id='body']/popup/div/div/div/ul/li[6]/a").click()
        # driver.find_element_by_xpath("//a[contains(text(),'排课')]").click()
        self.wait
        #调用公共一对一排课界面
        valitext=self.hourCours04()
        context_expxcted="排课成功!共排课1次(1小时)"
        self.assertEqual(context_expxcted, valitext)

if __name__=='__main__':
	unittest.main(verbosity=2)
