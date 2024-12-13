class Car:
    total = 0
    def __init__(self, brand, model, type):
        self.__brand = brand
        self.__model = model
        self.__type = type
        Car.total += 1

    def __str__(self):
        return f"{self.__brand} {self.__model} of type {self.__type}"

class ElectricCar(Car):
    def __init__(self, brand, model, type, battery):
        super().__init__(brand, model, type)
        self.battery = battery

    def __str__(self):
        return f"electric"


print(ElectricCar("Telsa", "S", "idk", "85"))
print(ElectricCar.total)
