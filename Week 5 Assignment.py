# Base Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number):
        print(f"📞 Calling {number} from {self.model}...")

    def get_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage."

# Subclass (Inheritance)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, strap_type):
        super().__init__(brand, model, storage)  # Call the parent constructor
        self.strap_type = strap_type

    def track_fitness(self):
        print(f"🏃‍♂️ Tracking fitness on {self.model} smartwatch!")

    # Method Overriding (Polymorphism Example)
    def make_call(self, number):
        print(f"⌚ Making a call to {number} from smartwatch {self.model}!")

# Testing
phone = Smartphone("Apple", "iPhone 15", 256)
watch = Smartwatch("Samsung", "Galaxy Watch 6", 16, "Silicone")

print(phone.get_info())
phone.make_call("123-456-7890")

print(watch.get_info())
watch.make_call("987-654-3210")
watch.track_fitness()
