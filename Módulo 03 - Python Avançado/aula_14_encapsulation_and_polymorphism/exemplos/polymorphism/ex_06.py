class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")
 
class Dog(Animal):
    def speak(self):
        return "Woof!"
 
class Cat(Animal):
    def speak(self):
        return "Meow!"
 
# Create a list of Animal objects
animals = [Dog(), Cat()]
 
# Call the speak method on each object
for animal in animals:
    print(animal.speak())


""" 
Woof!
Meow!
"""