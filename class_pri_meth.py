""" class Speed:
    def __init__(self):
        self.speed = 10
        self.__new_speed = 80

    def get_new_speed(self):
        return self.__new_speed

s = Speed()
print(s.get_new_speed()) """

class Speed:
    def __init__(self):
        self.x = 10
        self.y = 80
        self.z = 40
    
    def public_method(self):
        print(self.x)
        print(self.y)
        print(self.z)
        self.__private_method()

    def __private_method(self):
        print("Inside private method")
        print("----------------")


s = Speed()
s.public_method() 