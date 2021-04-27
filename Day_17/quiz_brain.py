class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def ask_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.text} (True/False)")
        self.check_answer(user_answer, current_q.answer)
        print(f"You're score is {self.score}/{self.question_number}")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("incorrect!")
        print(f"The correct answer is {c_answer}")
        print("\n")
