from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz.ask_question()

while quiz.still_has_questions():
    quiz.ask_question()

print("That's the end of the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
