from car import Car

class ElectricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,mode,year)
    
if __name__ == "__main__":
    my_tesla = ElectricCar("tesla","model s","2022")
    print(my_tesla.get_descriptive_name()) 