print("IMPORTS DONE")

from modules.caesar_cipher import caesar_cipher;
from modules.file_encryption import file_encryption;
from modules.password_generator import password_generator;
from modules.spam_email_detector import spam_email_detector;

print("=====================================")
print("       WELCOME TO CRYPTEX-HUB       ")
print("======================================")

menu = input("Do you want Toolkit: ").lower()

if menu == "yes":

    while True:

        print("=================================================")
        print("__________CRYPTEX-HUB TOOLKIT IS HERE__________")
        print("1. Caesar Cipher")
        print("2. File Encryption") 
        print("3. Password generator")
        print("4. Spam Email Detector")
        print("5. Exit")
        print("=================================================")

        choice = input("Enter your requirement here: ").lower()

        if choice in ["1", "caesar cipher"]:
            caesar_cipher()

        elif choice in ["2", "file encryption"]:
            file_encryption()

        elif choice in ["3", "password generator"]:
            password_generator()
        
        elif choice in ["4", "spam email", "spam email detector"]:
            spam_email_detector()

        elif choice in ["5", "exit"]:
            print("Thankyou! for using Cryptex-Hub.")
            break

        else:
            print("I didn't understand!")

elif menu == "no":
    print("It's okay! Bye")
    exit()

else:
    print("Sorry! I didn't understand. Please! try again!")