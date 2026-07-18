import hashlib
from util.screen_cleaner import screen_cleaner

def blake2b():

    while True:
        print("Blake2B Hash")
        print("""
[1]Generate Hash
[0] Go Back""")
        print()
        choice = input("Option: ")

        if choice == "1":
            screen_cleaner()
            text = input("Enter text to encode: ")
            text_byte = text.encode("utf-8")
            text_hash = hashlib.blake2b(text_byte)
            encoded = text_hash.hexdigest()

            print(encoded)
        
        elif choice == "0":
            screen_cleaner()
            break

        else:
            print("Invalid choice")
        print()
        input("Press enter to continue")
        screen_cleaner()