import random
code = ["p","r","s"]
x = input("Enter (r/p/s):")
if x in code :
    comp = random.choice(code)
    print(f"computer has taken {comp}")

else:
    print("invalid choice")

