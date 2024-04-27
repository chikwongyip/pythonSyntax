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


stu1 = Student(1, 'happy', '40')
print(stu1)
