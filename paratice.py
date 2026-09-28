x = input("Enter the Model name of your Car: ")
y = int(input("Enter year: "))
z = input("Enter the color: ")

class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

car1 = Car(x, y, z)

with open("car.txt", "a") as f:
    f.write(f"Model: {car1.model}, Year: {car1.year}, Color: {car1.color}\n")