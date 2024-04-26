# coding： utf-8

# 可变参数
import random
import string
from os.path import splitext


def add(*args):
    total = 0
    for val in args:
        if type(val) == int or type(val) == float:
            total = total + val
    return total


# 设计一个生成验证码的函数
def generate_verification_code(length=4):
    # 生成一个由数字和字母组成的字符串
    verification_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return verification_code


for _ in range(10):
    print(generate_verification_code())


# 设计一个函数返回给定文件的后缀名
def get_file_extension(file_name):
    # 获取文件名中的最后一个点
    dot_index = file_name.rfind(".")
    # 如果找到点，则返回文件名从最后一个点到最后的部分
    if dot_index != -1:
        return file_name[dot_index:]
    else:
        return ""


def get_suffix(filename, ignore_dot=True):
    if ignore_dot:
        return splitext(filename)[1][1:]
    else:
        return splitext(filename)[1]


print(get_suffix('example.txt', ignore_dot=False))
print(get_suffix('example.txt', ignore_dot=True))


def calc(*args, **kwargs):
    result = 0
    for arg in args:
        if type(arg) in (int, float):
            result += arg
    for value in kwargs.values():
        if type(value) in (int, float):
            result += value
    return result


# map 和 filter 高阶用法

def is_even(num):
    return num % 2 == 0


def square(num):
    return num ** 2


numbers = [35, 12, 9, 99, 52]
numbers2 = list(map(square, numbers))
print(numbers2)
numbers2 = list(map(square, filter(is_even, numbers)))
print(numbers2)

# Lambda 函数
# 以函数作为参数而且只有一行
numbers2 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(numbers2)
