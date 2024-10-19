import flcs

def info():
    print("""
    1) start a flashcard set
    2) create new flashcard set
    3) exit program
    """)

if __name__ == "__main__":
    print("Welcome to termcards, what do you want to do:")
    while True:
        info()
        inp = input(">")
        match inp:
            case "1":
                print("type name of a flashcard")
                try:
                    flcs.app(f"./flcs/{input(">")}.flc")
                except FileNotFoundError:
                    print("flashcard set not found")
            case "2":
                print("not a function yet")
            case "3":
                quit()
        