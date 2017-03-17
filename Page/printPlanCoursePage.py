__author__ = 'xueyan'
#coding:utf-8
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from selenium.webdriver.common.by import By
from .homePage import HomePage
from .BasePage import WebUI
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
'''打印页面'''
class PrintCoursePlanPage(WebUI):
    studentName_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[1]/span")#学员姓名
    courseType_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[2]/span")#课程类型
    grage_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[3]/span")#年级
    startTime_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[4]/span")#上课时间
    endTime_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[5]/span")#下课时间
    teachingStyle_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[6]/span")#授课方式
    coefficient_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[7]/span")#折算系数
    startLen_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[8]/span")#上课课时
    dealLen_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[9]/span")#消课课时
    dealAccount_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[10]/span")#消课金额
    subjectName_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[11]/span")#科目
    teacherName_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[12]/span")#授课老师
    adviserName_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[13]/span")#班主任
    printTime_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[14]/span")#打印时间
    balance_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[15]/span")#账户余额
    restCourseNum_loc=(By.XPATH, "//*[@id='mt_print']/div/ul[1]/li[16]/span")#剩余课时
    print_loc=(By.XPATH, "//button[@onclick='preview()']")#打印课票
    cancel_loc=(By.XPATH, "//button[contains(text(),'取消')]")#取消

    def getStudentNameField(self):
        return self.findElement(*self.studentName_loc).text
    def getCourseTypeField(self):
        return self.findElement(*self.courseType_loc).text
    def getGrageField(self):
        return self.findElement(*self.grage_loc).text
    def getStartTimeField(self):
        return self.findElement(*self.startTime_loc).text
    def getEndTimeField(self):
        return self.findElement(*self.endTime_loc).text
    def getTeachingStyleField(self):
        return self.findElement(*self.teachingStyle_loc).text
    def getCoefficientField(self):
        return self.findElement(*self.coefficient_loc).text
    def getStartLenField(self):
        return self.findElement(*self.startLen_loc).text
    def getDealLenField(self):
        return self.findElement(*self.dealLen_loc).text
    def getDealAccountField(self):
        return self.findElement(*self.dealAccount_loc).text
    def getSubjectNameField(self):
        return self.findElement(*self.subjectName_loc).text
    def getTeacherNameField(self):
        return self.findElement(*self.teacherName_loc).text
    def getAdviserNameField(self):
        return self.findElement(*self.adviserName_loc).text
    def getPrintTimeField(self):
        return self.findElement(*self.printTime_loc).text
    def getBalanceField(self):
        return self.findElement(*self.balance_loc).text
    def getRestCourseNumField(self):
        return self.findElement(*self.restCourseNum_loc).text
    def getPrintField(self):
        self.findElement(*self.print_loc).click()
        self.wait
    def getCancelField(self):
        self.findElement(*self.cancel_loc).click()
        self.wait
    ##消课成功不打印客票
    def printCourse01(self):
        valiText=self.getStudentNameField()
        return valiText
    ##消课成功打印客票
    def DealCourse01(self):
        pass
if __name__=='__main__':
    pass

