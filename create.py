import os

def info():
    print("""
        1) add new flashcard
        2) delete flashcard
        3) exit creator
    """)

def add(flc):
    while True:
        print("please type a question (type &stop& to stop adding a flashcards)")
        print("WARNING! typing a question same as existing answer might result in unexpected results while deleting flashcards")
        question = input(">")
        if question == "&stop&":
            return
        print("now type an answer to a question")
        print("WARNING! typing an answer same as existing question might result in unexpected results while deleting flashcards")

        answer = input(">")
        with open(f"flcs/{flc}.flc", "a") as f:
            f.write(f"{question}\n{answer}\n")
        

def delete(flc):
    print("type question or answer of flashcard you want to delete")
    print("(if there's a question same as existing answer, will be deleted whatever was added first)")
    question_to_delete = input(">")+"\n"
    all_lines = []
    with open(f"flcs/{flc}.flc", "r") as f:
        all_lines = f.readlines()
    with open(f"flcs/{flc}.flc", "w") as f:
        try:
            line_index = all_lines.index(question_to_delete)
            if line_index % 2 == 0:
                all_lines.pop(line_index)
                all_lines.pop(line_index)
                f.writelines(all_lines)
                return
            all_lines.pop(line_index)
            all_lines.pop(line_index-1)
            f.writelines(all_lines)
            return
        except ValueError:
            print("question not found, nothing was deleted")
            f.writelines(all_lines)
            return
        

def app():
    os.system("cls || clear")
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
            
if __name__ == "__main__":
    app()