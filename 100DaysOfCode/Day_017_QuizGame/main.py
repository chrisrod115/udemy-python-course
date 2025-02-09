from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain
import os

model=QuestionModel


clear_screen=lambda:os.system('cls' if os.name=='nt' else 'clear')

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=QuestionModel(question_text, question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

clear_screen()
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")