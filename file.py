# coding：utf-8
file = None

try:
    file = open('致像树.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print('文件不存在')
except LookupError:
    print('指定了未知编码')
except UnicodeDecodeError:
    print('读取文件解码错误')
finally:
    if file:
        file.close()

# 上下文语法

try:
    with open('致像树.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('文件不存在')
except LookupError:
    print('指定了未知编码')
except UnicodeDecodeError:
    print('读取文件解码错误')

# 读取图片二进制

try:
    with open('致像树.jpg', 'rb') as file:
        print(file.read())

except FileNotFoundError:
    print('文件不存在')

except LookupError:
    print('指定了未知编码')

except UnicodeDecodeError:
    print('读取文件解码错误')
