#coding=utf8


from selenium import  webdriver
import unittest
import time
import HTMLTestRunner


class  MyTest(unittest.TestCase):
    '''百度搜测试'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.baidu.com"

    def test_baidu(self):

        '''selenium关键词搜索'''
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_elements_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title,"selenium_百度搜索")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    print("start")
    suite = unittest.TestSuite()
    suite.addTest(MyTest("test_baidu"))

    #定义报告存放路径
    fp = open('./result.html','wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                            title='百度搜索报告',
                            description='用例执行情况:')
    runner.run(suite)
    fp.close()