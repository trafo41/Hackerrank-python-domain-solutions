class Student:
    message  =  "hello there"
    
    def __init__(self):
        self.name  = "nothing"
        self.age  = 22
        self.marks  = 0
        
    def talk(self):
        print("Your name : ", self.name)
        print("Your age : ", self.age)
        print("Your marks : ", self.marks)
        print("Message : ", self.message)

s1 = Student()
s1.name = "veer"
s1.talk()

s2 = Student()
s2.message = "this also works"
s2.talk()