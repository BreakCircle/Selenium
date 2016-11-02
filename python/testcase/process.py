from multiprocessing import Process
import os


def inf(title):
    print title
    print 'process id:', os.getpid()


def fss(name):
    inf('cc')
    print name

if __name__ == '__main__':

    inf('sss')
    p = Process(target=fss, args=("shuai",))
    p.start()
    p.join()
