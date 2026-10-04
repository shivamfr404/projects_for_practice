

print("                            ")
print("                            ")
print("                            ")

print("============================")
print("        PYTHON QUIZ")
print("============================")

print("                            ")
print("                            ")
print("                            ")





def quiz():
    score = 0

    name = input("Enter your Name : ")
    age = int(input("Enter your age : "))

    #que 1
    print("Q1. Which keyword is used to create a function? ")
    print("                                                ")
    print("1. function")
    print("2. def")
    print("3. func")
    print("4. create")

    x = int(input("Enter : 1/2/3/4 :  "))
    if x == 2:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! ")
    

    #que2
    print("============================")

    print("Q2.Which data type stores multiple values in order? ")
    print("                                                ")
    print("1. List")
    print("2. Integer")
    print("3. Bollean")
    print("4. Float")
    
    x = int(input("Enter : 1/2/3/4 :   "))
    if x == 1:
            print("✅ Correct!")
            score += 1
    else:
        print("❌ Wrong! ")


    print("============================")

#que 3
    print("Q3.What does len() do? ")
    print("                                                ")
    print("1. Delete somehting")
    print("2. Returns value / number of items")
    print("3. converts into integer")
    print("4. create a list")

    x = int(input("Enter : 1/2/3/4 :   "))
    if x == 2:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! ")

    #que4
    print("============================")

    print("Q4.Which symbol is used for comments?? ")
    print("                                                ")
    print("1. //")
    print("2. /*")
    print("3. #")
    print("4. --")
    
    x = int(input("Enter : 1/2/3/4 :   "))
    if x == 3:
            print("✅ Correct!")
            score += 1
    else:
        print("❌ Wrong! ")


    print("============================")

#que 5

    print("Q5.Which loop is commonly used when you want to repeat something while a condition remains true? ")
    print("                                                ")
    print("1. if")
    print("2. while")
    print("3. def")
    print("4. import")
    
    x = int(input("Enter : 1/2/3/4 :   "))
    if x == 2:
            print("✅ Correct!")
            score += 1
    else:
        print("❌ Wrong! ")

    c = (score / 5)*100
#final result. good wala
    print("============================================================")
    if score >= 4:
        print("                  ⭐ FINAL SCORE"                           )
        print(f"{name} is a topper ! he scored {score}/5 and he has {c} ")
    print("============================================================")
    if score > 2 and score < 4:
        print("                  ⭐ FINAL SCORE"                           )
        print(f"{name} score is decent ! he scored{score}/5 and he has {c} ")
    print("============================================================")
    if  score <3 :
            print("                  ⭐ FINAL SCORE"                           )
            print(f"{name} is Chutiya ! he scored{score}/5 and he has {c} ")
        


option1 = input("Enter : (Start/Exit) ").strip().lower()
if option1 == "start":

    quiz()
elif option1 == "exit":
    print("Good bye 👋, have a nice Day ")

else:
    print("❌ Invalid choice ❌")






#final scerrrnvmnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnnnvnvnvnvnvnvnnvnvnnvnvnvnvnvnvnnvnvvnnvnvvnvnvnvnnvnnn



