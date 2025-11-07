# Program # 2: Car Class
# Write a class named Car that has the following data attributes:

# __year_model (for the car's year model)
# __make (for the make of the car)
# __speed (for the car's current speed)
# The Car class should have an __init__ method that accepts the car's year model and make as arguments.
# These values should be assigned to the object's __year_model and __make data attributes.
# It should also assign 0 to the __speed data attribute.

# The class should also have the following methods:

# The accelerate method should add 5 to the speed data attribute each time it it called.
# The brake method should subtract 5 from the speed data attribute each time it is called.
# The get_speed method should return the current speed.
# Next, design a program that creates a Car object then calls the accelerate method five times.
# After each call to the accelerate method, g
# et the current speed of the car and display it.
# The call the brake method.  After each call to the brake method,
# get the current speed of the car and display it.

class Car:
    def __init__(self, make, year_model, speed):
        self.year_model = year_model
        self.make = make
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed

def main():
    my_car = Car('Dodge', '2011 Durango', 70)
    print(f'Staring speed = {my_car.get_speed()} mph.')
    count = 1
    while count < 6:
        my_car.accelerate()
        print(f'Acceleration #{count}: speed = {my_car.get_speed()} mph.')
        count += 1
    while count >= 6 and count < 11:
        my_car.brake()
        print(f'Deceleration #{count - 5}: speed = {my_car.get_speed()} mph.')
        count += 1

main()


#This program was written on 11/6/25 by Logan Gibson
#Its name is "Inaccurate Speedometer"