# coding: utf-8

t1 = (30, 10, 55)
t2 = ('happy', 'bear', '薯条')
# 遍历元组
for i in t1:
    print(i)

# 检查元素是否存在元组
print(30 in t1)

# 成员拼接
t3 = t1 + t2

# 切片
print(t3[1:3])

# 空元组
t4 = ()

# 只有一个元素的元组
t5 = (1,)
# 不是元组
t6 = (123213)

# 元组应用场景
# 打包
a = 1, 10, 100
# 解包
x, y, z = a

# 解包时候，如果元组元素个数和变量个数不一致，会抛出异常 too many value to unpack
# 用*来解决数量不一致的问题
a, b, *c = t1

# 变量交换
x, y = y, x
a, b, c = b, c, a

# 元组转换列表
t1 = list(t1)

# 列表转换元组
t1 = tuple(t1)
