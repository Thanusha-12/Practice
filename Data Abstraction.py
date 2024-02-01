from abc import ABC, abstractmethod
# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    # Create abstract method
    @abstractmethod
    def printDetails(self):
        pass
    # Create concrete method
    def accelerate(self):
        print("speed up ...")
    def break_applied(self):
        print("Car stop")
# Create a child class
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand);
        print("Model:", self.model);
        print("Year:", self.year);
    def Sunroof(self):
        print("Not having this feature")
# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand);
        print("Model:", self.model);
        print("Year:", self.year);
    def Sunroof(self):
        print("Available")
car1 = Hatchback("Maruti", "Alto", "2022");
car1.printDetails()
car1.accelerate()


from abc import ABC,abstractmethod
class maths(ABC):
    pass
class square(maths):
    length=3
    def Area(self):
        return self.length * self.length
class circle(maths):
    radius=5
    def Area(self):
        return 3.14 * self.radius * self.radius

sq=square()
ci=circle()
print("Area of square",sq.Area())
print("Area of circle",ci.Area())
