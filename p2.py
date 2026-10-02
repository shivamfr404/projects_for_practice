import random

integer = random.randint(1,10)

while True:
    user = int(input("Guess the number : "))
    if user > 10 or user < 0 :
        print("Enter the number between 1 to 10")

    elif user > integer :
        print("Too high!")

    elif user < integer:
        print("Too low!")

    

    else:
        print("Correct!")
        break
