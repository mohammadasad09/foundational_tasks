import random
import os

def difficulty_level(difficulty_chosen):
    global range_limit
    global random_number
    global guesses
    difficulty = {"easy": 100, "medium": 200, "hard": 300, "professional": 400, "legend": 500}
    range_limit = difficulty[difficulty_chosen]
    guesses = difficulty[difficulty_chosen] // 50  # More balanced calculation
    random_number = random.randint(0, range_limit)

resume_game = 'yes'

while resume_game == 'yes':
    guessed_number_list = []
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Number Guessing game!")
    
    diff_selected = input("Please select difficulty from the following: \n1. Easy \n2. Medium \n3. Hard \n4. Professional\n5. Legend\n").lower()
    
    while diff_selected not in ['easy', 'medium', 'hard', 'professional', 'legend']:
       diff_selected = input("Invalid difficulty level, please try again: ")
    
    difficulty_level(diff_selected)
    print(f"Select a number between 0 and {range_limit}. You have {guesses} guesses.")

    while guesses > 0:

        chosen_number = int(input("Please pick a number: "))

        while chosen_number not in range(range_limit + 1):
            chosen_number = int(input("please pick a valid number from 0 to 500: "))
        while chosen_number in guessed_number_list:
            chosen_number = int(input(f"You have already guessed {chosen_number}. Kindly try again: "))
        if chosen_number == random_number: 
            print("Congratulations! You guessed the correct number. You win.")
            guessed_number_list.append(chosen_number)            
            break
        elif chosen_number > random_number:
            guesses -= 1
            print(f"You guessed too high. You have {guesses} guesses left.")
            guessed_number_list.append(chosen_number)
        else:
            guesses -= 1
            print(f"You guessed too low. You have {guesses} guesses left.")
            guessed_number_list.append(chosen_number)
        if guesses == 0:
            print(f"You lost. The number was {random_number}.")
    
    resume_game = input("Would you like to play another game? 'yes' or 'no': ").lower()

print("Thanks for playing!")
