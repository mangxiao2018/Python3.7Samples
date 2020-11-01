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
# 地上:1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,19,20
max_floor_number = 20
# 不吉利的数字列表
not_luck_numbers_list = [14, 18]

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
    v = re.match(r'^(0|[1-9][0-9]*|-[1-9][0-9]*)$', str(arg))
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
    count = calculate(floor_number)
    physics_floor_number = floor_number - count
    display_screen(physics_floor_number, count)

"""
因用户对楼层标识数字的敏感，需要对14，18等不吉利的数字进行剔除
该函数用于计算输入楼层号后，判断是否有包含这些不吉利数字，从而加以计算
如输入15，则实际要进行15-1=14层；
如输入19，则实际要进行19-2=17层。
"""
def calculate(floor_number):
    floor_number = int(floor_number)
    # print("floor_number:" + str(floor_number))
    count = 0
    for i in not_luck_numbers_list:
        if floor_number >= i:
            count = count + 1
    # print("count:" + str(count))
    return count


"""
电梯显示屏显示上升或下降过程楼层并标识是上升还是下降以及当前层
输入0层当1层处理
"""
def display_screen(physics_floor_number, count):
    if (physics_floor_number == 0):
        print("当前物理高度：地上1层")
    elif (physics_floor_number + count) in not_luck_numbers_list:
        print("输入楼层数字标识不存在,当前物理高度：" + ("地上" if physics_floor_number > 0 else "地下") + str(physics_floor_number) + "层")
    else:
        print("当前物理高度：" + ("地上" if physics_floor_number > 0 else "地下") + str(physics_floor_number) + "层")


"""
程序主入口
"""
if __name__ == '__main__':
    run()