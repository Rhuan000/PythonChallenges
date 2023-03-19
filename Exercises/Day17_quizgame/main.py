from data import question_data
from question_model import Question
from quiz_brain import Quiz_brain

question_bank = []

for key in question_data:
    new_question = Question(key['question'], key['correct_answer'],)
    question_bank.append(new_question)

quiz = Quiz_brain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the Quiz.")
print(f"You final score was: {quiz.score}/{quiz.question_number}")