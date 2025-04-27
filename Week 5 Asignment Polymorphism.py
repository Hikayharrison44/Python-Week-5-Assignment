class Car:
    def move(self):
        print("🚗 The car is driving.")

class Plane:
    def move(self):
        print("✈️ The plane is flying.")

class Boat:
    def move(self):
        print("🚢 The boat is sailing.")

# Polymorphism in action
def start_journey(vehicle):
    vehicle.move()

# Testing
car = Car()
plane = Plane()
boat = Boat()

start_journey(car)
start_journey(plane)
start_journey(boat)
