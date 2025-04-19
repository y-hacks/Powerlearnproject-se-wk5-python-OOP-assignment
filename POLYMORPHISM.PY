# Class representing a Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement the 'move' method")


# Class representing a Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


# Class representing a Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")
        

# Create objects of Car and Plane
my_car = Car()
my_plane = Plane()

# Call the move method on both
my_car.move()  # Should print: Driving 🚗
my_plane.move()  # Should print: Flying ✈️
