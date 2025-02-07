class QuizBrain:
    def __init__(self, list) -> None:
        self.question_number=0
        self.question_list=list
    
    
    def get_question(self):
        user_input=str(input(f"Q{self.question_number+1}: {self.question_list[self.question_number].question} (True/False)?: ")).strip().lower()
        return user_input
    
    
    def 