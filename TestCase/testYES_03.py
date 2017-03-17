__author__ = 'xueyan'
from selenium import webdriver
import HTMLTestRunner
import unittest,time,re
from selenium.webdriver.common.by import  By
from selenium.common.exceptions import  NoSuchElementException
from  selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import  NoAlertPresentException
from  selenium.common.exceptions import NoAlertPresentException
def wait():
    time.sleep(3)
class rechargeSingleCoursePlanPage(unittest.TestCase):
    def setUp(self):
        #启动浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('http://172.168.101.83/')
        #登录
        self.driver.find_element_by_id('login-name').send_keys('qiqi1')
        self.driver.find_element_by_id('login-pass').send_keys('password')
        self.driver.find_element_by_name('user.verifyCode').send_keys('1234')
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        wait()
    '''创建排课'''
    def test_Charge01(self):
        driver=self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        wait()
        # 点击学员管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        driver.find_element_by_xpath("//*[@id='noMar']").clear()
        driver.find_element_by_xpath("//*[@id='noMar']").send_keys("自动化一对一储值")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='keydown-query']").click()
        wait()
        # 点击学员列表操作
        driver.find_element_by_xpath("//*[@id='nw+0']/span").click()
        wait()
        # 点击排课操作
        driver.find_element_by_xpath("//*[@id='body']/popup/div/div/div/ul/li[6]/a").click()
        wait()
        # 点击切换储值排课操作
        driver.find_element_by_xpath("//span[@ng-click='showPaikeView(1)']").click()
        wait()
        # 点击查看订单
        driver.find_element_by_xpath("//button[@ng-click='showStoredOrderList(detail)']").click()
        wait()
        driver.find_element_by_xpath("//button[@ng-click='cancle()']").click()
        wait()
        #选择排课科目
        selectLen = Select(driver.find_element_by_xpath("//*[@id='subjectId']"))
        selectLen.select_by_index(2)
        wait()
        #选择教师
        driver.find_element_by_xpath("//a[text()='王建婷']").click()
        wait()
        # 点击添加日期
        driver.find_element_by_xpath("//a[text()='添加']").click()
        wait()
        # 选择星期日
        driver.find_element_by_xpath("//input[@value='7']").click()
        driver.find_element_by_xpath("//*[@id='time1']").send_keys('8')
        driver.find_element_by_xpath("//*[@id='time2']").send_keys('00')
        # 选择上课时长
        selectLen = Select(driver.find_element_by_name("timeSize"))
        selectLen.select_by_index(2)
        # 点击确定
        driver.find_element_by_xpath("//button[text()='确定']").click()
        wait()
        driver.find_element_by_xpath("//span[text()='只排下周']").click()
        wait()
        # 选择开始结束时间段
        # startTime = "$(\"input[placeholder='开始时间≥当前时间']\").removeAttr('readonly');$(\"input[placeholder='开始时间≥当前时间']\").attr('value','2017-01-10 12:00:00')"
        # stopTime = "$(\"input[placeholder='结束时间>开始时间']\").removeAttr('readonly');$(\"input[placeholder='结束时间>开始时间']\").attr('value','2017-08-10 12:00:00')"
        # driver.execute_script(startTime)
        # driver.execute_script(stopTime)
        #键入排课次数
        #driver.find_element_by_xpath("//*[@id='body']/div[4]/form/div/div[2]/div[8]/div[2]/div/div/h3/p/span[2]").click()
        # 点击提交排课
        driver.find_element_by_xpath("//button[@ng-click='show.submitPlan()']").click()
        wait()
        valiText=driver.find_element_by_xpath("//*[@id='body']/div[6]/h2").text
        self.assertEqual(valiText,'即将排课1次(1小时),是否确定?')
        driver.find_element_by_xpath("//*[@id='body']/div[6]/div[7]/div/button").click()
        wait()
        confirmValiText=driver.find_element_by_xpath("//*[@id='body']/div[6]/h2").text
        self.assertEqual(confirmValiText,'排课成功!共排课1次(1小时)')
        #点击"OK,不继续排课"
        driver.find_element_by_xpath("//*[@id='body']/div[6]/div[7]/button").click()
    '''消课'''
    def test_Charge02(self):
        driver = self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        wait()
        # 点击学员管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        driver.find_element_by_xpath("//*[@id='noMar']").clear()
        driver.find_element_by_xpath("//*[@id='noMar']").send_keys("自动化一对一储值")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='keydown-query']").click()
        wait()
        # 点击学员列表记录查看
        driver.find_element_by_xpath(
            "//*[@id='body']/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/table/tbody[1]/tr[1]/td[12]/a").click()
        wait()
        # 点击排课记录tab页
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'排课记录')]")).perform()
        wait()
        # 点击操作
        driver.find_element_by_xpath("//*[@id='nwt+0']/span").click()
        wait()
        # 点击消课
        driver.find_element_by_xpath("//*[@id='body']/popup/div/div/div/ul/li[1]/a").click()
        wait()
        # 是否确认消课
        confirmText = driver.find_element_by_xpath("//*[@id='body']/div[6]/h2").text
        self.assertEqual(confirmText, '是否确认消课？')
        # 点击消课确定
        driver.find_element_by_xpath("//*[@id='body']/div[6]/div[7]/div/button").click()
        wait()
        # 检查消课状态
        state = driver.find_element_by_xpath(
            "//*[@id='body']/div[4]/div/div/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[1]/td[3]").text
        self.assertEqual(state, '已消课')
    '''打印课票'''
    def test_Charge03(self):
        driver = self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        wait()
        # 点击学员管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        driver.find_element_by_xpath("//*[@id='noMar']").clear()
        driver.find_element_by_xpath("//*[@id='noMar']").send_keys("自动化一对一储值")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='keydown-query']").click()
        wait()
        # 点击查看
        driver.find_element_by_xpath(
            "//*[@id='body']/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/table/tbody[1]/tr[1]/td[12]/a").click()
        time.sleep(1)
        # 点击排课记录tab页
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'排课记录')]")).perform()
        wait()
        # 选中操作
        driver.find_element_by_xpath("//*[@id='nwt+0']/span").click()
        wait()
        # 点击打印课票
        driver.find_element_by_xpath("//*[@id='body']/popup/div/div/div/ul/li[1]/a").click()
        wait()
        #检查消课课时正确性
        self.assertEqual(driver.find_element_by_xpath("//*[@id='mt_print']/div/ul[1]/li[9]/span").text,'1')
        # 检查消课金额正确性
        self.assertEqual(driver.find_element_by_xpath("//*[@id='mt_print']/div/ul[1]/li[10]/span").text, '220')
        # 检查计费金额正确性
        self.assertEqual(driver.find_element_by_xpath("//*[@id='mt_print']/div/ul[1]/li[14]/span").text, '220')
        # 检查账户余额正确性
        self.assertEqual(driver.find_element_by_xpath("//*[@id='mt_print']/div/ul[1]/li[16]/span").text, '4780')
    '''取消消课'''
    def test_Charge04(self):
        driver = self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        wait()
        # 点击学员管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        driver.find_element_by_xpath("//*[@id='noMar']").clear()
        driver.find_element_by_xpath("//*[@id='noMar']").send_keys("自动化一对一储值")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='keydown-query']").click()
        wait()
        # 点击学员列表记录查看
        driver.find_element_by_xpath(
            "//*[@id='body']/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/table/tbody[1]/tr[1]/td[12]/a").click()
        wait()
        # 点击排课记录tab页
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'排课记录')]")).perform()
        wait()
        # 点击操作
        driver.find_element_by_xpath("//*[@id='nwt+0']/span").click()
        wait()
        # 点击取消消课
        driver.find_element_by_xpath("//*[@id='body']/popup/div/div/div/ul/li[2]/a").click()
        wait()
        # 选择消课错误
        driver.find_element_by_xpath("//*[@id='body']/div[6]/div/div/form/div[2]/div[2]/a[2]").click()
        # 点击提交
        driver.find_element_by_xpath("//*[@id='body']/div[6]/div/div/form/div[2]/div[3]/button[2]").click()
        wait()
        cancelText = driver.find_element_by_xpath("//*[@id='mt_cancel_consumers']").text
        self.assertEqual(cancelText, '确定取消消课？')
        # 点击确认确定
        driver.find_element_by_xpath("//*[@id='body']/div[8]/div[7]/div/button").click()
        wait()
        # 检查消课状态
        state = driver.find_element_by_xpath(
            "//*[@id='body']/div[4]/div/div/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[1]/td[3]").text
        self.assertEqual(state, '未消课')
        self.assertEqual(driver.find_element_by_xpath(
            "//*[@id='body']/div[4]/div/div/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[1]/td[9]").text, '消课错误')
    '''编辑排课'''
    def test_Charge05(self):
        driver = self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        wait()
        # 点击学员管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        driver.find_element_by_xpath("//*[@id='noMar']").clear()
        driver.find_element_by_xpath("//*[@id='noMar']").send_keys("自动化一对一储值")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='keydown-query']").click()
        wait()
        # 点击查看
        driver.find_element_by_xpath(
            "//*[@id='body']/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/table/tbody[1]/tr[1]/td[12]/a").click()
        time.sleep(1)
        # 点击排课记录tab页
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'排课记录')]")).perform()
        wait()
        # 选中操作
        driver.find_element_by_xpath("//*[@id='nwt+0']/span").click()
        wait()
        # 编辑消课
        driver.find_element_by_xpath("//*[@id='body']/popup/div/div/div/ul/li[2]/a").click()
        wait()
        # 修改科目
        selectLen = Select(driver.find_element_by_xpath("//*[@id='body']/div[6]/div/div/form/div[2]/div[1]/select"))
        selectLen.select_by_index(9)
        wait()
        # 修改教师
        is_selected = driver.find_element_by_xpath(
            "//*[@id='body']/div[6]/div/div/form/div[2]/div[3]/table/tbody[1]/tr[1]/td[1]/input").is_selected()
        driver.find_element_by_xpath(
            "//*[@id='body']/div[6]/div/div/form/div[2]/div[3]/table/tbody[1]/tr[1]/td[1]/input").click()
        # #修改上课时间
        selectLen = Select(driver.find_element_by_name("select.timeSize"))
        selectLen.select_by_index(6)
        wait()
        # 点击提交
        # ActionChains(driver).click(driver.find_element_by_class_name("submit")).perform()
        driver.find_element_by_xpath("//*[@type='submit']").click()
        wait()
        valiText = driver.find_element_by_xpath("//*[@id='body']/div[6]/h2").text
        self.assertEqual(valiText, '排课成功')
        # 点击
        driver.find_element_by_xpath("//*[@id='body']/div[6]/div[7]/div/button").click()
        time.sleep(1)
        # 检查课时编辑成功
        self.assertEqual(driver.find_element_by_xpath(
            "//*[@id='body']/div[4]/div/div/div[2]/div/div/div[3]/div/div/div/table/tbody/tr/td[7]").text, '3')
    '''删除排课'''
    def test_Charge06(self):
        driver = self.driver
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'前台业务')]")).perform()
        wait()
        # 点击学员管理列表
        click = driver.find_element_by_xpath("//*[@id='CustomerStudentManagement']/li[1]/a")
        ActionChains(driver).click(click).perform()
        driver.find_element_by_xpath("//*[@id='noMar']").clear()
        driver.find_element_by_xpath("//*[@id='noMar']").send_keys("自动化一对一储值")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='keydown-query']").click()
        wait()
        driver.find_element_by_xpath(
            "//*[@id='body']/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/table/tbody[1]/tr[1]/td[12]/a").click()
        wait()
        ActionChains(driver).click(driver.find_element_by_xpath("//a[contains(text(),'排课记录')]")).perform()
        wait()
        driver.find_element_by_xpath("//*[@id='nwt+0']/span").click()
        wait()
        # 删除消课
        driver.find_element_by_xpath("//*[@id='body']/popup/div/div/div/ul/li[3]/a").click()
        wait()
        # 检查状态
        # state = driver.find_element_by_xpath("//*[@id='body']/div[6]/h2").text
        # self.assertEqual(state, '确定要删除吗？')
        driver.find_element_by_class_name("confirm").click()
        wait()
    def tearDown(self):
        #关闭浏览器
        self.driver.quit()
def getNowTime():
    return time.strftime("%Y%m%d %H_%M_%S", time.localtime(time.time()))
if __name__=='__main__':
    unittest.main(verbosity=2)


