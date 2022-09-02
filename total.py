# -*- coding: utf-8 -*-
# @Time    : 2022/9/1
# @Author  : rickHan
# @Software: PyCharm
# @File    : total.py
import os
def getfiles():
    filenames=os.listdir(r'./txtLabel1/test')
    print(filenames)
    total = 0
    for filename in filenames:
        with open('./txtLabel/test.txt','a+') as f:
            filename = filename[:-4]
            f.write(filename + '\n')
            total = total + 1
            print(total)
            f.close()

if __name__ == '__main__':
    getfiles()

