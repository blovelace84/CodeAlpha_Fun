class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(thing):
    thing.quack()

#Create an instance
duck = Duck()
person = Person()

#Pass the object to the function
make_it_quack(duck)
make_it_quack(person)

