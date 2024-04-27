# coding:utf-8
import random
import time
from functools import wraps


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(result)
        end = time.time()
        print(f'{func.__name__}执行时间：{end - start:.2f}秒')

    return wrapper


@record_time
def download(filename):
    print(f'开始下载文件{filename}')
    time.sleep(random.randint(2, 6))
    print(f'文件{filename}下载完成')
    return True


@record_time
def upload(filename):
    print(f'开始上传文件{filename}')
    time.sleep(random.randint(2, 6))
    print(f'文件{filename}上传完成')
    return False


download('MYSQL从衫裤到跑路.avi')
upload('python从入门到住院.pdf')


# 有下结构{"id":1,"name":"happy","parent_id":0},
# 请用python实现一个递归函数，将上述数据转换为列表结构

def build_tree(data, parent_id=0):
    tree = []
    for item in data:
        if item['parent_id'] == parent_id:
            children = build_tree(data, item['id'])
            if children:
                item['children'] = children
            tree.append(item)
    return tree


data = [
    {"id": 1, "name": "happy", "parent_id": 0},
    {"id": 2, "name": "lucy", "parent_id": 1},
    {"id": 3, "name": "john", "parent_id": 1},
    {"id": 4, "name": "tom", "parent_id": 2},
    {"id": 5, "name": "jerry", "parent_id": 3}]

tree = build_tree(data)
print(tree)
