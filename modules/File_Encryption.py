import os;

def file_encryption():

    print("-----------FILE ENCRYPTION---------")

    def generated_file():

        while True:
            file_name = input("Enter file Name: ")
            check = os.path.exists(file_name)

            if check:
            # print("File Exsits")
                break

            else:
                print("File not found. Try again")

        key = int(input("Enter key here: "))

        while True:
            mode = input("Enter mode Encryption/Decryption here: ").lower()
            if mode in ["encryption", "decryption"]:
                break
            else:
                print("I didn't understand. Please try again!")

        return file_name, key, mode
        

    file_name, key, mode = generated_file()

    file = open(file_name , "r")
    content = file.read()
    file.close()


    result = ""

    if mode == "decryption":
        key = -key

    for char in content:
        if char.isalpha():
            if char.isupper():
                position = ord(char) - ord("A")
                new_position = (position + key) % 26
                new_char = chr(new_position + ord("A"))
                result += new_char

            elif char.islower():
                position = ord(char) - ord("a")
                new_position = (position + key) % 26
                new_char = chr(new_position + ord("a"))
                result += new_char
        else:
            result += char

    new_file_name = "encrypted_" + file_name

    new_file = open(new_file_name, "w")
    new_file.write(result)
    new_file.close()