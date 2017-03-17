#coding:utf-8
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
import  unittest,os,sys,HTMLTestRunner,time
from email.mime.text import MIMEText
from email.header import Header
import  smtplib
import  unittest
import configparser,logging
import importlib
importlib.reload(sys)

#=======================定义发送邮件===================================
def send_mail(file_new):
    #获取最新测试报告
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()
    # 编写HTML类型的邮件正文
    subject='YES后台管理自动化测试报告'
    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header(subject,'utf-8')
    # 发送邮箱服务器
    smtpserver = 'smtp.exmail.qq.com'
    # 发送邮箱用户/密码
    user = 'xueyan@youwinedu.com'
    password = ''
    # 发送邮箱
    sender = 'xueyan@youwinedu.com'
    # 接收邮箱
    receiver = '1255676779@qq.com'
    # 连接发送邮件
    smpt = smtplib.SMTP()
    smpt.connect(smtpserver)
    smpt.login(user, password)
    # smpt.sendmail(sender,receiver,msg.as_string())
    smpt.sendmail(sender, receiver, msg.as_string())
    smpt.quit()
#==================查找测试报告目录，找到最新生成的测试报告文件 ============
def new_report(resuleDir):
    lists = os.listdir(resuleDir)
    lists.sort(key=lambda fn: os.path.getmtime(resuleDir + "\\" + fn))
    file_new = os.path.join(resuleDir, lists[-1])
    return file_new
#==================生成测试报告 ======================================
def suite1(testCaseDir):
	dir_case=unittest.defaultTestLoader.discover(testCaseDir,
		pattern='createGroup.py',
		top_level_dir=None
	)
	return dir_case

#获取当前时间另外一种方式是:
nowTime=time.strftime('%Y-%m-%d %X',time.localtime())
def getNowTime():
	return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
def runAutomation1(testCaseDir,testReportDir):
    filename = testReportDir+getNowTime()+'TestReport.html'
    fp = open(filename,mode='wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='一对一排课自动化测试报告',
        description='自动化测试报告详细的信息'
    )
    runner.run(suite1(testCaseDir))
    fp.close()

if __name__=='__main__':
    testCaseDir='./TestCase/test/'
    testReportDir='./Report/'
    runAutomation1(testCaseDir,testReportDir)
    #send_mail(new_report(testReportDir))