
print("############### TO DO LIST #################")
print("1.START")
print("2.EXIT")

def main():
    while True:
        print("1. Addd Task")
        print("2. View Task")
        print("3. Remove Task")
        print("4. Exit program")
        user1 = int(input("Enter the Choices ! :  "))

        if user1 == 1:
            entertask = input("Add Task :  ")
            with open("file.txt" , "a") as f:
                entertask1 = f.write(entertask + "\n")
                print("Task Added ! ")

        elif user1 == 2:
            with open("file.txt" , "r") as f:
                entertask1 = f.read()
                print(entertask1)

        elif user1 == 3:
            removetask = input("Enter the task you want to remove  :  ")

            with open("file.txt" , "r") as f:
                entertask1 = f.readlines()

            if removetask + "\n" in entertask1:
                entertask1.remove(removetask + "\n")

                with open("file.txt" , "w") as f:
                    for task in entertask1:
                        f.write(task)

                print("Task Removed ! ")

            else:
                print("Task not found ! ")

        elif user1 == 4:
             print("Good bye have a nice day !")
             break

        else:
             print("enter a valid choi9ce ! ")


main()
