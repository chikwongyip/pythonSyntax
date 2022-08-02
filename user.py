class User(object):
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print("My name is "+ self.first_name + self.last_name)
    
    def greet_user(self):
        self.describe_user()
        print("I live in ZhongShan")
        print("I love happy")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

if __name__ == "__main__":
    happyUser = User("Yip","Happy")
    happyUser.describe_user()
    happyUser.greet_user()
