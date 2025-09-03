
# Assignment 1: Design Your Own Class 

# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

# Derived class (inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.battery = battery
    
    # Method to simulate calling someone
    def call(self, contact):
        print(f"Calling {contact}... 📞")
    
    # Method to simulate charging the phone
    def charge(self, amount):
        self.battery += amount
        print(f"Battery charged. Current battery: {self.battery}%")

# Create objects with unique values
phone1 = Smartphone("Apple", "iPhone 14", "128GB", 50)
phone2 = Smartphone("Samsung", "Galaxy S22", "256GB", 75)

print("=== Question 1 Output ===")
print(phone1.info())
phone1.call("Brian")
phone1.charge(20)

print(phone2.info())
phone2.call("Alice")
phone2.charge(10)



# Assignment 2: Polymorphism Challenge 

# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

# Car class
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Bike class
class Bike(Vehicle):
    def move(self):
        print("Riding 🚴")

print("\n=== Question 2 Output ===")
# List of vehicles demonstrating polymorphism
vehicles = [Car(), Plane(), Bike()]

for v in vehicles:
    v.move()  # Each class has its own move() version
