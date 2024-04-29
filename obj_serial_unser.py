# coding:utf-8

import json
import csv
import random

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
