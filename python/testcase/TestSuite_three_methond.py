# coding=utf-8
import unittest
import HTMLTestRunner
import time
# 导入测试用例
import baidu
import baidumap
import baidushiping
import mail
utest = unittest.TestSuite()

# 导入用例方式一：list
alltestcase = [baidu.Baidu, baidumap.Baidumap, baidushiping.Baidushiping]
for test in alltestcase:
    utest.addTest(unittest.makeSuite(test))

# 导入用力方式二：discover
lista = "D:\\python\\testcase\\testcase"
discover = unittest.defaultTestLoader.discover(
    lista,
    pattern="start_*.py",
    top_level_dir=None)
for test_suite in discover:
    for test_case in test_suite:
        utest.addTests(test_case)
        print utest

# 导入用例方式三：一个个addTest
utest.addTest(unittest.makeSuite(baidu.Baidu))
utest.addTest(unittest.makeSuite(baidumap.Baidumap))
utest.addTest(unittest.makeSuite(baidushiping.Baidushiping))

# 执行测试
# runner=unittest.TextTestRunner()
now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
filename = 'D:\\python\\report\\' + now + 'alltest.html'
fp = file(filename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u"测试报告",
    description=u"用例执行情况")
runner.run(utest)

#调用发邮件模块
mail.Send_mail()
