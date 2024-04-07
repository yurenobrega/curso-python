from abc import ABC

class Vehicle(ABC):
    @classmethod
    def go(self):
        pass
    
    @classmethod
    def stop(self):
        pass

class Car(Vehicle):
    
    def go(self):
        print("You drive the car")
        
    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    
    def go(self):
        print("You ride the motorcycle")
        
    def stop(self):
        print("This motorcycle is stopped")

# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()