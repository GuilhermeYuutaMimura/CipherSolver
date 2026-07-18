from util.screen_cleaner import screen_cleaner

def kbcipher():
    translation_table = None
    choice = None
    while True:
        screen_cleaner()
        print("Keyboard Cipher")
        print("""
[1] Decrypt
[2] Encrypt
[0] Exit""")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            screen_cleaner()
            text = input ("Enter the text to decrypt: ")

            translation_table = str.maketrans("qwertyuiopasdfghjklzxcvbnm","abcdefghijklmnopqrstuvwxyz" )
            text = text.translate(translation_table)
            translation_table = str.maketrans("QWERTYUIOPASDFGHJKLZXCVBNM","ABCDEFGHIJKLMNOPQRSTUVWXYZ" )
            text = text.translate(translation_table)

            print("")
            print("Decrypted text: " + text)
            print()

        elif choice == "2":
            screen_cleaner()
            text = input ("Enter the text to encrypt: ")

            translation_table = str.maketrans("abcdefghijklmnopqrstuvwxyz","qwertyuiopasdfghjklzxcvbnm" )
            text = text.translate(translation_table)
            translation_table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ","QWERTYUIOPASDFGHJKLZXCVBNM" )
            text = text.translate(translation_table)

            print("")
            print("Encrypted text: " + text)
            print()
        
        elif choice == "0":
            screen_cleaner()
            break
        else:
            screen_cleaner()
            break
        print()
        input("Press enter to continue")
