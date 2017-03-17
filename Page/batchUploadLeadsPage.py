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

'''意向客户上传页面'''
class BatchUploadLeadsPage(WebUI):
    batchRadio_loc=(By.XPATH, "//*[@ng-click='checkedAddType(1)']/input")#批量导入radio
    selectFile_loc=(By.XPATH, "//input[@type='file' and @ng-if='!isOneChecked']")#批量导入radio
    uploadFile_loc=(By.XPATH, "//button[@type='button' and @ng-click='item.upload()']")#文件上传按钮
    cancelFile_loc=(By.XPATH, "//button[@type='button' and @ng-click='item.cancel()']")#取消上传
    removeFile_loc=(By.XPATH, "//button[@type='button' and @ng-click='item.remove()']")#删除文件
    submitButton_loc=(By.XPATH, "//button[@class='confirm']")#确认
    valiText_loc=(By.XPATH,"//div[@class='sweet-alert showSweetAlert visible']/h2") #检查点
    okButton_loc=(By.XPATH, "//button[@class='confirm']")#ok

    def getBatchRadioField(self):
        self.findElement(*self.batchRadio_loc).click()
        self.wait
    def getSelectFileField(self,filePath):
        self.findElement(*self.selectFile_loc).send_keys(filePath)
        self.wait
    def getCancelFileField(self):
        self.findElement(*self.cancelFile_loc).click()
        self.wait
    def getUploadFileField(self):
        self.findElement(*self.uploadFile_loc).click()
        self.wait
    def getRemoveFileField(self):
        self.findElement(*self.removeFile_loc).click()
        self.wait
    def getSubmitButtonField(self):
        self.findElement(*self.submitButton_loc).click()
        self.wait
    def getOkButtonField(self):
        self.findElement(*self.okButton_loc).click()
        self.wait
    def getValitextField(self):
        self.findElement(*self.valitext_loc).text
        self.wait
    ##上传文件
    def dealCourse01(self,filePath):
        self.getBatchRadioField()
        self.getSelectFileField(filePath)
        self.getUploadFileField()
        self.getSubmitButtonField()
        valitext=self.getValitextField()
        self.getOkButtonField()
        return valitext
    ##删除
    def dealCourse02(self):
        pass
if __name__=='__main__':
    pass


