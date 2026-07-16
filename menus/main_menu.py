from turtle import clear
from menus.ciphers_menu import ciphers_menu
from menus.hashes_menu import hashes_menu
from menus.encoding_menu import encoding_menu
from util.logo import logo
from util.screen_cleaner import screen_cleaner
#Importing all the menus so that they can be called from the main menu

def main_menu():
    #* Funtion to display the main menu and handle user input, separeted by sections and handling invalid inputs
    while True: 
        screen_cleaner()
        logo()
        print("""
[1] Ciphers
[2] Hashes
[3] Encoding
[0] Exit""")

        choice = None
        print("")
        choice = input("Option: ")

        if choice == "1":
            ciphers_menu()

        elif choice == "2":
            hashes_menu()

        elif choice == "3":
            encoding_menu()

        #todo fazer que o texto "Exiting..." adicione um ponto no final para simular um efeito de loading,
        #todo  e depois de 3 segundos feche o programa

        elif choice == "0":
            print("Exiting...")

            break
        
        else:
            print("Invalid choice")