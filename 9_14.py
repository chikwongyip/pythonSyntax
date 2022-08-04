from random import randint
class Die():
    def __init__(self,sides):
        self.sides = 6

    def roll_sides(self):
        count = 0
        while count <= self.sides:
            
            print(randint(1,self.sides))
            count += 1
            
