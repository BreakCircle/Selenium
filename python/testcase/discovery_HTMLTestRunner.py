# coding=utf-8
import HTMLTestRunner
import time
import unittest
import os


class Test(unittest.TestCase):

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
        runner.run(alltestnames)
        

if __name__ == '__main__':
    unittest.main()
