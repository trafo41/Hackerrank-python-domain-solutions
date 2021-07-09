'''' how to use private variables in inheritance'''

class Polygon():
    __width = None                        
    __height = None

    def set_value(self,width,height):
        self.__width = width                          #setter
        self.__height = height

    def get_width(self):
        return self.__width
                                                      #getter
    def get_height(self):
        return self.__height

class Square(Polygon):
    def area(self):
        return self.get_width() * self.get_height()

class Triangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height() * 0.5


s1 = Square()
s1.set_value(41,42)
print(s1.area())
print("----------")

s2 = Triangle()
s2.set_value(41,42)
print(s2.area())
print("----------")