# coding=utf-8
import os
import datetime
import time


report_dir="D:\\python\\report"
lists=os.listdir(report_dir)
lists.sort(key=lambda x: os.path.getmtime(report_dir + "\\" + x)
           if not os.path.isdir(report_dir + "\\" + x) else 0)
file=os.path.join(report_dir, lists[-1])
print file
