class Vehical1:
    def max_speed(self,mspeed):
        self.mspeed = mspeed
    def Milage (self,milage):
        self.milage = milage
    def show_max_speed(self):
        print(self.mspeed)
    def show_milage(self):
        print(self.milage)

v1 = Vehical1()
v1.max_speed(1000)
v1.Milage(50)
v1.show_max_speed()
v1.show_milage()


class Vehical2:

    def __init__(self,maxspeed,milage):
        self.maxspeed = maxspeed
        self.milage = milage
    def show(self):
        print(self.maxspeed)
        print(self.milage)

v2 = Vehical2(1000,60)
v3 = Vehical2(500,30)
v2.show()
v3.show()

