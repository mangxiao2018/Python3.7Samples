# @description:用户密码加密作业
# @author:zhangyanqing@
# @date:2020-10-25
# python-version:3.7



import random
import string


def pwd_generator():
    chars = string.ascii_letters
    # 单个数字列表
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # 特殊字符列表
    special_characters = ['@', '#', '$', '%', '^', '&', '*', '~']
    # 随机生成长度为13位的大小写字母组合串
    chars_13 = random.sample(chars, 13)
    # 随机抽取1个特殊字符
    one_spe_char = random.choice(special_characters)
    # 随机抽取1个数字
    one_number = random.choice(number_list)
    # 增加单个特殊字符以及单个数字
    chars_13.extend(one_spe_char)
    chars_13.extend(str(one_number))
    # 二次随机混淆
    random.shuffle(chars_13)
    # 列表转字符串
    strx = "".join(chars_13)
    return strx
"""
生成单用户的密码
"""
def generate_account_pwd(user_name):
    username_pwd_dic = {}
    pwd = pwd_generator()
    username_pwd_dic.setdefault(user_name,pwd)
    return username_pwd_dic
"""
批量生成用户密码
"""
def batch_generate_account_pwd(user_name_list):
    username_pwd_dic = {}
    for user_name in user_name_list:
        username_pwd_dic.setdefault(user_name,pwd_generator())
    return username_pwd_dic

def print_username_pwd(username_pwd_dic):
    for key,value in username_pwd_dic.items():
        print("用户名:"+key+" " + "密码:" + value)

if __name__ == '__main__':
        # 单个用户密码生成测试
        print("单个用户密码生成测试:")
        print(print_username_pwd(generate_account_pwd('zhangsan')))
        # 批量用户密码生成测试
        user_name_list = ['zhangsan','lisi','wangwu']
        print("批量用户密码生成测试:")
        print(print_username_pwd(batch_generate_account_pwd(user_name_list)))