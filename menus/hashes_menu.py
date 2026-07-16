from hashes.blake2b import blake2b
from hashes.md5 import md5
from hashes.sha_256 import sha_256
from hashes.sha_512 import sha_512
from util.screen_cleaner import screen_cleaner

def hashes_menu():
    screen_cleaner()
    #* Funtion to display the hashes menu and handle user input, separeted by sections and handling invalid inputs
    while True: 
        print("""
[1] Blake2
[2] MD5
[3] SHA-256
[4] SHA-512
[0] Back""")

        choice = None
        print("")
        choice = input("Option: ")

        if choice == "1":
            blake2b()

        elif choice == "2":
            md5()

        elif choice == "3":
            sha_256()

        elif choice == "4":
            sha_512()

        elif choice == "0":
            break
            
        else:
            print("Invalid choice")