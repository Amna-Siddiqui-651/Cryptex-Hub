import os

def file_encryption():

    print("======================================")
    print("         FILE ENCRYPTION")
    print("======================================")

    def generated_file():

        while True:
            file_name = input("Enter file name (.txt): ")

            if not file_name.endswith(".txt"):
                print("Only .txt files are supported.")
                continue

            if os.path.exists(file_name):
                break
            else:
                print("File not found. Try again.")

        while True:
            try:
                key = int(input("Enter key here: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number.")

        while True:
            mode = input("Enter mode (Encryption/Decryption): ").lower()

            if mode in ["encryption", "decryption"]:
                break
            else:
                print("Invalid input! Please try again.")

        return file_name, key, mode

    file_name, key, mode = generated_file()

    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()

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

            else:
                position = ord(char) - ord("a")
                new_position = (position + key) % 26
                new_char = chr(new_position + ord("a"))
                result += new_char

        else:
            result += char

    if mode == "encryption":
        new_file_name = "encrypted_" + file_name
    else:
        new_file_name = "decrypted_" + file_name

    with open(new_file_name, "w", encoding="utf-8") as new_file:
        new_file.write(result)

    print(f"Output file: {new_file_name}")

    if mode == "encryption":
        print()
        print("--------------------------------------")
        print("Encryption completed successfully.")
    else:
        print()
        print("--------------------------------------")
        print("Decryption completed successfully.")

    print("--------------------------------------")