from ciphers.kbcipher import kbcipher
from ciphers.atbash import atbash
from ciphers.caesar import caesar
from ciphers.morse import morse
from ciphers.rail_fence import rail_fence
from ciphers.vigenere import vigenere
from ciphers.xor import xor
from util.screen_cleaner import screen_cleaner

def ciphers_menu():
    choice = None
    screen_cleaner()
    while True: 

        print("""
[1] Atbash Cipher
[2] Caesar Cipher
[3] Keyboard Cipher
[4] Morse Cipher
[5] Vigenere Cipher
[0] Go Back""")

        print("")
        choice = input("Option: ")

        if choice == "1":
            atbash()

        elif choice == "2":
            caesar()
        
        elif choice == "3":
            kbcipher()

        elif choice == "4":
            morse()

        #elif choice == "5":
            #rail_fence()

        elif choice == "5":
            vigenere()

        #elif choice == "8":
            #xor()
        
        elif choice == "0":
            break

        else:
            print("Invalid choice")
        