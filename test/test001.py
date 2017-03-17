#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def getConfig():
    list = {
        'http://192.168.0.161:5555/wd/hub': 'chrome',
        'http://192.168.0.161:5556/wd/hub': 'firefox',
        'http://192.168.0.161:5557/wd/hub': 'chrome',
        'http://192.168.0.161:5558/wd/hub': 'firefox',
    }
    return list

for host,browser in getConfig().items():
    print (u'节点信息:%s'%host)
    print (u'执行的浏览器:%s'%browser)
    driver=webdriver.Remote(
        command_executor=host,
        desired_capabilities={
        'browserName':browser,
        'version':'',
        'javascriptEnabled':True
    }
    )
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('grid2')
driver.close()



