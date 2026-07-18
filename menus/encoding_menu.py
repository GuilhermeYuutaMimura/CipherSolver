from encodes.ascii import ascii
from encodes.base64 import base64, base64_menu
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
[1] Ascii
[2] Base64
[3] Binary
[4] Hexadecimal
[5] Rot13
[6] URL Encoding
[0] Back""")
        print("")
        choice = input("Option: ")
        if choice == "1":
            ascii()

        if choice == "2":
            base64_menu()

        elif choice == "3":
            binary()

        elif choice == "4":
            hexadecimal()

        elif choice == "5":
            rot13()

        elif choice == "6":
            url_encoding()
            
        elif choice == "0":
            break

        else:
            print("Invalid choice")