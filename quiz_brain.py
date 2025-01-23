class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").title()
        self.check_answer(current_question, user_answer)


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, current_question, user_answer):
        if current_question.answer == user_answer:
            print("You are right!")
            self.score += 1
            print(f"Your score is: {self.score}/ {self.question_number} for the Question: {current_question.text}")
        else:
            print("You are false")
