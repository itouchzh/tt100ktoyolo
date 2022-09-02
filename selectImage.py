# -*- coding: utf-8 -*-
# @Time    : 2022/9/2
# @Author  : rickHan
# @Software: PyCharm
# @File    : selectImage.py
# 选出test中没有的图片和其他文件。
import os

f = open("./txtLabel/test.txt")  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
totalImage = []
i = 0

with open('./txtLabel/test.txt','r') as f:
    line = f.readlines()
    print(line)
    for i in line:
        i = i.strip('\n') + '.jpg'
        totalImage.append(i)
    f.close()
# while line:
#     # print line,  # 后面跟 ',' 将忽略换行符
#     # print(line, end = '')　      # 在 Python 3 中使用
#     line = f.readline()
#     line = line.strip('\n')
#     line = line + '.jpg'
#     totalImage.append(line)
#     i = i + 1
#     if i == 3064:
#         break
#     # print(line)
# f.close()
print(totalImage)
# totalImage.append('10056.jpg')
print(len(totalImage))
# #
# # # 提取文件夹中文件名字。
for filename in os.listdir(r'G:\论文资料\源码\数据集\交通标志\tt100k\data\test'):
    # print("111"+filename)
    if filename not in totalImage:
        print(filename)


