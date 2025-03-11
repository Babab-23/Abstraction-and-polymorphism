class BMW:
    def __init__(self, model, horsepower):
        self.model = model
        self.horsepower = horsepower
    
    def start(self):
        return f"BMW {self.model} is starting with {self.horsepower} HP."
    
    def accelerate(self):
        return f"BMW {self.model} is accelerating swiftly."
    
    def stop(self):
        return f"BMW {self.model} has stopped."


class Ferrari:
    def __init__(self, model, horsepower):
        self.model = model
        self.horsepower = horsepower
    
    def start(self):
        return f"Ferrari {self.model} is roaring to life with {self.horsepower} HP."
    
    def accelerate(self):
        return f"Ferrari {self.model} is speeding up rapidly."
    
    def stop(self):
        return f"Ferrari {self.model} has come to a halt."


def test_car(car):
    print(car.start())
    print(car.accelerate())
    print(car.stop())


# Creating instances of BMW and Ferrari
bmw_car = BMW("M4", 503)
ferrari_car = Ferrari("488 Pista", 711)

# Demonstrating polymorphism
test_car(bmw_car)
print()
test_car(ferrari_car)
