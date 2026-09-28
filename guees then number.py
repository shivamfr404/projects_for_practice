import random
intan = random.randint(1,100)
guess = int(input("Guess the number between 1 and 100:"))
while guess != intan:
    if intan < guess:
        print("to high!")
    elif intan > guess:
        print("to low!")
    guess = int(input("Guess the number between 1 and 100:"))

print("you guessed the number congratiulations!!")
