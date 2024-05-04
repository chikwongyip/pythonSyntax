# coding:utf-8

import json
import csv
import random
import re

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
print(json.dumps(my_dict))

# with open('source.csv', 'w') as file:
#     writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)
#     writer.writerow(['姓名', '语文', '数学', '英语'])
#     names = ['关羽', '张飞', '赵云', '马超', '黄忠', '刘备', '曹操', '孙权', '周瑜', '吕蒙']
#     for name in names:
#         scores = [random.randrange(50, 101) for _ in range(4)]
#         scores.insert(0, name)
#         writer.writerow(scores)
# 读取csv
with open('source.csv', 'r') as file:
    reader = csv.reader(file, delimiter='|')
    for row in reader:
        print(row)

# username = input('请输入qq号码')
#
# if re.match(r'^[1-9]\d{4,10}$', username):
#     print('qq号码格式正确')
# else:
#     print("qq号码格式不正确")
# 创建查找手机的正则表达式
phone_regex = re.compile(r'(?<=\D)1[3456789]\d{9}(?=\D)')
sentence = ("""我的手机号是13812345678，我的QQ号是123456789，我的邮箱是zhangsan@sina.com。'
            '重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也是110或119，王大锤的手机号才是15600998765""")
tels_list = re.findall(phone_regex, sentence)
for _list in tels_list:
    print(_list)

for temp in phone_regex.finditer(sentence):
    print(temp.group())

# m = phone_regex.search(sentence)
# while m:
#     print(m.group())

