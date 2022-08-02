class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.distance = 0
    
    def get_descriptive(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def get_distance(self):
        print("Models had been ran " + str(self.distance) + ' KM')
    
    def update_distance(self,distance):
        """修改车的公里数"""
        self.distance = distance

if __name__ == "__main__":
    my_tesla = Car('Tesla','Models','2022')
    print(my_tesla.get_descriptive())
    my_tesla.get_distance()