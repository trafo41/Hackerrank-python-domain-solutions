class Speed:
    def __init__(self):
        self.speed = 10
        self.__new_speed = 80

s = Speed()
# print(s.new_speed)                                #error, since neww_sspeed is private
s.speed = 60
s.new_speed = 100


print("-----------------------")
print(s.speed)
print(s.new_speed)
print("-----------------------")
