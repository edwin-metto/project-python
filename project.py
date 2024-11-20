import random


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'


def play_game(rounds=3):
    user_score = 0
    computer_score = 0
    target_score = (rounds // 2) + 1  

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}/{rounds}")
        
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        
        winner = determine_winner(user_choice, computer_choice)

        if winner == 'user':
            user_score += 1
            print("You win this round!")
        elif winner == 'computer':
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a draw!")

        print(f"Score: You {user_score} - Computer {computer_score}")

        
        if user_score >= target_score:
            print("\nYou win the game!")
            break
        elif computer_score >= target_score:
            print("\nComputer wins the game!")
            break

    
    if user_score > computer_score:
        print("\nYou win the game!")
    elif computer_score > user_score:
        print("\nComputer wins the game!")
    else:
        print("\nIt's a tie game!")


if __name__ == "__main__":
    rounds = 3  
    play_game(rounds)
