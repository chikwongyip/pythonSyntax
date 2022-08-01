class leaf(object):
    """A leaf object"""
    def __init__(self,color = 'green'):
        self.color = color
        pass
    def fall(self,season="autumn"):
        print("a leaf falls in {season}!")

class MapLeaf(leaf):
    def change_color(self):
        if self.color == "green":
            self.color = "yellow"
    def fall(self,season="autumn"):
        self.change_color()
        print(f"A leaf falls in {season}!")
        