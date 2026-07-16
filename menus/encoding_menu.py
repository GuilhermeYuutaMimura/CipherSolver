from encodes.ascii import ascii
from encodes.base64 import base64
from encodes.binary import binary
from encodes.hexadecimal import hexadecimal
from encodes.rot13 import rot13
from encodes.url_encoding import url_encoding
from util.screen_cleaner import screen_cleaner

def encoding_menu():
    screen_cleaner()
    while True:
        choice = None

        print("""
[1] Base64
[2] Binary
[3] Hexadecimal
[4] Rot13
[5] URL Encoding
[0] Back""")
        print("")
        choice = input("Option: ")

        if choice == "1":
            base64()

        elif choice == "2":
            binary()

        elif choice == "3":
            hexadecimal()

        elif choice == "4":
            from encodes.rot13 import rot13_menu
            rot13_menu()

        elif choice == "5":
            url_encoding()
            
        elif choice == "0":
            break

        else:
            print("Invalid choice")