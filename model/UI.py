#coding:utf-8
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from model import  Model

def main():
	username=input(u'请输入用户名:\n')
	passwd=input(u'请输入地址:\n')
	user=Model.User()
	result=user.checkValidate(username,passwd)
	if not result:
		print (u'用户验证失败')
	else:
		print (u'用户注册成功')

if __name__=='__main__':
	main()