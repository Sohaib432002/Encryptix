import random


def get_user_choice():
    while True:
        print('\nSelect one option:')
        print('1 - Rock')
        print('2 - Paper')
        print('3 - Scissors')
        choice = input('Enter your choice (1/2/3): ')
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print('Invalid choice, please try again.')


def get_choice_name(choice):
    return {1: 'Rock', 2: 'Paper', 3: 'Scissors'}.get(choice, '')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Draw'
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
            (user_choice == 'Paper' and computer_choice == 'Rock') or \
            (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return 'User'
    else:
        return 'Computer'


def play_round():
    user_choice_num = get_user_choice()
    user_choice_name = get_choice_name(user_choice_num)
    computer_choice_name = random.choice(['Rock', 'Paper', 'Scissors'])

    print(f'Your choice: {user_choice_name}')
    print(f'Computer\'s choice: {computer_choice_name}')

    winner = determine_winner(user_choice_name, computer_choice_name)
    if winner == 'Draw':
        print('It\'s a draw!')
    elif winner == 'User':
        print('Congratulations! You won this round.')
    else:
        print('System won this round.')
    return winner


def main():
    while True:
        try:
            num_games = int(input('How many matches do you want to play? '))
            if num_games <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        user_score, computer_score = 0, 0

        for _ in range(num_games):
            winner = play_round()
            if winner == 'User':
                user_score += 1
            elif winner == 'Computer':
                computer_score += 1
            print('---------------------------------------------')

        print(f'\nFinal Scores:\nYou: {user_score}\nComputer: {computer_score}')

        if user_score > computer_score:
            print('Congratulations! You won the game.')
        elif user_score == computer_score:
            print('It\'s a draw!')
        else:
            print('Sorry, you lost. System won the game.')

        play_again = input('Would you like to play again? (y/n): ').lower()
        if play_again == 'n':
            print('Thanks for playing!')
            break


if __name__ == '__main__':
    main()
