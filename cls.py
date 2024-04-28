import math
class leaf(object):
    """A leaf object"""

    def __init__(self, color='green'):
        self.color = color
        pass

    def fall(self, season="autumn"):
        print("a leaf falls in {season}!")


class MapLeaf(leaf):
    def change_color(self):
        if self.color == "green":
            self.color = "yellow"

    def fall(self, season="autumn"):
        self.change_color()
        print(f"A leaf falls in {season}!")


class Student:
    # 定义学生的属性
    def __init__(self, id, name, age):
        self.name = name
        self.age = age

    # 定义学生的行为
    def study(self, course_name):
        print(f'学生正在学习{course_name}')

    def play(self):
        print(f'学生正在玩耍')

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age})'
# 定义一个钟的类
class Clock(object):
    # 钟属性分别有时分秒
    def __init__(self,second,minute,hour):
        self.second = second
        self.minute = minute
        self.hour = hour
    
    # 时钟他自己会走
    def run(self):
        self.second = self.second + 1
        if self.second == 60:
            self.minute = self.minute + 1.
            self.second = 0
            if self.minute == 60:
                self.hour = self.hour + 1
                self.minute = 0
                if self.hour == 24:
                    self.hour = 0
    def show(self):
        print(f'{self.hour}:{self.minute}:{self.second}')

# 屏幕点描述类

class Point(object):
    # 平面点有 x坐标和y坐标属性
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f'该点的x坐标为{self.x},y坐标为{self.y}')
    
    def show_distance(self,des):
        # 两个值得绝对值
        return (abs(self.x - des.x) + abs(self.y -des.y)) ** 0.5