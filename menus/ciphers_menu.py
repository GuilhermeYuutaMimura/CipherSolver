from ciphers.atbash import atbash
from ciphers.caesar import caesar
from ciphers.kbshift import kbshift
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
[3] Vigenere Cipher
[4] Keyboard Shift Cipher
[5] Morse Cipher
[6] Rail Fence Cipher
[7] Vigenere Cipher
[8] Xor Cipher
[0] Go Back""")

        print("")
        choice = input("Option: ")

        if choice == "1":
            atbash()

        elif choice == "2":
            caesar()
        
        elif choice == "3":
            vigenere()
        
        elif choice == "4":
            kbshift()

        elif choice == "5":
            morse()

        elif choice == "6":
            rail_fence()

        elif choice == "7":
            vigenere()

        elif choice == "8":
            xor()
        
        elif choice == "0":
            break

        else:
            print("Invalid choice")
        