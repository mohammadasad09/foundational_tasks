# True/False Game 
from data import question_data
from quiz_brain import QuizBrain, Question


question_bank = []

question_number = input("How many questions would you like to attempt? (1-50): ")
while question_number not in [str(x) for x in range(1,51)]:
    question_number = input("Please enter a valid number:")
    
for x in range(len(question_data)):
    specific_question = question_data[x]["question"]
    specific_answer = question_data[x]["correct_answer"]
    question_bank.append(Question(specific_question, specific_answer))

quiz = QuizBrain(question_bank[1:int(question_number) + 1])

while quiz.still_has_questions():
    quiz.next_question()


print(f"You have completed the quiz. Your final score was: {quiz.score}/{quiz.question_number}.")