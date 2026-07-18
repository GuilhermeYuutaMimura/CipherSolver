from util.screen_cleaner import screen_cleaner
def morse():
    choice = None
    split_text = []
    
    morse_code = {
    # Letters
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",

    # Numbers
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",

    # Symbols
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
    " ": "/"
}
    reverse_morse = {value: key for key, value in morse_code.items()} #Saves times, by reversing the morse_code to morse to letter
    while True:
        screen_cleaner()

        print("Morse Cipher")
        print("""
[1] Decrypt
[2] Encrypt
[0] Go Back""")
        print("")
        choice = input("Option: ")

        if choice == "1":
            screen_cleaner()

            text = input("Enter the text to decrypt: ")
            split_text = text.split()

            for i in split_text:
                
                print(reverse_morse[i], end=" ")
                
        elif choice == "2":
            screen_cleaner()

            text = input("Enter the text to encrypt: ")

            for i in text:
                print(morse_code[i], end=" ")
        
        elif choice == "0":
            screen_cleaner()
            break

        else:
            screen_cleaner()
            print("Invalid choice")
        print()
        input("Press enter to continue")