""" class Student:
    message  =  "hello there"
    
    def __init__(self,n,a,m=0):
        self.name  = n
        self.age  = a
        self.marks  = m
        
    def display(self):
        print("-----------------------------")
        print("Your name : ", self.name)
        print("Your age : ", self.age)
        print("Your marks : ", self.marks)
        print("-----------------------------")
#        print("Message : ", self.message)

s1 = Student("veer", 22)
s1.display() """

""" class Student:
    message  =  "hello there"
    
    def __init__(self,n,a,*m):
        self.name  = n
        self.age  = a
        self.marks  = m
        
    def display(self):
        print("-----------------------------")
        print("Your name : ", self.name)
        print("Your age : ", self.age)
        print("Your marks : ", self.marks)
        print("-----------------------------")
#        print("Message : ", self.message)

s1 = Student("veer", 22, 95,56,98)
s1.display() """

class Student:
    message  =  "hello there"
    
    def __init__(self,n,a,**m):
        self.name  = n
        self.age  = a
        self.marks  = m
        
    def display(self):
        print("-----------------------------")
        print("Your name : ", self.name)
        print("Your age : ", self.age)
        print("Your marks : ", self.marks)
        print("-----------------------------")
#        print("Message : ", self.message)

s1 = Student("veer", 22, science =  95, math = 56, phy = 98)
s1.display()