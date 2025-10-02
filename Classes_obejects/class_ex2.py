""" Intermediate

Inheritance

Create a parent class Animal with a method eat().

Create two subclasses: Cat and Bird.

Override a method in each subclass (Cat meows, Bird chirps).

Polymorphism

Put your Dog, Cat, and Bird objects in a list.

Loop through the list and call the same method (e.g., make_sound()).

Each animal should make a different sound."""





# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    # General method to be overridden
    def make_sound(self):
        print(f"{self.name} makes a sound.")


# Subclass Cat (inherits from Animal)
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow!")


# Subclass Bird (inherits from Animal)
class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says: Chirp!")


# Your Dog class (also an Animal)
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says: Woof!")


# ✅ Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

# ✅ Polymorphism: Same method, different behaviors
animals = [dog, cat, bird]

for animal in animals:
    animal.eat()         # All animals eat
    animal.make_sound()  # Each makes its own sound
