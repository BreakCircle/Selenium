# coding=utf-8

import time
import os
import smtplib
import HTMLTestRunner
import unittest
from email.mime.text import MIMEText


def sendreport():
    report = "D:\\python\\report"
    lists = os.listdir(report)
    lists.sort(key=lambda x: os.path.getmtime(report + "\\" + x)
               if not os.path.isdir(report + "\\" + x) else 0)
    filenew = os.path.join(report, lists[-1])
    sentmail(filenew)


def sentmail(filenew):
    mail_from = "zs7224250@163.com"
    mail_to = "469907467@qq.com"
    username = "zs7224250@163.com"
    passport = "zs2009110"
    f = open(filenew, "rb")
    text = f.read()
    f.close()
    msg = MIMEText(text, "html", "utf-8")
    msg["Subject"] = u"测试报告"
    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login(username, passport)
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print "ok"

if __name__ == '__main__':
    sendreport()
