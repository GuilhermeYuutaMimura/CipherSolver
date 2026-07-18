from util.screen_cleaner import screen_cleaner
def ascii():
    choice = None
    ascii_values = []

    while True:
        screen_cleaner()

        print("Ascii encode")
        print("""
[1] Decode
[2] Encode
[0] Go Back""")
        print()
        choice = input("Option: ")

        if choice == "1":
            screen_cleaner()
            text = input("Enter text to decode: ")

            for i in text.split(): #Transform a single string into separeted numbers
                ascii_values.append(int(i)) #Put all of them inside a list and transforming in ints
            
            for j in ascii_values:
                print (chr(j),end="")
        
        elif choice == "2":
            screen_cleaner()
            text = input("Enter text to encode: ")

            for i in text:
                print(ord(i), end= " ")

        elif choice == "0":
            screen_cleaner
            break
        
        else:
            print("Invalid choice")
        print()
        input("Press enter to continue")