questions_file = open("questions.txt")
answers_file = open("answers.txt")

questions = questions_file.readlines()
answers = answers_file.readlines()

questions_file.close()
answers_file.close()

questionsCount = len(questions)
correctAns = 0

for i in range(questionsCount):
    question = questions[i].strip()
    answer = answers[i].strip()

    userAnswer = input(question)
    if userAnswer == answer:
        print("Rätt!")
        correctAns = correctAns + 1
    else:
        print("Fel: Rätt svar är " + answer)

print("RESULTAT: ")
print("Du fick " + str(correctAns) + " poäng av möjliga " + str(questionsCount))

"""userAnswer = input(questions.readline())
correctAnswer = answers.readline()


if userAnswer == correctAnswer.strip():
    print("Rätt!")
    correctAns = correctAns + 1
else:
    print("Fel: Rätt svar är " + correctAnswer)

userAnswer = input(questions.readline())
correctAnswer = answers.readline()

if userAnswer == correctAnswer.strip():
    print("Rätt!")
    correctAns = correctAns + 1
else:
    print("Fel: Rätt svar är " + correctAnswer)

userAnswer = input(questions.readline())
correctAnswer = answers.readline()

if userAnswer == correctAnswer.strip():
    print("Rätt!")
    correctAns = correctAns + 1
else:
    print("Fel: Rätt svar är " + correctAnswer)

print("RESULTAT: ")
print("Du fick " + str(correctAns) + " poäng av möjliga " + str(questionsCount))
"""