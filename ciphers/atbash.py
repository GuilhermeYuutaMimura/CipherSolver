from util.screen_cleaner import screen_cleaner

def atbash():
    screen_cleaner()
    translation_table = None
    choise = None
    while True:
        print("""
[1] Decrypt
[2] Encrypt
[3] Go Back""")
        
        choise = input("Choose an option: ")

        if choise == "1":
            screen_cleaner()
            text = input("Enter the text to decrypt: ")

            translation_table = str.maketrans("abcdefghijklmnopqrstuvwxyz","zyxwvutsrqponmlkjihgfedcba" ) #table for lowercase
            text = text.translate(translation_table)

            translation_table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ","ZYXWVUTSRQPONMLKJIHGFEDCBA" ) #table for uppercase
            text = text.translate(translation_table)

            translation_table = str.maketrans("0123456789","9876543210" ) #table for numbers
            text = text.translate(translation_table)

            print("")
            print("Decrypted text: " + text)
        
        elif choise == "2":
            screen_cleaner()
            text = input("Enter the text to encrypt: ")

            translation_table = str.maketrans("abcdefghijklmnopqrstuvwxyz","zyxwvutsrqponmlkjihgfedcba" )
            text = text.translate(translation_table)

            translation_table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ","ZYXWVUTSRQPONMLKJIHGFEDCBA" )
            text = text.translate(translation_table)

            translation_table = str.maketrans("0123456789","9876543210" )
            text = text.translate(translation_table)
        
            print("")
            print("Encrypted text: " + text)

        else:
            screen_cleaner()
            break