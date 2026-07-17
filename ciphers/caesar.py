from util.screen_cleaner import screen_cleaner

def caesar():
    screen_cleaner()
    choice = None
    
    while True:


        print("""
[1] Decrypt
[2] Encrypt
[0] Go Back""")
        
        print("")
        choice = input("Option: ")

        if choice == "2":
            screen_cleaner()

            text = str(input("Enter the text to decrypt: "))
            key = int(input("Enter the key (number of positions to shift): "))

            for char in text: #Iterate through each character, checks if its a letter and lowercase, gets the ascii value, 
                              # if the value + key is higher than 122, - 26 to return to a, else just prints
                if char.isalpha() and char.islower():
                    value = (ord(char))

                    if (value + key) > 122:
                        value = (value + key) - 26

                    else:
                        value = (value + key)
                    print(chr(value), end="") #end to avoid new line after each character

                elif char.isalpha() and char.isupper():
                    value = (ord(char))

                    if (value + key) > 90:
                        value = (value + key) - 26

                    else:
                        value = (value + key)
                    print(chr(value), end="")

                else:
                    print(char, end="") #print the text with the letters

        elif choice == "1":
            screen_cleaner()

            text = str(input("Enter the text to encrypt: "))
            key = int(input("Enter the key (number of positions to shift): "))

            for char in text:

                if char.isalpha() and char.isupper(): #Basicamente o contrário do encrypt quando menor que 65, adiciona 26 para voltar a Z, caso contrário apenas subtrai o key
                    value = ord(char)
                    
                    if (value - key) < 65:
                        value = (value - key) + 26

                    else:
                        value = (value - key)
                    print(chr(value), end="")

                elif char.isalpha() and char.islower():
                    value = ord(char)

                    if (value - key) < 97:
                        value = (value - key) + 26

                    else:
                        value = (value - key)
                    print(chr(value), end="")

                else:
                    print(char, end="")

        elif choice == "0":
            screen_cleaner()
            break
        
        else:
            screen_cleaner()
            print("Invalid choice")