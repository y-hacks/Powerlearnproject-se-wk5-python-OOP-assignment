# Class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Life: {self.battery_life} hours")

    def charge_phone(self):
        self.battery_life = 200
        print("The phone is now fully charged!")


# Create an object of Smartphone
my_phone = Smartphone("SAMSUNG", "SAMSUNG GALAXY S21 ULTRA", 85)

# Show details of the smartphone
my_phone.show_details()

# Charge the smartphone
my_phone.charge_phone()

# Show updated details after charging
my_phone.show_details()
