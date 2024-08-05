print("Class and Object")

class Dog:
    # init stands for initialization, and this function is called,
    # when ever an instance of the class Dog is created.
    # this is special python defined thing so the computer will recognize this as the initialization function.
    # self is the first parameter of the function, and it is a reference to the current instance of the class.
    def __init__(self,  name: str):
        self.name = name
        self.legs = 4
        
    def speak(self):
        # there two style to write it.
        # print(self.name + " says Bark!")
        print(f"{self.name} says Bark!")
        
my_dog = Dog("Rover")

dog2 = Dog("Fluffy")


my_dog.speak()

dog2.speak()

# Challenge Solved
def fact(num):
    if type(num) != int or num < 0: 
        return None
    return 1 if num <= 0 else num * fact(num - 1)
    

print(fact(5))
print(fact(6))
print(fact("span span"))
print(fact(-2))