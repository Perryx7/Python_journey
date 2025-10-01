"""
classes is like blueprints where we want to create something
inside a classw we create an objetct like a class vehicle

"""

class Vehicle :
    #define property
    def __init__(self,  make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("moves along" )

    #getter
    def get_make_model(self):
        print(f" i'm a {self.make} {self.model}.")

##object"
my_car = Vehicle('tesla', 'model 3')

#print(my_car.make)
#print(my_car.model)
my_car.get_make_model()
my_car.moves()

#create a new car
snd_car = Vehicle('toyota', 'Yaris')
snd_car.get_make_model()
snd_car.moves()


#heritance

class Airplane(Vehicle):
    def moves(self):
        print("flies along")

class Truck(Vehicle):
    def moves(self):
        print("rumbles along")

class GolfCart(Vehicle):
    def moves(self):
       pass

cessna = Airplane('cessna', 'boweing')
mack = Truck('Mack', 'pinnacle')
golfwagon = GolfCart('yamaha', 'GC11')

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()