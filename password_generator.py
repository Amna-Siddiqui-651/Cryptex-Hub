import random;

print("------PASSWORD GENERATOR-------")
while True:
    try:
        length = int(input("Enter password length here: "))
        break
    except:
        print("Password length should be an integer!")

UP_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LP_set = "abcdefghijklmnopqrstuvwxyz"
SY_set = "~!@#$%^&*()_+{|:=;<>}?`-[]',./"
NUM_set = "0123456789"

def get_choice(text):
    while True:
        ans = input(text).lower()
        if ans in ["yes","no"]:
            return ans
        print("I didn't understand")


UP = get_choice("Do you want uppercase: ")
LP = get_choice("Do you want lowercase: ")
SY = get_choice("Do you want symbol: ")
NUM = get_choice("Do you want number: ")

final_pool = []
if UP == "yes":
    final_pool.extend(UP_set)
if LP=="yes":
    final_pool.extend(LP_set)
if SY=="yes":
    final_pool.extend(SY_set)
if NUM =="yes":
    final_pool.extend(NUM_set)

if final_pool == []:
    ask = input("You haven't selected any character set!" \
    "Do you want by default password?: ").lower()
    password = ""
    if ask == "yes":
        final_pool = LP_set
        for i in range(length):
            password += random.choice(final_pool)
        print(f"Password is here: {password}")
    else:
        pass 

else:
    password = []
    for char in range(length):
        password.append(random.choice(final_pool))
    random.shuffle(password)
    final_password = "".join(password)
    print(f"Password is here: {final_password}")
    print("----------------------------------")

