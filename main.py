# BibleQuiz.py

import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "On what day did TMH create the sun & moon?": [
        "day 3", "day 2", "day 1", "day 4"
    ],
    "How many nights did the flood in Genesis last?": [
        "40", "30", "72", "12"
    ],
    "How many tribes are in the nation of Israel?": [
        "12", "7", "23", "18"
    ],
    "Who was Abraham's first child?": [
        "Ishmael", "Tahar", "Lot", "Isaac"
    ],
    "Who facilitated the covenant between the Israelites and TMH in Exodus": [
        "Moses", "Caleb", "Joshua", "Aaron"
    ],
}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

num_correct = 0
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question} ")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
    for label, alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")

    while (answer_label := input("\nAnswer? ")) not in labeled_alternatives:
        print(f"please choose one of the following as an answer {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct += 1
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")


print(f"\nYou got {num_correct} correct out of {num} questions")
