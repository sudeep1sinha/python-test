class Dog():

    species='mammal'
    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots

    def bark(self):
        print("woof! name is {}".format(self.name))

        
my_dog=Dog(breed='lab',name='kahti',spots=False)


print(my_dog.breed)

my_dog.name

my_dog.spots

print(my_dog.bark())

print(my_dog.species)