print("############### EXPENSE TRECKER #################")



def main():
    while True:

        print("1. Add Expense")
        print("2. View Expense")
        print("3. Show Total")
        print("4. Exit")

        user1 = int(input("Enter the Choice: "))
        # step 1 to openen add expensese
        if user1 == 1:
            name1 = input("Enter The product : ")
            cost1 = int(input("Enter Cost : "))

            with open("expensefile.txt", "a") as f:
                f.write(name1 + "-" + str(cost1) + "\n")

            with open("costfile.txt", "a") as f:
                f.write(str(cost1) + "\n")

            print("EXPENSE ADDED ✅")
        #step2 to open ba;ace
        elif user1 == 2:
            with open("expensefile.txt", "r") as f:
                x = f.read()
                print(x)
        #show total 
        elif user1 == 3:
            total = 0

            with open("costfile.txt", "r") as f:
                for cost in f:
                    total = total + int(cost)

            print("Total Expense:", total)
        #exit program
        elif user1 == 4:
            print("PROGRAM EXITED ✅ !")
            break

        else:
            print("ENTER A VALID CHOICE!")


main()