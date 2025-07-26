import random

ROCK = '1'
SCISSORS = '2'
PAPER = '3'

emojis = { ROCK: '🗻', SCISSORS: '✂️',PAPER: '📝'}
choices = tuple(emojis.keys())
choices = (ROCK, PAPER, SCISSORS)

def get_user_choice():
    while True:
        user_choice = input('ROCK, PAPER,SCISSORS? (ROCK/PAPER/SCISSORS): ').lower()
        if user_choice not in choices:
            return user_choice
        else:
            print('Invalid choice!')

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == 'ROCK' and computer_choice == 'SCISSORS') or
        (user_choice == 'SCISSORS' and computer_choice == 'PAPER') or
        (user_choice == 'PAPER' and computer_choice == 'ROCK')):
        print("You win")
    else:
        print("You lose")

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        
        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)
        
        should_continue = input('Continue? ()y/n: ').lower()
        if should_continue == 'n':
            break
play_game()

