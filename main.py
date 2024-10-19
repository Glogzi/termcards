import flcs
import create
import os

def info():
    print("""
    1) start a flashcard set
    2) create new flashcard set
    3) exit program
    """)

if __name__ == "__main__":
    if not os.path.exists("./flcs"):
        os.makedirs("./flcs")
    print("Welcome to termcards, what do you want to do:")
    while True:
        info()
        inp = input(">")
        match inp:
            case "1":
                flcs.welcome()
            case "2":
                create.welcome()                
            case "3":
                quit()        