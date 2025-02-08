import html
from time import sleep


class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = html.unescape(self.question_list[self.question_number].question)
        current_question_answer = self.question_list[self.question_number].answer
        answer = input(f"Q.{self.question_number + 1}: {current_question} (True/False): ")
        self.question_number = self.question_number + 1
        self.check_answer(answer, current_question_answer)

    def is_question_available(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if correct_answer == user_answer:
            self.score += 1
            print("You are correct")
        else:
            print("Ops, better luck next time")

        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{len(self.question_list)}")
        print("\n")
