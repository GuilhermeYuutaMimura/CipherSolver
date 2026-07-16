import os
def screen_cleaner():
    os.system("cls" if os.name == "nt" else "clear")
    #cls para fazer CipherSolver ser Cross-plataform
#os.system("clear")
#Screen cleaner function, to clear the terminal screen when called
