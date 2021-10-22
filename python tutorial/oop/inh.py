class Vehicle:
    def general_use(self):
        print("Transportation")


class Car(Vehicle):
    def __init__(self):
        print("I am car")
        self.wheels = 4
        self.has_roofs = True

    def specific_use(self):
        self.general_use()
        print("Commute to work")


class MotorCycle(Vehicle):
    def __init__(self):
        print("I am motorcycle")
        self.wheels = 2
        self.has_roofs = False

    def specific_use(self):
        print("Long drive")


c = Car()

c.specific_use()

m = MotorCycle()
m.general_use()
m.specific_use()

print(isinstance(c, Car))
print(isinstance(m, Car))

print(issubclass(Vehicle, Car))
print(issubclass(Car, Vehicle))
