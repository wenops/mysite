#coding=utf-8

import unittest
from HTMLTestRunner import HTMLTestRunner
from report import test_baidu
from report import test_360

test_dir = './report'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
suite =  unittest.TestSuite()
suite.addTest(test_baidu.MyTest("test_baidu"))
suite.addTest(test_360.MyTest("test_360"))


if __name__ == '__main__':
    filename = test_dir + '/' + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='测试用例执行情况'
                            )
    runner.run(discover)
    fp.close()