#Make a two-player Rock-Paper-Scissors game.  
#Compare them, print out a message of congratulations to the winner.
#Ask if the players want to start a new game.

def winner_calculation(option1, option2):
    if option1 == option2:
        return 'Tie!'

    if option1 == 'rock' and option2 == 'paper':
        return 'Player 2 win';

    if option2 == 'rock' and option1 == 'paper':
        return 'Player 1 win'

    if option1 == 'scissors' and option2 == 'paper':
        return 'Player 1 win'

    if option2 == 'scissors' and option1 == 'paper':
        return 'Player 2 win'

    if option1 == 'rock' and option2 == 'scissors':
        return 'Player 1 win'

    if option2 == 'rock' and option1 == 'scissors':
        return 'Player 2 win'

def is_invalid(optt):
    return optt != 'rock' and optt != 'paper' and optt != 'scissors'

end = 'yes'
while end == 'yes':
    player1 = input('Player 1, enter a play: ')
    while is_invalid(player1):
        player1 = input('Try again player 1: ')

    player2 = input('Player 2, enter a play: ')
    while is_invalid(player2):
        player2 = input('Try again player 2: ')

    result = winner_calculation(player1, player2)
    print(result)
    end = input('Do you want a new game? ')

    