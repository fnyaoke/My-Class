# Smartphone class with inheritance example

class Device:
    """Base class for devices"""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


class Smartphone(Device):  # Inherits from Device
    def __init__(self, brand, model, storage, battery_life):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.battery_life = battery_life

    def make_call(self, number):
        print(f" Calling {number} from {self.info()}")

    def charge(self):
        print(f" Charging {self.info()}... Battery life: {self.battery_life} hours")

    def __str__(self):
        return f"{self.info()} with {self.storage}GB storage and {self.battery_life}h battery life"


# Create Smartphone objects
phone1 = Smartphone("Apple", "iPhone 15", 256, 20)
phone2 = Smartphone("Samsung", "Galaxy S24", 512, 25)

print(phone1)
phone1.make_call("123-456-789")
phone2.charge()

# Polymorphism with vehicles

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement move()")


class Car(Vehicle):
    def move(self):
        print("Driving on the road")


class Plane(Vehicle):
    def move(self):
        print("Flying in the sky")


class Boat(Vehicle):
    def move(self):
        print("Sailing on the water")


# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()