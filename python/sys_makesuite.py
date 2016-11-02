# coding=utf-8
import unittest
import sys
sys.path.append("\\testcase")

from testcase import baidu
from testcase import baidumap
from testcase import baidushiping

import HTMLTestRunner
# 导入测试用例

utest = unittest.TestSuite()

utest = unittest.TestSuite()

utest.addTest(unittest.makeSuite(baidu.Baidu))
utest.addTest(unittest.makeSuite(baidumap.Baidumap))
utest.addTest(unittest.makeSuite(baidushiping.Baidushiping))

# 执行测试
# runner=unittest.TextTestRunner()

# 定义报告存放路径
filename = "D:\\python\\report\\sys.html"
fp = file(filename, "wb")

# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u"测试报告",
    description=u"用例执行情况")
runner.run(utest)
