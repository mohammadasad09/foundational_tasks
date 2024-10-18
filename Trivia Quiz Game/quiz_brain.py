#question_number = 0
#question_list
#next_question()

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = question_list 
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: Your question is as follows: {current_question.text}. Is it 'True' or 'False': ").lower()
        while user_answer not in ['true','false']:
            user_answer = input("Please enter your answer again. You can only choose 'True' or 'False': ").lower()
        self.check_answer(user_answer,current_question.answer)

    
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    
    def check_answer(self, answer_1, answer_2):
        if answer_1 == answer_2.lower():
            print("You got the answer right!")
            self.score += 1
        else:
            print("You got the answer wrong. :(")
        print(f"The correct answer was {answer_2}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

