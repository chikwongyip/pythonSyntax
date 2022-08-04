from restaurant import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine_type):
        super().__init__(name,cuisine_type)
        self.flavor = ["banana","strawberry","apple"]
    
    def show_icecream(self):
        for taste in self.flavor:
            print("Icecream flavor we have" + taste)

        