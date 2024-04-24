# coding: utf-8

xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(xinhua)
person = {
    'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号',
    'home': '中同仁路8号', 'tel': '13122334455', 'econtact': '13800998877'
}
print(person)

# 通过zip函数压缩为两个字典
keys = ['name', 'age', 'weight', 'office', 'home', 'tel', 'econtact']
value = ['王大锤', 55, 60, '科华北路62号', '中同仁路8号', '13122334455', '13800998877']

person = dict(zip(keys, value))
print(person)
# 字典遍历
for key in person:
    print(key, person[key])
# 字典运算
print('name' in person)

students = {
    1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'},
    1002: {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
    1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
}
# get方法获取键位的对应的值
print(students.get(1001))
# 获取student 所有键位
print(students.keys())
# 获取student 所有值
print(students.values())

for key, value in students.items():
    print(key, '===>', value)

# 使用pop 方法通过键删除并返回该值
stu1 = students.pop(1002)

key, value = students.popitem(1002)
