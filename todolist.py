print("############### TO DO LIST #################")
print("1.START")
print("2.EXIT")

def main():
    while True:
        print("1. Add Task")
        print("2. View Task")
        print("3. Remove Task")
        print("4. Exit program")
        user1 = int(input("Enter the Choices ! :  "))

        if user1 == 1:
            entertask = input("Add Task :  ")
            with open("file.txt" , "a") as f:
                entertask1 = f.write(entertask)
                print("Task Added ! ")

        elif user1 == 2:
            with open("file.txt" , "r") as f:
                entertask1 = f.read()
                print(entertask1)

        elif user1 == 3:
            with open("file.txt" , "a") as f:
                            entertask1 = f.open()

        elif user1 == 4:
             print("Good bye have a nice day !")
             break
        else :
             print("enter a valid choi9ce ! ")
             

main()

