# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱
sender = "zs7224250@163.com"

# 接收邮箱
receiver = "469907467@qq.com"

# 发送主题
subject = "python test "

# 发送到邮箱服务器
smtpserver = "smtp.163.com"

# 发送邮箱账户密码

username = "zs7224250@163.com"
passport = "zs2009110"

file_add = open("zsmail.txt", "rb")
poem = file_add.read()

# 中文需要参数“utf-8”，单字节字符不需要
msg = MIMEText(poem, "text", "utf-8")
msg["Subject"] = Header(subject, "utf-8")

smtp = smtplib.SMTP()
smtp.connect("smtp.163.com")
smtp.login(username, passport)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
