class Animal():
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
    def good(self):
        print(f"{self.name} is good animal")

class Dog(Animal):
    pass
class Cat(Animal):
    pass
class rabbit(Animal):
    pass

dog = Dog("scobby")
print(dog.name)