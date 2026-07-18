from util.screen_cleaner import screen_cleaner
import base64

def base64_menu():

    while True:
        screen_cleaner()
        print("Base64 encode")
        print("""
[1] Decode
[2] Encode
[0] Go Back""")
        print()
        choice = input("Option: ")

        if choice =="1":
            screen_cleaner()
            text = input("Enter text to decode: ")

            decoded_text = base64.b64decode(text)
            string_result = decoded_text.decode("utf-8")

            print(string_result)
        
        elif choice == "2":
            screen_cleaner()
            text = input("Enter text to encode: ")

            text_byte = text.encode("utf-8")
            string_result = base64.b64encode(text_byte)
            legible_string_result = string_result.decode("utf-8")

            print(legible_string_result)
        
        elif choice == "0":
            screen_cleaner
            break
        else:
            print("Invalid choice")
        print()
        input("Press enter to continue")
