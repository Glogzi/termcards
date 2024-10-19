import os

reset = '\033[0m'
redt = '\033[91m'
greent = '\033[92m'
yellowt = '\033[93m'

def welcome():
    os.system("cls || clear")
    print("welcome in flashcard set creator, first name a new flashcard set")
    print("(typing existing flashcard set will result in editing previous one)")
    change_set()

def delete_set(flc):
    print(f"are you sure you want to delete {yellowt}{flc}{reset}?")
    print("y/n (deafult: n)")
    y_or_n = input()
    match y_or_n:
        case "y":
            os.remove(f"flcs/{flc}.flc")
            print(f"{redt}removed{reset} \"{flc}\"")
            change_set()
        case _:
            print("deleting canceled")

def change_set():
    print(f"type {yellowt}&show&{reset} to show all of current sets and type {yellowt}&quit&{reset} to quit choosing a set")
    flc_name = input(">")
    match flc_name:
        case "&show&":
            directory = os.listdir("flcs/")
            for file in directory:
                file_splitted = file.split(".")
                if file_splitted[1] == "flc":
                    print(file_splitted[0])
            change_set()
        case "&quit&":
            return
        case _:    
            app(flc_name)
            return

def info():
    print(f"""
    1) add new flashcard
    2) delete flashcard
    3) show all flashcards
    4) change flashcard set
    5) exit creator
    {redt}6) delete current flashcard set{reset}
    """)

def show(flc):
    with open(f"flcs/{flc}.flc", "r") as f:
        lines = f.readlines()
        for line in lines:
            show_line = ""
            line_without_backslash_n = line.split("\n")[0]
            if lines.index(line) % 2 == 0:
                show_line = f"{greent}Q:{reset} {line_without_backslash_n}"
            else:
                show_line = f"{redt}A:{reset} {line_without_backslash_n}"
            print(show_line)
                

def add(flc):
    while True:
        print(f"please type a question (type {redt}&stop&{reset} to stop adding a flashcards)")
        print(f"{redt}!WARNING!{reset} typing a question same as existing answer might result in unexpected results while deleting flashcards")
        question = input(">")
        if question == "&stop&":
            return
        print("now type an answer to a question")
        print(f"{redt}!WARNING!{reset} typing an answer same as existing question might result in unexpected results while deleting flashcards")

        answer = input(">")
        with open(f"flcs/{flc}.flc", "a") as f:
            f.write(f"{question}\n{answer}\n")
        

def delete(flc):
    print("type question or answer of flashcard you want to delete")
    print(f"{redt}(if there's a question same as existing answer, will be deleted whatever was added first){reset}")
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
            print(f"{redt}question not found{reset}, nothing was deleted")
            f.writelines(all_lines)
            return
        

def app(flc_name):
    try:
        open(f"flcs/{flc_name}.flc", "x")
        print(f"{greent}created new flashcard set{reset} \"{flc_name}\"")
    except FileExistsError:
        print(f"{yellowt}editing{reset} \"{flc_name}\"")
    while True:
        info()
        usr_inp = input(">")
        match usr_inp:
            case "1":
                add(flc_name)
            case "2":
                delete(flc_name)
            case "3":
                show(flc_name)
            case "4":
                os.system("cls || clear")
                change_set()
            case "5":
                return
            case "6":
                delete_set(flc_name)
                return
            
if __name__ == "__main__":
    welcome()