class vehicles:
    def move(self):
        print("vehicles name")
class car(vehicles):
    def move(self):
        print("car moves on the road")
class boat(vehicles):
    def move(self):
        print("boat sails on the river")
v1=car()
v2=boat()
v1.move()
v2.move()
