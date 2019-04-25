#coding=utf-8

import unittest
from HTMLTestRunner import HTMLTestRunner
from test_case import test_baidu, test_360
import time
import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

#定义发送邮件
def send_mail(file_new):
    f = open(file_new,'rb')
    sendfile = f.read()
    f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.qq.com'
    # 发送邮箱用户/密码
    user = '671313512'
    password = '*****'
    # 发送邮箱
    sender = '671313512@qq.com'

    # 接受邮箱
    receiver = 'dengwenyong@redbirdedu.com'
    # 发送邮件主题s
    subject = 'Python email test'

    # 发送的附件
    #sendfile = open('D:\\mysite\\mysite\\report\\result.html', 'rb').read()
    msg = MIMEText(sendfile,'html','utf-8')
    msg['Subject'] = subject
    msg['From'] = formataddr(['', sender])
    msg['To'] = formataddr(['', receiver])
    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("email has send out")

def find_file(dir):
    lists = os.listdir(dir)

    lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn))

    print(('最新的文件为：' + lists[-1]))
    file = os.path.join(dir, lists[-1])
    print(file)
    return file




# test_dir = './test_case'
# discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
# suite =  unittest.TestSuite()
# suite.addTest(test_baidu.MyTest("test_baidu"))
# suite.addTest(test_360.MyTest("test_360"))
# now = time.strftime("%Y_%m_%d %H_%M_%S")

if __name__ == '__main__':
    # filename = './report' + '/'+ now + 'result.html'
    # fp = open(filename,'wb')
    # runner = HTMLTestRunner(stream=fp,
    #                         title='测试报告',
    #                         description='测试用例执行情况'
    #                         )
    # runner.run(discover)
    # fp.close()
    # dir = 'D:\\mysite\\mysite\\report\\'
    # send_mail(file)
    # find_file(dir)
    test_dir = 'D:\\mysite\\mysite\\test_case'
    test_report = 'D:\\mysite\\mysite\\report'

    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='test_*.py'
                                                   )
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况：'
    )
    runner.run(discover)
    fp.close()
    new_report = find_file(test_report)
    send_mail(new_report)
