import random


def rps():
    keep_playing = True
    while keep_playing is True
    player_input = input('Enter r, p, s, for Rock, Paper, Scissors')
    possible_actions = ['r', 'p', 's']
    computer_input = random.choice(possible_actions)

    print(f'You chose {player_input} and the computer chose {computer_input}')

    if player_input == computer_input:
        print(f'Both players chose {player_input}, a tie')
    elif player_input == 'r':
        if computer_input == 's':
            print('Rock smashes scissors, you win')
        else:print('Paper covers rock, computer wins')
elif player_input == 'p':
    if computer_input == 'r':
        print('Paper covers rock, you win')
    else:
        print('Scissors cuts paper')
elif player_input == 'S':
    if computer_input == 'p':
        print('Scissors cuts paper, you win')
    else:
        print('Rock smashes scissors, computer wins')
        
        choice = ('Would you like to keep playing?:[y/n]')
        if choice == 'y':
            keep_playing = True
        elif choice == 'n':
            keep_playing = False
    
    rps()
