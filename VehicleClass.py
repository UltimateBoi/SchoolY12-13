class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return("The vehicle has started.")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def openBoot(self):
        return("Boot opened.")


class Truck(Vehicle):
    def __init__(self, make, model, year, bedSize):
        super().__init__(make, model, year)
        self.bedSize = bedSize

    def tow(self, weight):
        return(f"Towing {weight} lbs of weight.")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engineCapacity):
        super().__init__(make, model, year)
        self.engineCapacity = engineCapacity

    def wheelie(self):
        return("Performing a wheelie.")