import urllib.parse
from util.screen_cleaner import screen_cleaner

def url_encoding():
    
    while True:
        screen_cleaner()

        print("URL encode")
        print("""
[1] Decode
[2] Encode
[0] Go Back""")
        print()
        choice = input("Option: ")

        if choice == "1":
            screen_cleaner()
            text = input("Enter text to decode: ")
            decoded = urllib.parse.unquote(text)
            print(decoded)
        
        elif choice == "2":
            screen_cleaner()
            text = input("Enter text to encode: ")
            encoded = urllib.parse.quote(text)
            print(encoded)
        
        elif choice == "0":
            screen_cleaner()
            break
        else:
            print("Invalid choice")
        print()
        input("Press enter to continue")


