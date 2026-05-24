import random;

length = int(input("Enter password length here: "))
UP = input("Do you want uppercase: ").lower()
LP = input("Do you want lowercase: ").lower()
SY = input("Do you want symbols: ").lower()
NUM = input("Do you want numbers: ").lower()

UP_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LP_set = "abcdefghijklmnopqrstuvwxyz"
SY_set = "~!@#$%^&*()_+{|:=;<>}?`-[]',./"
NUM_set = "0123456789"

final_pool = ""

if UP=="yes":
    final_pool += UP_set
if LP=="yes":
    final_pool += LP_set
if SY=="yes":
    final_pool += SY_set
if NUM =="yes":
    final_pool += NUM_set

if final_pool == "":
    ask = input("You haven't selected any character set!" \
    "Do you want by default password?: ").lower()
    password = " "
    if ask == "yes":
        final_pool = LP_set
        for i in range(length):
            password += random.choice(final_pool)
        print(password)
    else:
        pass 

else:
    password = " "
    for char in range(length):
        password += random.choice(final_pool)
    print(password)
