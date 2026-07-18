from util.screen_cleaner import screen_cleaner
import codecs

def rot13 ():
    choice = None

    while True:
        screen_cleaner()

        print("Rot13 encode")
        print("""
[1] Decode
[2] Encode
[0] Go Back""")
        print()
        choice = input("Option: ")

        if choice == "1":
            screen_cleaner()
            text = input("Enter text to decode: ")
            encoded = codecs.encode(text, "rot_13")
            print(encoded)
        
        elif choice == "2":
            screen_cleaner()
            text = input("Enter text do encode: ")
            decoded = codecs.decode(text,"rot_13")
            print(decoded)
        
        elif choice == "0":
            screen_cleaner()
            break
        else:
            print("Invalid choice")
        print()
        input("Press enter to continue")