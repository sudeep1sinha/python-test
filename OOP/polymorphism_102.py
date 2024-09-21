class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError ("subclass must implement this abstract method")


class Dog(Animal):
    def speak(self):
        return self.name + " says woof"

class Cat(Animal):
    def speak(self):
        return self.name + " says meow"


john=Dog("john")

henry=Cat("henry")

print(john.speak())

print(henry.speak())

