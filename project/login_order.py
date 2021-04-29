# -*- coding: UTF-8 -*-
import unittest
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class LoginOrderTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.base_url = "https://xdclass.net"
        self.driver.get(self.base_url)


    def tearDown(self):
        print("单个测试用例结束")
        self.driver.quit()
        #单个测试用例结束
    
    def test_login_order(self):
        u"登录测试用例"
        driver = self.driver
        #登录框
        login_ele = driver.find_element_by_css_selector(".login > span:nth-child(2)")
        ActionChains(driver).click(login_ele).perform()

        sleep(2)
        #查找输入框,输入账号，输入框要提前清理里面的数据
        driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").clear()
        driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys("15079146363")
        #查找密码输入框，输入密码
        driver.find_element_by_css_selector(".psw > input:nth-child(1)").clear()
        driver.find_element_by_css_selector(".psw > input:nth-child(1)").send_keys("wodemima")

        #拿到登录按钮
        login_btn_ele = driver.find_element_by_css_selector(".btn")
        #触发点击事件,登录
        login_btn_ele.click()
        #判断登陆是否成功，逻辑-》鼠标移到上面，判断弹窗字符
        #获取鼠标上移的元素
        user_info_ele = driver.find_element_by_css_selector(".avatar_img")
        sleep(1)
        #hover触发
        ActionChains(driver).move_to_element(user_info_ele).perform()
        sleep(1)
        #获取用户名称元素
        user_name_ele = driver.find_element_by_css_selector(".username")
        print("===测试结果==")
        print(user_name_ele.text)

        name = user_name_ele.text
        #self.assertEqual(name, u"二当家小D",msg="登录失败")

        video_ele = driver.find_element_by_css_selector(".hotcourse > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(2)")
        video_ele.click()
        sleep(2)

        #buy_btn_ele = driver.find_element_by_css_selector(".learn_btn > a:nth-child(1)")

        #buy_btn_ele.click()
        print("进入工业级Pass")
       


if __name__ == '__main__':
       unittest.main()

   
