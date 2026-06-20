print("------------CAESAR CIPHER------------------")

def generated_text():

    text = input("Enter text here: ")

    while True:
        try:
            shift_value = input("Enter shift value here: ")
            key = int(shift_value)
            
            break
        except:
            print("Invalid input! Please number here. ")

    while True:
        mode = input("Enter mode here(Encryption/Decryption): ").lower()
        if mode in ["encryption", "decryption"]:
            break 
        else:
            print("Invalid input. Please try again!")

    return text, key, mode

text, key, mode = generated_text()

result =  " "

for char in text:
    if char.isalpha():
        if char.isupper():
            position = ord(char) - ord("A")
            new_position = (position + key) % 26
            new_char = new_position + ord("A")
            result+=new_char

        else:
            position = ord(char) - ord("a")
            new_position = (position + key) % 26
            new_char = new_position + char("a")
            result+=new_char
        




