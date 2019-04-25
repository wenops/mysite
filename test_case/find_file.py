#coding=utf-8

import os


#定义文件目录
result_dir = 'D:\\mysite\\mysite\\report'

lists = os.listdir(result_dir)

lists.sort(key=lambda fn:os.path.getmtime(result_dir+"\\"+fn))

print(('最新的文件为：'+ lists[-1]))
file = os.path.join(result_dir,lists[-1])
print(file)