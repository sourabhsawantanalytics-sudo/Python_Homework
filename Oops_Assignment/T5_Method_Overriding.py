class Vehicle:          # class
    def start(self):
        print("Vehicle is starting")

   
class Car(Vehicle):     # class
    def start(self):    # Override
        print("Car is starting with a key")


class Bike(Vehicle):    # class
    def start(self):    # Override
        print("Bike is starting with a self start button")

class Truck(Vehicle):
    def start(self):
        print("Truck is stating with a self key")


car = Car()
bike = Bike()
truck = Truck()

car.start()
bike.start()
truck.start()
        