class Dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + " says woof "

class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + " says meow "

niko=Dog("niko")
fred=Cat("fred")

print(niko.speak())

print(fred.speak())


for pet in [niko,fred]:

    print(type(pet))
    print(pet.speak())


def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)

pet_speak(fred)