# 不能确定是否能正确执行代码
# try:

#     num = int(input("输入一个整数"))
#     print(num)
# except:
#     print('不能识别数字')

try:
    num = int(input("输入一个整数"))
    res = 8 / num
except ZeroDivisionError:
    print("不能除以0")
except Exception as e:
    print("未知错误", e)
else:
    print("执行成功")
finally:
    print("无论如何都会执行")
