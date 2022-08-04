class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("this car has a" + str(self.battery_size) + "kilometers")
    
    