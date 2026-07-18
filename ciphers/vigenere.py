from util.screen_cleaner import screen_cleaner
#stupid identation 
def vigenere():
    translation_text = None
    choice = None
    key_total = 0 #counts the total number the key got itinarated
    key_index = 0 #counts the actual index

    while True:
        screen_cleaner()
        print("Vigenere")
        print("""
[1] Decrypt
[2] Encrypt
[0] Go Back
""")

        choice = input("Option: ")

        if choice == "1":
            screen_cleaner()

            text = input("Enter the text to decrypt: ")
            key = input("Enter the key: ")

            key_total = 0  # Counts how many letters of the text already used the key

            for char in text:

                if char.isalpha() and char.isupper():

                    value = ord(char)

                    key_index = key_total % len(key)
                    # Uses the current index, total key counter and key size to find
                    # which letter from the keyword will encrypt/decrypt the current letter

                    key_char = key[key_index]
                    # key_char stores the current letter from the key

                    shift = ord(key_char.upper()) - ord('A')
                    # Converts the keyword letter into a shift value (0-25)

                    if (value - shift) < 65:
                        value = (value - shift) + 26
                    else:
                        value = value - shift

                    print(chr(value), end="")
                    key_total += 1

                elif char.isalpha() and char.islower():

                    value = ord(char)

                    key_index = key_total % len(key)
                    key_char = key[key_index]

                    shift = ord(key_char.lower()) - ord('a')

                    if (value - shift) < 97:
                        value = (value - shift) + 26
                    else:
                        value = value - shift

                    print(chr(value), end="")
                    key_total += 1

                else:
                    print(char, end="")

            print()

        elif choice == "2":
            screen_cleaner()

            text = input("Enter the text to encrypt: ")
            key = input("Enter the key: ")

            key_total = 0

            for char in text:

                if char.isalpha() and char.isupper():

                    value = ord(char)

                    key_index = key_total % len(key)
                    key_char = key[key_index]

                    shift = ord(key_char.upper()) - ord('A')

                    if (value + shift) > 90:
                        value = (value + shift) - 26
                    else:
                        value = value + shift

                    print(chr(value), end="")
                    key_total += 1

                elif char.isalpha() and char.islower():

                    value = ord(char)

                    key_index = key_total % len(key)
                    key_char = key[key_index]

                    shift = ord(key_char.lower()) - ord('a')

                    if (value + shift) > 122:
                        value = (value + shift) - 26
                    else:
                        value = value + shift

                    print(chr(value), end="")
                    key_total += 1

                else:
                    print(char, end="")

            print()

        elif choice == "0":
            screen_cleaner()
            break

        else:
            screen_cleaner()
            print("Invalid option")
        print()
        input("Press enter to continue")
