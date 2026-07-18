from util.screen_cleaner import screen_cleaner
def hexadecimal():
    text_values = []
    while True:
        screen_cleaner()

        print("Hexadecimal encode")
        print("""
[1] Decode
[2] Encode
[0] Go Back""")
        print()
        choice = input("Option: ")

        if choice == "1":
            screen_cleaner()
            text = input("Enter text to decode: ")

            for i in text.split():
                text_values.append(int(i, 16))
            
            for j in text_values:
                print(chr(j), end="")

        elif choice == "2":
            screen_cleaner()
            text = input("Enter text to encode: ")

            for i in text:
                text_values = ord(i) 
                hex_value = hex(text_values)[2:] 
                print(hex_value, end = " ")
        
        elif choice == "0":
            screen_cleaner()
            break
        
        else:
            print("Invalid choice")
            print()
            input("Press enter to continue")
            
#same code as binary, 2 lines changes