x = int(input("Enter 1st Number :"))
y = int(input("Enter 2st Number :"))

operator = input("Enter the operetor (+/-/*///):")
if operator == "+":
    print(f"Answer:{x+y}")
elif operator == "-":
    print(f"Answer:{x-y}")
elif operator == "*":
    print(f"Answer:x*y")
elif operator == "/":
    print(f"Answer:x/y")
else:
    print("Kya kar rahe ho , mazak hai ?")
input("\nPress Enter to exit...")