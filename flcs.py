import random
import os

green = '\033[42m'
greent = '\033[92m'
red = '\033[41m'
redt = '\033[91m'

magenta = '\033[35m'
reset = '\033[0m'

QnA = []
with open('./flc.txt', "r", encoding="utf-8") as f:
    QnA = f.readlines()

for i in range(len(QnA)):
    new = QnA[i].splitlines()
    QnA[i] = new[0]
    

og_questions = []
og_answers = []
for i in range(len(QnA)):
    if i % 2 == 0:
        og_questions.append(QnA[i])
    else:
        og_answers.append(QnA[i])
questions = og_questions.copy()
answers = og_answers.copy()
loading = "|"
os.system("cls || clear")
while questions != []:
    pr = ((len(og_questions)-len(questions))*100)/len(og_answers)
    print(f"{round(pr)}% {greent}{loading*round(pr)}{redt}{loading*(100-round(pr))}{reset}")
    print(f"({greent}{len(og_questions)-len(questions)}/{len(og_questions)}{reset})")
    q = random.choice(questions)
    a = answers[questions.index(q)]
    
    print(q)
    inp = input(">")
    os.system("cls || clear")
    if inp.lower() == a: 
        print(f"{green}{inp}: NICE{reset}")
        questions.pop(questions.index(q))
        answers.pop(answers.index(a))
    else: 
        print(f"{red}{inp}: NOT NICE ({a}){reset}")
        questions = og_questions.copy()
        answers = og_answers.copy()
print(f"{magenta}gratulacje{reset}")
input()