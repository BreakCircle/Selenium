# coding=utf-8
import HTMLTestRunner
import time
import unittest
import os


class Test(unittest.TestCase):
     """通过时间计划来执行用例"""

    def test_creatsuite(utest):
        utest = unittest.TestSuite()
        lista = "D:\\python\\testcase\\testcase1"
        print lista
        discover = unittest.defaultTestLoader.discover(
            lista,
            pattern="*.py",
            top_level_dir= None)

        for test_suite in discover:
            for test_case in test_suite:
                utest.addTests(test_case)
        print utest

        alltestnames = utest
        # 执行用例
        now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
        filename = "D:\\python\\report\\" + now + "discover.html"
        fp = file(filename, "wb")
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u"测试报告",
            description=None)
        #设定时间
        while True:
            time_per = time.strftime("%H-%M",time.localtime(time.time()))
            if time_per == "17-00":
                print u"开始测试"
                runner.run(alltestnames)
                print u"测试完成"
                break
            else:
                time.sleep(5)
                print time_per
        #注释掉while 也可直接执行这步
        # runner.run(alltestnames)
        

if __name__ == '__main__':
    unittest.main()
