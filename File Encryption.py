import os;

print("-----------FILE ENCRYPTION---------")

def generated_file():

    while True:
        file = input("Enter file Name: ")
        check = os.path.exists(file)

        if check == True:
            print("File Exsits")
            break

        else:
            print("File not found. Try again")


