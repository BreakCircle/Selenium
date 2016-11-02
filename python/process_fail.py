# coding=utf-8
import unittest
import time
import commands
import os
import multiprocessing
import HTMLTestRunner
import sys

sys.path.append("\\testcase")


def creat_suite():

    folder_dir = []
    lista = os.listdir("D:\\python\\testcase\\")
    for x in lista:
        if "thread" in x:
            folder_dir.append(x)
    print folder_dir

    suite = []

    for n in folder_dir:
        utest = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(
            str(n), pattern="*.py", top_level_dir=r"D:\\")
        for test_suite in discover:
            for testcase in test_suite:
                utest.addTests(testcase)
        suite.append(utest)
    return suite, folder_dir


def RunnerCase(suite, folder_dir):
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    filename = "D:\\python\\report" + now + "process_thread.html"
    fp = file(filename, "wb")
    prolist = []
    s = 0
    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp, title="folder_dir[s]" + u"多进程测试", description=u"用例执行情况")
    pro = multiprocessing.Process(target=runner.run, args=(i,))
    prolist.append(pro)
    s = s + 1
    for pro in prolist:
        pro.start()
    for pro in prolist:
        pro.join()
    fp.close()

if __name__ == '__main__':
    creat_suite()
    RunnerCase()
