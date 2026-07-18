from random import choice

from util.screen_cleaner import screen_cleaner
def binary():
    text_values = []
    while True:
        screen_cleaner()

        print("Binary encode")
        print("""
[1] Decode
[2] Encode
[0] Go Back""")
        print()
        choice = input("Option: ")

        if choice == "1":
            screen_cleaner()
            text = input("Enter text to decode: ")

            for i in text.split():#Splits the text in blocks of binary
                text_values.append(int(i, 2)) #Since binary is base 2, after this is trasnlate do an ascii value
            
            for j in text_values:
                print(chr(j), end="")

        elif choice == "2":
            screen_cleaner()
            text = input("Enter text to encode: ")

            for i in text:
                text_values = ord(i) #intinarate all the letters and takes the ascii
                binary_values = bin(text_values)[2:] #After bin transforms the ascii number in to binary and removes the fist 2 letters (2b[which indicates its a binary])
                print(binary_values, end = " ")
        
        elif choice == "0":
            screen_cleaner()
            break
        
        else:
            print("Invalid choice")
            print()
            input("Press enter to continue")
            
