class QuizBrain:
    def __init__(self,q_list) -> None:
        self.question_number = 0
        self.score_correct = 0
        self.score_total = 0
        self.question_list = q_list
        
    
    def still_has_question(self):
        return (self.question_number < len(self.question_list))

                      
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = str(input(f"Q.{self.question_number}: {current_question.text}. (True/False?): ")).strip().lower()
        self.check_answer(user_answer, current_question.answer)
        print(f"Your current score: {self.score_correct}/{self.score_total}\n")
        
        
    def check_answer(self, user_answer, answer):
        if user_answer == answer.lower():
            self.score_correct += 1
            print("That's correct!")
        else:
            print("That's wrong!")
        self.score_total += 1
        print(f"The correct answer was: {answer}.")