"""
Classes in Python are like blueprints to create objects.
Each object can have properties (attributes) and behaviors (methods).
Example: a base class Vehicle that represents a generic vehicle.
"""

# ===============================
# 1. Base Class (Parent)
# ===============================
class Vehicle:
    # constructor: defines object properties
    def __init__(self, make, model):
        self.make = make      # brand
        self.model = model    # model

    # generic method
    def moves(self):
        print("moves along")

    # getter to display make and model
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


# ===============================
# 2. Create Objects (Instances)
# ===============================
my_car = Vehicle("Tesla", "Model 3")
snd_car = Vehicle("Toyota", "Yaris")

my_car.get_make_model()   # --> I'm a Tesla Model 3
my_car.moves()            # --> moves along

snd_car.get_make_model()  # --> I'm a Toyota Yaris
snd_car.moves()           # --> moves along


# ===============================
# 3. Inheritance (Child Classes)
# ===============================

# An airplane is a type of vehicle
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        # reuse the constructor from the parent Vehicle
        super().__init__(make, model)
        self.faa_id = faa_id  # specific property for airplanes

    # override the moves() method
    def moves(self):
        print("flies along")  # airplanes fly


# A truck is another type of vehicle
class Truck(Vehicle):
    def moves(self):
        print("rumbles along")  # trucks rumble


# A golf cart
class GolfCart(Vehicle):
    def moves(self):
        print("rolls slowly along")  # golf carts roll slowly


# ===============================
# 4. Polymorphism
# ===============================
# Create several objects of different classes
cessna = Airplane("Cessna", "B12", "B-123")
mack = Truck("Mack", "Pinnacle")
golfwagon = GolfCart("Yamaha", "GC11")

# With polymorphism, we can call the same method name "moves"
# but each object responds differently depending on its class
for v in (my_car, snd_car, cessna, golfwagon, mack):
    v.moves()
    v.get_make_model()
