#coding:utf-8
import  unittest
from appium import  webdriver
import sys, os,time
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from Page.BaseLoginPage  import AppBaseLogin
from model import Model
from model.Model import DataHelper


class AppStudentBuyTest(AppBaseLogin):
    #@unittest.skip('test')
    def testLogin(self):
        time.sleep(1)
        teachername='王美丽'
        selectCourse_loc = self.driver.find_element_by_id("com.youwinedu.student:id/r_second")
        selectCourse_loc.click()
        time.sleep(1)
        loc_loc = self.driver.find_element_by_id("com.youwinedu.student:id/tv_location")
        loc_loc.click()
        time.sleep(1)
        city_loc = self.driver.find_element_by_name("天津市")
        city_loc.click()
        time.sleep(1)
        find_loc = self.driver.find_element_by_id("com.youwinedu.student:id/iv_find")
        find_loc.click()
        time.sleep(2)
        teacherName_loc = self.driver.find_element_by_id("com.youwinedu.student:id/edittext").send_keys(teachername)
        time.sleep(2)
        self.driver.keyevent(66)#回车
        time.sleep(1)
        valit_loc = self.driver.find_element_by_id("com.youwinedu.student:id/tv_name").text
        self.assertEqual('王美丽', valit_loc)
        image_loc = self.driver.find_element_by_id("com.youwinedu.student:id/iv_item_rou")
        image_loc.click()
        time.sleep(1)
        join_loc = self.driver.find_element_by_id("com.youwinedu.student:id/bt_now_join")
        join_loc.click()
        time.sleep(1)
        inputName_loc = self.driver.find_element_by_id("com.youwinedu.student:id/tv_content")
        inputName_loc.click()
        time.sleep(1)
        dialog_loc = self.driver.find_element_by_id("com.youwinedu.student:id/et_dialog").send_keys('大黄')
        dialogOk_loc = self.driver.find_element_by_name("确定")
        dialogOk_loc.click()
        time.sleep(1)
        sure_loc = self.driver.find_element_by_id("com.youwinedu.student:id/btn_sure")
        sure_loc.click()
        time.sleep(1)
        pay_loc = self.driver.find_element_by_id("com.youwinedu.student:id/btn_pay")
        pay_loc.click()
        time.sleep(1)
        left_loc = self.driver.find_element_by_id("com.youwinedu.student:id/title_left")
        left_loc.click()
        time.sleep(1)
        left_loc.click()
        time.sleep(1)
        left_loc.click()
        time.sleep(1)
        detail_loc = self.driver.find_element_by_id("com.youwinedu.student:id/iv_teacher_detail_left_back")
        detail_loc.click()
        back_loc = self.driver.find_element_by_id("com.youwinedu.student:id/back")
        back_loc.click()
        history_loc = self.driver.find_element_by_id("com.youwinedu.student:id/iv_seach_history_left_back")
        history_loc.click()
        # # WebDriverWait(self.driver,10000).until(EC.invisibility_of_element_located((By.ID,"com.youwinedu.student:id/rl_login_model")))
        # loginLink_loc = self.driver.find_element_by_id("com.youwinedu.student:id/rl_login_model")
        # loginLink_loc.click()
        # self.wait
        # self.login(username,password)
        # self.wait
        # valit_loc = self.driver.find_element_by_id("com.youwinedu.student:id/tv_use_name").text
        # self.assertEqual('大虫自动化', valit_loc)
if __name__ == '__main__':
    unittest.main(verbosity=2)

