# coding：utf-8

# 基于process类型来创建进程
from multiprocessing import Process, current_process
from time import sleep


def sub_task(content, nums):
    # 通过current_process 函数获取当前进程
    # 通过进程对象pid和name属性获取进程id和名字
    print(f'{content} 进程id：{current_process().pid} 进程名字：{current_process().name}')
    counter, total = 0, nums.pop(0)
    print(f'loop count:{total}')
    sleep(0.5)
    while counter < total:
        counter += 1
        print(f'{counter}:{content}')
        sleep(0.01)


def main():
    nums = [20, 30, 40]
    # 创建进程
    Process(target=sub_task, args=('Ping', nums)).start()
    Process(target=sub_task, args=('Ping', nums)).start()
    sub_task('Good', nums)


def fib(max_count):
    a, b = 0, 1
    for _ in range(max_count):
        a, b = b, a + b
        yield a, b


if __name__ == '__main__':
    # main()
    generator = fib(10)
    print(generator)
    for value in generator:
        print(value)
