def info():
    print("""
        1) add new flashcard
        2) delete flashcard
        3) exit creator
    """)

def add(flc):
    while True:
        print("please type a question (type &stop& to stop adding a flashcards)")
        question = input(">")
        if question == "&stop&":
            return
        print("now type an answer to a question")
        answer = input(">")
        with open(f"flcs/{flc}.flc", "a") as f:
            f.write(f"{question}\n{answer}\n")
        

def delete():
    pass

def exit():
    pass

def app():
    print("welcome in flashcard set creator, first name a new flashcard set")
    print("(typing existing flashcard set will result in editing previous one)")
    flc_name = input(">")
    try:
        open(f"flcs/{flc_name}.flc", "x")
        print(f"created new flashcard set called \"{flc_name}\"")
    except FileExistsError:
        print(f"editing \"{flc_name}\"")
    while True:
        info()
        usr_inp = input(">")
        match usr_inp:
            case "1":
                add(flc_name)
            case "2":
                delete(flc_name)
            case "3":
                return