# coding: utf-8

# 无序性
# 互异性

# 重复的元素不会出现在集合中

set1 = {1, 2, 3, 3, 2, 12, 34}
print(set1)

# 集合构造器
set2 = set('hello')
print(set2)

set3 = {num for num in range(1, 20) if num % 3 == 0 or num % 5 == 0}
print(set3)

# 集合元素遍历
for elem in set3:
    print(elem)

# 集合运算
print(11 in set3)
print(11 not in set3)

# 交集
print(set3 & set1)
# 并集
print(set1 | set3)
print(set1.union(set3))
# 差集
print(set1 - set3)
print(set1.difference(set3))
# 对称差
print(set1 ^ set3)
print(set1.symmetric_difference(set3))

# 集合的方法
set1 = set()
set1.add(1)
set1.add(33)
set1.update(set3)
# 删除元素
set1.discard(1)
# remove方法删除指定元素建议先做判断再删除
if 10 in set1:
    set1.remove(10)
# 删除随机元素
rd = set1.pop()
# 清空集合
set1.clear()

