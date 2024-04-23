# coding： utf-8

# 字符串定义
s1 = 'hello world'
s2 = "你好世界"
s3 = """
hello
world
"""
print(s3, end='')
# 转义字符和原始字符串
s4 = 'hello\nworld'
s5 = '\\hellow, world\\'

print(s4, s5)

s1 = '\time up \now'
s2 = r'{"time":1,"name":"json"}'
print(s1, s2)

# 字符串操作
s1 = 'hello world' + '!'
s2 = 'hello' * 3

# 成员运算
s1 = 'hello world'
print('o' in s1)

# 获取字符串的长度
print(len(s1))

# 索引和切片
s = 'abc123456'
N = len(s)
print(s[:3], s[-N])
print(s[::-1])
# 字符串遍历
for index in range(len(s)):
    print(s1[index])
for ch in s:
    print(ch)

# 字符串方法
s = 'hello world'
# 第一个字符大写
print(s.capitalize())
# title方法
print(s.title())
# upper方法
print(s.upper())
s = 'GOOD BYE'
# 转换为小写
print(s.lower())

# 性质判断
s = 'hello'
print(s.startswith('HE'))
s2 = 'hjkl123213'
print(s2.isalpha())
# 检查是否以数字和字符构成
print(s2.isalnum())
# 格式化填充
print(s.center(20, '*'))
# 左侧填充
print(s.rjust(20, '*'))
# 右侧填充
print(s.ljust(20, '*'))

print('{0} * {1} = {2}'.format(3, 4, 3 * 4))
# 用f开头来嵌入变量
a = 12321
b = 789
print(f'{a} * {b} = {a * b}')

# 修剪字符串
s = '     527439024@qq.com   \t\r\n'
print(s.strip())