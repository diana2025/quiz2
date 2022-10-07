q1 = {"question": "Vilken funktion används för att skriva ut saker på skärmen?",
      "answers": [{"answer": "print", "correct": True},
                  {"answer": "len", "correct": False},
                  {"answer": "for", "correct": False},
                  {"answer": "pprint", "correct": True}]}

q2 = {"question": "Vad heter nyckelordet för att göra en loop i Python?",
      "answers": [{"answer": "ans1", "correct": True},
                  {"answer": "ans2", "correct": False},
                  {"answer": "ans3", "correct": False},
                  {"answer": "ans4", "correct": True}]}

q3 = {"question": "Hur tar man fram längden på listan i variabeln fruits?",
      "answers": [{"answer": "ans5", "correct": True},
                  {"answer": "ans6", "correct": False},
                  {"answer": "ans7", "correct": False},
                  {"answer": "ans8", "correct": True}]}

questions = [q1, q2, q3]

for i in range(len(questions)):
    print(questions[i]['question'])
    answers = questions[i]['answers']

    for n, answer in enumerate(answers, start=1):
        print(f"({n}) {answer['answer']}")

    user_answer = int(input(">"))
    if answers[user_answer - 1]['correct']:
        print("Rätt svar")
    else:
        print("Fel svar, rätt svar är")
        for answer in answers:
            if answer['correct']:
                print(answer['answer'])

# userAnswer1 = input("Vilken funktion används för att få input från användaren?")
# correctAnswer1 = "input"
# if correctAnswer1 == userAnswer1:
#    print("Rätt")
# if correctAnswer1 != userAnswer1:
#    print("Fel: rätt svar är: " + correctAnswer1)

# userAnswer1 = input("Vilken operator används för att addera 2 siffror?")
# correctAnswer1 = "+"
# if correctAnswer1 == userAnswer1:
#    print("Rätt")
# if correctAnswer1 != userAnswer1:
#    print("Fel: rätt svar är: " + correctAnswer1)
