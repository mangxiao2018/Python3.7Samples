# coding=utf-8

# @description:电梯模拟程序作业
# @author:zhangyanqing@
# @date:2020-10-20
# python-version:3.7

import re

def read_file():
    digits = letters = spaces = others = 0
    file = open('data.txt','r')
    try:
        for line in file:
            for c in line:
                if c.isdigit():
                    digits += 1
                elif c.isalpha():
                    letters += 1
                elif c.isspace():
                    spaces += 1
                else:
                    others += 1
        file.close()
        print("文件中数字共：" + str(digits))
        print("文件中字母共：" + str(letters))
        print("文件中空格共：" + str(spaces))
        print("文件中其它共：" + str(others))
    except IOError:
        print("文件读取失败")


"""
程序主入口
"""
if __name__ == '__main__':
    read_file()