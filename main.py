from models.QuestionModel import QuestionModel
from data.questions import data
from quiz import Quiz

question_bank = []

for qst in data:
    question = qst['question']
    answer = qst['correct_answer']

    new_question = QuestionModel(question=question, answer=answer)
    question_bank.append(new_question)

# print(question_bank)
quiz = Quiz(question_bank)

while quiz.is_question_available():
    quiz.next_question()

print("Congratulation you finish the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")