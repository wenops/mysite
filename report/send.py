#coding=utf-8
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


#发送邮箱服务器
smtpserver = 'smtp.qq.com'
#发送邮箱用户/密码
user = '671313512'
password = 'oiesdcrcgrtqbcdb'
#发送邮箱
sender = '671313512@qq.com'

#接受邮箱
receiver = 'dengwenyong@redbirdedu.com'
#发送邮件主题s
subject = 'Python email test'

#编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['From'] =  formataddr(['发件人昵称',sender])
msg['To'] = formataddr(['收件人昵称',receiver])
msg['Subject'] = Header(subject,'utf-8')

#连接发送邮件
smtp = smtplib.SMTP_SSL(smtpserver,465)
smtp.login(sender,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()