from random import choices

from util.screen_cleaner import screen_cleaner

def vigenere():
    screen_cleaner()
    translation_text = None
    choice = None
    key_total = 0 #counts the total number the key got itinarated
    key_index = 0 #counts the actual index

    while True:
        print("""
[1] Decrypt
[2] Encrypt
[0] Go Back""")
        
        print("")
        choice = input("Option: ")

        if choice == "2": #accidently did the wrong order
            screen_cleaner()
            text = input("Enter the text to Encrypt: ")
            key = input("Enter the key: ")

            for char in text:

                if char.isalpha() and char.islower():

                    value = (ord(char))
                    key_index = key_total % len(key) #Conta usando o index atual, index total e tamanho da key pra achar a letra para encriptar a letra atual
                    key_char = key[key_index] #key_char pega a letra atual da key usando o index calculado
                    shift = ord(key_char.lower()) - ord('a') #o valor que vai ser mudado, pegando o ascii e subtraindo com o ascii de 'a', ou seja o primero, logo k (107) - a(97) = 10 que serão movidos para chegar a letra certa

                    if (value + shift) > 122:
                        value = (value + shift) - 26
                    
                    else:
                        value = (value + shift)
                    print(chr(value), end="")
                key_total += 1
        
        if choice == "1":
            screen_cleaner()
            text = input("Enter the text to Decripty")
            