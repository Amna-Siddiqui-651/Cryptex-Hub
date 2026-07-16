import os;

def spam_email_detector():

    print("-----------SPAM EMAIL DETECTOR---------")

    spam_words = [
        "free",
        "winner",
        "won",
        "prize",
        "cash",
        "money",
        "urgent",
        "limited",
        "offer",
        "discount",
        "click",
        "buy",
        "bonus",
        "claim",
        "gift",
        "congratulations",
        "selected",
        "lottery",
        "guaranteed",
        "earn",
        "income",
        "investment",
        "credit",
        "loan",
        "casino",
        "bitcoin",
        "crypto",
        "cheap",
        "deal",
        "exclusive",
        "risk-free",
        "act now",
        "subscribe",
        "promotion",
        "win",
        "reward",
        "voucher",
        "coupon",
        "limited time",
        "verify",
        "account",
        "password",
        "bank",
        "payment",
        "refund",
        "invoice"
    ]

    def file_check():

        print("======================================")
        print("         CAESAR CIPHER")
        print("======================================")

        while True:

            file_name = input("Enter file name(only TXT): ")
            check = os.path.exists(file_name)

            if check:
                break
            else:
                print("File didn't exixts! Please try again.")

        return file_name

    text = input ("Do you want FILE or TEXT: ").lower()

    if text == "file":
        
        file_name = file_check()

        with open(file_name , "r" ) as file:
            content = file.read()
            content = content.lower().split()

        count = 0

        for word in content:
            if word in spam_words:
                count += 1

        if count >= 3:
            print("SPAM EMAIL!")
        else:
            print("CONGRATULATIONS! EMAIL IS SAFE.")

    elif text in ["text", "text message"]:
        input_text = input("Input text here: ").lower().split()
        count = 0
        for i in input_text:
            if i in spam_words:
                count += 1
        if count >= 3:
            print("SPAM EMAIL!")
        else:
            print("CONGRATULATIONS! EMAIL IS SAFE.")
            print()
            print("--------------------------------------")
            print("Operation completed successfully.")
            print("--------------------------------------")   

    else:
        print("I didn't understand!")
            
     