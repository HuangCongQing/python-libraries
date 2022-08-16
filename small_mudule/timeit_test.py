'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2022-08-07 21:02:31
LastEditTime: 2022-08-07 21:05:54
FilePath: /python-libraries/small_mudule/timeit.py
'''
''' 
timeit(stmt="pass", setup="pass", timer=default_timer, number=default_number) 函数介绍

timeit() 函数有四个参数，每个参数都是关键字参数，都有默认值。

stmt：传入需要测试时间的代码，可以直接传入代码表达式或单个变量，也可以传入函数。传入函数时要在函数名后面加上小括号，让函数执行，如 stmt = ‘func()’  。

setup：传入 stmt 的运行环境，如 stmt 中使用到的参数、变量，要导入的模块等，如 setup = ‘from __main__ import func’ (__main__表示当前的文件)。可以写一行语句，也可以写多行语句，写多行语句时用分号隔开。

stmt 参数和 setup 参数默认值都是 pass，如果不传值，那么就失去了测试的意义，所以这两个参数是必要的。

timer: timer 参数是当前操作系统的基本时间单位，默认会根据当前运行环境的操作系统自动获取(源码中已经定义)，保持默认即可。

number：要测试的代码的运行次数，默认1000000(一百万)次，对于耗时的代码，运行太多次会花很多时间，可以自己修改运行次数。
————————————————
版权声明：本文为CSDN博主「小斌哥ge」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43790276/article/details/103848054
 '''

# coding=utf-8
def insert_time_test():
    insert_list = list()
    for i in range(10):
        insert_list.insert(0, i)
 
 
def append_time_test():
    append_list = list()
    for i in range(10):
        append_list.append(i)
 
 
# if __name__ == '__main__':
import timeit
insert_time_timeit = timeit.timeit(stmt='insert_time_test()',
                                    setup='from __main__ import insert_time_test')
print('insert_time_timeit: ', insert_time_timeit)
append_time_timeit = timeit.timeit(stmt='append_time_test()', 
                                    setup='from __main__ import append_time_test')
print('append_time_timeit: ', append_time_timeit)