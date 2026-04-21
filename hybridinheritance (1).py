class animals:
    def make_sound(self):
        print("animals make sound")
class mammals(animals):
    def do_sound(self):
        print("mammals are doing the sound")
class cat(animals):
    def sound(self):
        print("cats are doing the sound")
class bat(mammals,cat):
    pass
b=bat()
b.mammals()
b.cat()
