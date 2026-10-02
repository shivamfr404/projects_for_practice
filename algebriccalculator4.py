def add(a,b):
    print("The sum of Number is : " ,a+b)
def sub(a,b):
    print("The diffrence of numbers is : " , a-b)
def multiply(a,b):
    print("The product of numbers is" , a*b)
def divison(a,b):
    print(" The division of number is : " , a/b)
def modulus(a):
    pass
def square(a):
    print("The square of number is : " , a*a)

print("--------------------------")
print("MENU :                   -") 
print("--------------------------")

print("1. Additon               -")
print("--------------------------")

print("2. Subtraction           -")
print("--------------------------")

print("3. Multiplication        -")
print("--------------------------")

print("4. Divison               -")
print("--------------------------")

print("5. Modulus               -")
print("--------------------------")

print("6. Square                 -")

print("--------------------------")
print("                          ")
print("                          ")
print("                          ")


user_input = int(input("ENTER : 1/2/3/4/5/6   :   "))


if user_input == 1:
    num1 = int(input("Enter 1st NUmber : "))
    num2 = int(input("Enter 2nd NUmber : "))

    add(num1,num2)

elif user_input == 2:
     num1 = int(input("Enter 1st NUmber : "))
     num2 = int(input("Enter 2nd NUmber : "))
    
     sub(num1,num2)

if user_input == 3:
     num1 = int(input("Enter 1st NUmber : "))
     num2 = int(input("Enter 2nd NUmber : "))
        
     multiply(num1,num2)

if user_input == 4:
     num1 = int(input("Enter 1st NUmber : "))
     num2 = int(input("Enter 2nd NUmber : "))
     divison(num1,num2)

if user_input == 5:
    modulus(num1,num2)

if user_input == 6:
     num1 = int(input("Enter 1st NUmber : "))
    
     square(num1)


