# coding:utf-8
import random
import time
from threading import Thread


def download(*, file_name):
    start = time.time()
    print(f'开始下载{file_name}')
    time.sleep(random.randint(3, 6))
    print(f'{file_name}下载完成，耗时{time.time() - start}秒')


def main():
    start = time.time()
    download(file_name='python入门到跑路.pdf')
    download(file_name='java从入门到入土.pdf')
    download(file_name='linux从精通到放弃.pdf')
    end = time.time()
    print(f'所有文件下载完成，总耗时{end - start}秒')


def main_thread():
    threads = [
        Thread(target=download, kwargs={'file_name': 'python入门到跑路.pdf'}),
        Thread(target=download, kwargs={'file_name': 'java从入门到入土.pdf'}),
        Thread(target=download, kwargs={'file_name': 'linux从精通到放弃.pdf'})
    ]
#     启动线程
    start = time.time()
    for thread in threads:
        thread.start()

#     等待所有线程执行完毕
    for thread in threads:
        thread.join()
    end = time.time()
    print(f'所有文件下载完成，总耗时{end - start}秒')


if __name__ == '__main__':
    # main()
    main_thread()