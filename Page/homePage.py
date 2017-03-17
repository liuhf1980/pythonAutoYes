__author__ = 'xueyan'
#coding:utf-8
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from selenium import webdriver
from selenium.webdriver.common.by import  By
from .BasePage import  WebUI

class HomePage(WebUI):
	valix_name_loc=(By.XPATH,"//span[@class='header-user-welcome ng-binding']")

	def getNameLoation(self):
		self.wait
		return self.find_element(*self.valix_name_loc).text