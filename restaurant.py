class Restaurant(object):
    """a little restaurant"""
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_server = 0

    def get_number_served(self,number_server):
        print("目前就餐人数:" + str(number_server))
    
    def set_number_server(self,max_number):
        self.number = max_number

    def increment_number_server(self,number):
        self.number_server -= number

    def describe_restaurant(self):
        print("Welcome to " + self.name.title() + 'restaurant!')
        print("Hope you enjoy" + self.cuisine_type + "food")

    def open_restaurant(self):
        print("Hell welcome, {self.cuisine_type},{self.name}")

if __name__ == '__main__':
    dogRestaurant = Restaurant('Happy','dog')
    dogRestaurant.open_restaurant()
    dogRestaurant.describe_restaurant()