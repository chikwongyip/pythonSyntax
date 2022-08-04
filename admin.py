from user import User
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privilege = Privileges()
    
    def show_privileges(self):
        for privilege in self.privileges:
            print("Admin " + privilege)

class Privileges():
    def __init__(self,privileges):
        self.privileges = ["can add post","can ban user","can delete post"]
    
