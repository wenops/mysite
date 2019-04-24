#coding=utf-8

from selenium import webdriver
import unittest
import time



class Send_Mail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://mail.qq.com"
        time.sleep(3)

    def test_send(self):
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("u").clear()
        driver.find_element_by_id("u").send_keys("671313512@qq.com")
        driver.find_element_by_id("p").send_keys("wen626026707")
        driver.find_element_by_id("login_button").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()