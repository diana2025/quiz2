import requests
import json
import pprint

QUIZ_URL = "https://bjornkjellgren.se/quiz/v2/questions"

response = requests.get(QUIZ_URL)

response_json = response.json()

# pprint.pprint(response_json)

questions = response_json['questions']
questionsCount = len(questions)

# print(type(questions))
# question1 = questions[1]
correctAnswer = 0
correctAnsCount = 0

for question in questions:
    # pprint.pprint(question)
    print(f"{question['prompt']}")
    answers = question['answers']
    # print(answers)
    for n, answer in enumerate(answers, start=1):
        print(str(n) + " " + answer['answer'])

        if (answer['correct']):
            correctAnswer = str(n)

    lastAnswerNumber = str(n)

    # Här bör användaren få svara på frågan
    # Följt av rättning och poängräkning
    user_ans = input(">")
    while (user_ans > lastAnswerNumber or user_ans < str('1')):
        print("You must choose a number between 1 and " + str(n))
        user_ans = input(">")

    if (user_ans == correctAnswer):
        print("Ditt svar: " + user_ans)
        print("Rätt!")
        correctAnsCount = correctAnsCount + 1
    else:
        print("Ditt svar: " + user_ans)
        print("Fel: Rätt svar är " + str(correctAnswer))

    print("-" * 80)

print("\n" + "RESULTAT: ")
print("Du fick " + str(correctAnsCount) + " poäng av möjliga " + str(questionsCount))

# Todo Låt användaren svara
#   Skall bara få svara på de alternativ som finn
# Todo rätta svaret
#   Vilket svar syftade man på?
#   Få tag på frågan användaren syftade på
#   Kontrollera om det var rätt svarsalternativ
