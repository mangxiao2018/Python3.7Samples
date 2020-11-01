# coding=utf-8

# @description:电梯模拟程序作业
# @author:zhangyanqing@
# @date:2020-10-20
# python-version:3.7

import re

# 电梯加电运行时初始楼层为第1层
current_floor_number = 1
# 本楼最底层楼实际最低层数
# 地下:-1,-2,-3
min_floor_number = -3
# 本楼最高层楼实际高层数
# 地上:1,2,3,5,6,7,8,9,10,11,12,13,15,16,17,19,20
max_floor_number = 20
# 不吉利的数字列表
not_luck_numbers_list = [0,4,14,18]

"""
开始运行
"""
def run():
    panel_btn()

"""
面板按键函数
"""
def panel_btn():
    stop = False
    while not stop:
        try:
            str = input("请按楼层按键:")
        except IOError:
            print("输入IO异常")
        if validate_is_number(str) and validate_range(str):
            control(str)
        else:
            print("输入格式不正确,请您输入-3至20层楼层数字")
"""
通过正则表达式校验输入是否合规:
1.输入必须为数值类型数据
"""
def validate_is_number(arg):
    pattern_expression = r'^([1-9][0-9]*|-[1-9][0-9]*)$'
    v = re.match(r'^([1-9][0-9]*|-[1-9][0-9]*)$', str(arg))
    # print(v)
    if v:
        return True
    else:
        return False

"""
验证数值范围
1.最小值只能大于等于本楼最底层数值
2.最大值只能小于等于本楼最高层数值
"""
def validate_range(arg):
    v = int(arg)
    if v > max_floor_number:
        return False
    elif v < min_floor_number:
        return False
    else:
        return True
"""
主逻辑控制函数
"""
def control(floor_number):
    global current_floor_number
    floor_number = int(floor_number)
    run_list = []
    if (floor_number > current_floor_number):
        for i in range(current_floor_number,floor_number+1):
            if i not in not_luck_numbers_list:
                run_list.append(i)
    else:
        for i in range(floor_number,current_floor_number+1):
            if i not in not_luck_numbers_list:
                run_list.append(i)
    display_screen(run_list,floor_number)

"""
电梯显示屏显示上升或下降过程楼层并标识是上升还是下降以及当前层
"""
def display_screen(run_list,floor_number):
    global current_floor_number
    floor_number = int(floor_number)
    # print(type(floor_number))
    if floor_number > current_floor_number:
        for i in run_list:
            print(str(i) + "楼" + "↑")
    elif floor_number < current_floor_number:
        for i in run_list:
            print(str(i) + "楼" + "↓")
    else:
        print(str(floor_number) + "楼" + "←→")
    current_floor_number = floor_number

"""
程序主入口
"""
if __name__ == '__main__':
    run()
    # x = validate('_123')
    # print(x)