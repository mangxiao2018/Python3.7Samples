# @description:用户密码加密作业
# @author:zhangyanqing@
# @date:2020-10-25
# python-version:3.7

import random
import string
import re

# a~z and A~Z
chars = string.ascii_letters
# 单个数字列表
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# 特殊字符列表
special_characters = ['@', '#', '$', '%', '^', '&', '*', '~']

"""
1、密码随机生成
2、密码长度15位
3、密码中需要只含一个数字，一个特殊字符，其它包含不限
4.特殊字符自设置
5.密码串中数字和特殊字符位置乱序以防猜防暴力破解
"""
def pwd_generator(pwd_length):
    # 随机生成长度为指定长度的大小写字母组合串,默认是13位
    if pwd_length is None:
        pwd_length = 15
    chars_x = random.sample(chars, pwd_length - 2)
    # 随机抽取1个特殊字符
    one_spe_char = random.choice(special_characters)
    # 随机抽取1个数字
    one_number = random.choice(number_list)
    # 增加单个特殊字符以及单个数字
    chars_x.extend(one_spe_char)
    chars_x.extend(str(one_number))
    # 二次随机混淆
    random.shuffle(chars_x)
    # 列表转字符串
    pwd = "".join(chars_x)
    return pwd

"""
通过正则表达式校验输入是否合规:
1.输入必须为数值类型数据
"""
def validate_is_number(arg):
    pattern_expression = r'^([1-9][0-9]*|-[1-9][0-9]*)$'
    v = re.match(r'^(0|[1-9][0-9]*|-[1-9][0-9]*)$', str(arg))
    # print(v)
    if v and arg <= 18 and arg >= 8:
        return True
    else:
        return False

"""
只生成密码
"""
def generate_only_pwd(pwd_length):
    if not validate_is_number(pwd_length):
        print("密码长度只能输入8到18之间的整数")
        return ''
    pwd = pwd_generator(pwd_length)
    return pwd

"""
生成单用户的密码
"""
def generate_account_pwd(user_name,pwd_length):
    if not validate_is_number(pwd_length):
        print("密码长度只能输入8到18之间的整数")
        return ''
    username_pwd_dic = {}
    pwd = pwd_generator(pwd_length)
    username_pwd_dic.setdefault(user_name,pwd)
    return username_pwd_dic

"""
批量生成用户密码
"""
def batch_generate_account_pwd(user_name_list,pwd_length):
    if not validate_is_number(pwd_length):
        print("密码长度只能输入8(含)到18(含)之间的整数")
        return ''
    username_pwd_dic = {}
    for user_name in user_name_list:
        username_pwd_dic.setdefault(user_name,pwd_generator(pwd_length))
    return username_pwd_dic

"""
打印用户名-密码对
"""
def print_username_pwd(username_pwd_dic):
    if username_pwd_dic is None or username_pwd_dic is '':
        return ''
    for key,value in username_pwd_dic.items():
        print("用户名:"+key+" " + "密码:" + value)
    return ''

"""
主程序入口
"""
if __name__ == '__main__':
        print("只生成指定长度的单一密码")
        print(generate_only_pwd(19)) #异常
        print(generate_only_pwd(18))
        print(generate_only_pwd(17))
        print(generate_only_pwd(7)) #异常
        print(generate_only_pwd(8))
        print(generate_only_pwd(9))
        print(generate_only_pwd('xx')) #异常

        # 1、单个用户密码生成测试
        print("单个用户密码生成测试:")
        print_username_pwd(generate_account_pwd('zhangsan', 19)) #异常
        print_username_pwd(generate_account_pwd('zhangsan', 18))
        print_username_pwd(generate_account_pwd('zhangsan', 17))
        print_username_pwd(generate_account_pwd('zhangsan', 7)) #异常
        print_username_pwd(generate_account_pwd('zhangsan', 8))
        print_username_pwd(generate_account_pwd('zhangsan', 9))
        print_username_pwd(generate_account_pwd('zhangsan', 'xx')) #异常
        print_username_pwd(generate_account_pwd('zhangsan', 0)) #异常

        # 2、批量用户密码生成测试
        user_name_list = ['zhangsan','lisi','wangwu']
        print("批量用户密码生成测试:")
        print_username_pwd(batch_generate_account_pwd(user_name_list, 19)) #异常
        print_username_pwd(batch_generate_account_pwd(user_name_list, 18))
        print_username_pwd(batch_generate_account_pwd(user_name_list, 17))
        print_username_pwd(batch_generate_account_pwd(user_name_list, 7)) #异常
        print_username_pwd(batch_generate_account_pwd(user_name_list, 8))
        print_username_pwd(batch_generate_account_pwd(user_name_list, 9))
        print_username_pwd(batch_generate_account_pwd(user_name_list, 'xx')) #异常
        print_username_pwd(batch_generate_account_pwd(user_name_list, 0)) #异常