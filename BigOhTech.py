class Person:
    def __init__(self, name, vehicles, v1, v2):
        self.name = name
        self.vehicles = vehicles
        self.v1 = v1
        self.v2 = v2

    def print_details(self):
        print(f'{self.name} has {self.vehicles} vehicles, one is {self.v1} and other is {self.v2}.')

        
class Vehicle:
    def __init__(self, vname, fuel, use, madeIn):
        self.vname = vname
        self.fuel = fuel
        self.use = use
        self.madeIn = madeIn
    
    def print_details(self):
        print(f'{self.vname} use {self.fuel} as fuel.It is {self.use} vehicle and is {self.madeIn}.')


p = Person("Sourabh", 'two','Honda Accord Car','Ducati Bike')
v1 = Vehicle('Honda Accord Car','diesel','new','made in India')
v2 = Vehicle("Ducati Bike",'petrol','used','imported')
p.print_details()
v1.print_details()
v2.print_details()
