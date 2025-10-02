class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

    def get_info(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Create two dogs
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Make them bark



# Get their info
for d in (dog1, dog2):
    d.bark()
    d.get_info()
