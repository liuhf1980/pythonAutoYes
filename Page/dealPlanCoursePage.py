__author__ = 'xueyan'
#coding:utf-8
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
# from selenium import webdriver
from selenium.webdriver.common.by import By
from .homePage import HomePage
from .BasePage import WebUI
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
'''消课页面'''
class DealCoursePlanPage(WebUI):
    SubmitButton_loc=(By.XPATH, "//button[@class='confirm']")#消课确认
    CancelButton_loc=(By.XPATH, "//button[@class='cancel']")#消课取消
    valitext_loc=(By.XPATH,"//div[@class='modal-body text-center']/h1")
    SubmitButton02_loc=(By.XPATH, "//button[@ng-click='hasNext()']")
    CancelButton2_loc=(By.XPATH, "//button[@ng-click='cancelModal']")
    def getSubmitButtonField(self):
        self.findElement(*self.SubmitButton_loc).click()
        self.wait
    def getCancelButtonField(self):
        self.findElement(*self.CancelButton_loc).click()
        self.wait
    def getSubmitButton02Field(self):
        self.findElement(*self.SubmitButton02_loc).click()
        self.wait
    def getCancelButton2Field(self):
        self.findElement(*self.CancelButton2_loc).click()
        self.wait
    def getValitextField(self):
        self.findElement(*self.valitext_loc).text
        self.wait
    ##消课成功不打印客票
    def DealCourse01(self):
        self.getSubmitButtonField
        Valitext=self.getValitextField()
        valiText=self.getConfirmValiTextField()
        self.getCancelButton2Field()
        return valiText
    ##消课成功打印客票
    def DealCourse01(self):
        pass
if __name__=='__main__':
    pass

