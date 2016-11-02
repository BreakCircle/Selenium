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
    lista = os.listdir("D:\\python\\testcase")
    for x in lista:
        if "thread" in x:
            folder_dir.append(x)
    print folder_dir

    suite = []
    utest = unittest.TestSuite()
    for testcase in folder_dir:
        listb = "D:\\python\\testcase\\" + testcase
        print listb

        discover = unittest.defaultTestLoader.discover(
            listb, pattern="start_*.py", top_level_dir= None)

        for test_suite in discover:
            for test_case in test_suite:
                utest.addTests(test_case)
    print utest

    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    filename = "D:\\python\\report\\" + now + "process_thread.html"
    fp = file(filename, "wb")
    proclist = []
    s = 0
    for i in utest:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp, title=str(folder_dir[s]) + u"多进程测试", description=u"用例执行情况")
        # runner.run(i)
    proc = multiprocessing.Process(target=runner.run, args=(i,))
    proclist.append(proc)
    s = s + 1
    
    for proc in proclist:
        proc.start()
    for proc in proclist:
        proc.join()
    

if __name__ == '__main__':
    creat_suite()
    # RunnerCase(m[0], m[1])
