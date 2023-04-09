class Wheel:
    def __init__(self, size):
        self.size = size
class Engine:
    def __init__(self, power):
        self.power = power
class Car:
    def __init__(self, wheels, engine):
        self.wheels = wheels
        self.engine = engine
wheel1 = Wheel(29)
wheel2 = Wheel(29)
wheel3 = Wheel(29)
wheel4 = Wheel(29)
engine = Engine(150)
car = Car([wheel1, wheel2, wheel3, wheel4], engine)
print(car.wheels[0].size) # output: 29