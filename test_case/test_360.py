#coding=utf-8
from selenium import  webdriver
import unittest
import time

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.so.com"

    def test_360(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        driver.find_element_by_id("input").send_keys("webdirver")
        driver.find_element_by_id("search-button").click()
        time.sleep(3)
        title = driver.title

        self.assertEqual(title,"webdirver_360搜索")

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()