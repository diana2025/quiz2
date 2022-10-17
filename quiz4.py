q1 = {"question": "Vilken funktion används för att skriva ut saker på skärmen?",
      "answers": [{"answer": "print", "correct": False},
                  {"answer": "len", "correct": False},
                  {"answer": "for", "correct": False},
                  {"answer": "pprint", "correct": False},
                  {"answer": "pprint2", "correct": True}]}

q2 = {"question": "Vad heter nyckelordet för att göra en loop i Python?",
      "answers": [{"answer": "ans1", "correct": False},
                  {"answer": "ans2", "correct": False},
                  {"answer": "ans3", "correct": False},
                  {"answer": "ans4", "correct": True}]}

q3 = {"question": "Hur tar man fram längden på listan i variabeln fruits?",
      "answers": [{"answer": "ans5", "correct": True},
                  {"answer": "ans6", "correct": False},
                  {"answer": "ans7", "correct": False},
                  {"answer": "ans8", "correct": False}]}

q4 = {"question": "Vilken metod används för att sortera en lista?",
      "answers": [{"answer": "sorts()", "correct": False},
                  {"answer": "sort()", "correct": True},
                  {"answer": "sorter()", "correct": False}]}

q5 = {"question": "Kan jag skriva kod i en JSON-fil?",
      "answers": [{"answer": "Ja", "correct": False},
                  {"answer": "Det finns en app för det", "correct": False},
                  {"answer": "Nej", "correct": True}]}

questions = [q1, q2, q3, q4, q5]
correct_answers_count = 0
wrong_answers = []

for i in range(len(questions)):
    print(questions[i]['question'])
    answers = questions[i]['answers']

    answers_count = 0
    for n, answer in enumerate(answers, start=1):
        print(f"({n}) {answer['answer']}")
        answers_count = answers_count + 1  # number of answers

    # print(answers_count)

    user_answer = input(">")
    user_input_is_valid = user_answer.isdigit()

    while user_input_is_valid and int(user_answer) <= answers_count:
        if answers[int(user_answer) - 1]['correct']:
            print("Rätt svar")
            correct_answers_count = correct_answers_count + 1
        else:
            print("Fel svar, rätt svar är")
            wrong_answers.append("- " + questions[i]['question'])
            for answer in answers:
                if answer['correct']:
                    print(answer['answer'])
                    wrong_answers.append("Rätt svar: " + answer['answer'])
        break
    else:
        print("Wrong input, please try again")
        break

print("\n\n*** RESULTAT ***")
print("Du fick " + str(correct_answers_count) + " av " + str(len(questions)) + " möjliga poäng.\n")
print("Du svarade fel på dessa frågor:")
for i in range(0, len(wrong_answers)):
    print(wrong_answers[i])

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
