class vehicles:
    def move(self):
        print("vehicles moves")
class car(vehicles):
    def drive(self):
        print("cars to make a drive")
class bike(vehicles):
    def ride(self):
        print("bikes to ride")
c=car()
c.move()
c.drive()
b=bike()
b.move()
b.ride

