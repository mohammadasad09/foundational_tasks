import pandas as pd
import random
import os

# Load the data from CSV
info_df = pd.read_csv("Day 14 - Higher or Lower/instagram_global_top_1000.csv", index_col="Rank")
analysis_subset = info_df[['Account', 'Title', 'Followers']].dropna()

def get_random_account(analysis_subset: pd.DataFrame) -> tuple[str, int]:
    """ Select a random account and retrieve the title and followers count """
    random_account = analysis_subset.sample(1).iloc[0]
    return random_account['Title'], int(random_account['Followers'])

def play_round(account1: str, followers1: int, account2: str, followers2: int) -> bool:
    """ Play a single round of the game, ask user for input, and validate the result """
    print(f"Compare these accounts:\n1. {account1} \n2. {account2}")

    while True:
        player_choice = input(f"Who has more followers?\nType '1' for {account1}\nType '2' for {account2}\n").strip()
        if player_choice in ['1', '2']:
            break
        print("Please enter '1' or '2'.")

    if (player_choice == '1' and followers1 > followers2) or (player_choice == '2' and followers2 > followers1):
        return True
    return False

def higher_or_lower_game(analysis_subset: pd.DataFrame) -> None:
    game_continue = 'yes'
    total_game_counter = 0
    while game_continue == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        if total_game_counter == 0:
            print("Welcome to the Higher or Lower Game!\n")
        else:
            print("Welcome to another game of Higher and Lower. Thank you for playing again.\n")
        if analysis_subset.empty or len(analysis_subset) < 2:
            print("Insufficient data to play the game.")
            return
        score = 0
        next_round = 'yes'

        # Start the game with a random account
        account1, followers1 = get_random_account(analysis_subset)

        while next_round == 'yes':
            account2, followers2 = get_random_account(analysis_subset)

            # Ensure two different accounts are selected
            while account1 == account2:
                account2, followers2 = get_random_account(analysis_subset)

            # Play a round and check the result
            if play_round(account1, followers1, account2, followers2):
                score += 1
                print(f"You are correct! {account1 if followers1 > followers2 else account2} has more followers. Current Score: {score}")

                # Assign the account with more followers to account1 for the next round
                if followers1 > followers2:
                    account1, followers1 = account1, followers1  # Keep the same account
                else:
                    account1, followers1 = account2, followers2  # Assign account2 to account1
            else:
                print(f"Sorry, that's wrong.")
                break
            
            next_round = input("Do you want to play another round? (yes/no): ").strip().lower()
            if next_round not in ['yes', 'no']:
                print("Please enter 'yes' or 'no'.")
                next_round = 'no'

        print(f"Game over! Your final score is: {score}")
        
        game_continue = input("Would you like to reset and play another game? 'yes' or 'no': ").lower()
        while game_continue not in ['yes','no']:
            game_continue = input("Please enter either 'yes' or 'no': ").lower()
        total_game_counter += 1

higher_or_lower_game(analysis_subset)