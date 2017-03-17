__author__ = 'xueyan'
#coding:utf-8
import  smtplib
from email.mime.text import  MIMEText
from email.header import Header
from email.mime.multipart import  MIMEMultipart

#发送邮箱服务器
smtpserver='smtp.exmail.qq.com'
#发送邮箱用户/密码
user='xueyan@youwinedu.com'
password=''
#发送邮箱
sender='xueyan@youwinedu.com'
#接收邮箱
receiver='1255676779@qq.com'
#发送邮件主题
subject='Python email test'
#发送的附件
sendfile=open('F:\\web\\webdriverYES\\uplodfile.xls','rb').read()
att=MIMEText(sendfile,'base64','utf-8')
att["Content-Type"]='application/octet-stream'
att["Content-Disposition"]='attachment;filename="uplodfile.xls"'

msgRoot=MIMEMultipart('related')
msgRoot['Subject']=subject
msgRoot.attach(att)
#编写HTML类型的邮件正文
# msg=MIMEText('<html><h1>世界，你好！</h1></html>','html','utf-8')
# msg['Subject']=Header(subject,'utf-8')

#连接发送邮件
smpt=smtplib.SMTP()
smpt.connect(smtpserver)
smpt.login(user,password)
# smpt.sendmail(sender,receiver,msg.as_string())
smpt.sendmail(sender,receiver,msgRoot.as_string())
smpt.quit()