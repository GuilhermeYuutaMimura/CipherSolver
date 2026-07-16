def main_menu():
    #* Funtion to display the main menu and handle user input, separeted by sections and handling invalid inputs
    while True: 
        print("""
        [1] Ciphers
        [2] Hashes
        [3] Encoding
        [0] Exit""")

        choice = None
        choice = input("")

        if choice == "1":
            from ciphers import ciphers_menu
            ciphers_menu()

        elif choice == "2":
            from hashes import hashes_menu
            hashes_menu()

        elif choice == "3":
            from encodes import encoding_menu
            encoding_menu()

        #todo fazer que o texto "Exiting..." adicione um ponto no final para simular um efeito de loading,
        #todo  e depois de 3 segundos feche o programa

        elif choice == "0":
            print("Exiting...")

            break
        
        else:
            print("Invalid choice")