from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

model=QuestionModel

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=QuestionModel(question_text, question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
print(quiz.get_question())
