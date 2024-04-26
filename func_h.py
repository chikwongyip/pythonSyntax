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
