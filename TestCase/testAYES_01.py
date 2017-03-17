__author__ = 'xueyan'
#coding:utf-8
import  unittest
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from Page.basetestcase import BaseTestCase
from Page.loginYesPage import  LoginYesPage
from Page.homePage import  HomePage
from model import Model
# from model.Model import  DataHelper
from ddt import  ddt,data,unpack

@ddt
class loginPage(BaseTestCase,LoginYesPage,HomePage):

	@data(*Model.DataHelper().readExcels())
	@unpack
	def testLoginError_001(self,username,password,verifyCode,context_expxcted):
		'''测试：YES登录失败的N种情况'''
		self.doLogin(username, password,verifyCode)
		# self.assertEqual(context_expxcted,self.getLoginErrorDiv())
if __name__=='__main__':
	unittest.main(verbosity=2)
