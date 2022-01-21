board = [['_', '_', '_']
       , ['_', '_', '_']
       , ['_', '_', '_']]

# game variables:
empty = '_'
player1 = 'X'
player2 = 'O'
play = True


def game_board():
    print("\n    0    1    2 ")  # indexing the columns
    for row_index, the_board in enumerate(board):  # indexing the rows
        print(row_index, the_board)


def place_player(active_player, row, column):  # place the player on the board
    if board[row][column] == empty:
        board[row][column] = active_player
    return board


def swap_player(active_player):  # swap between 'X' and 'O' turns
    if active_player == player1:
        return player2
    else:
        return player1


def new_game_request(new_game='game not over yet'):
    global board
    global play
    while new_game.lower() != 'y' or 'n':
        new_game = input('Would you like to start a new game? y/n \n')
        if new_game.lower() == 'n':
            play = False
            return play

        elif new_game.lower() == 'y':
            board = [['_', '_', '_']
                   , ['_', '_', '_']
                   , ['_', '_', '_']]
            return play   # still defined as True for a new game


def main_game():

    while play:
        active_player = player1  # 'X' player will start the game
        game_won = False
        game_tie = False
        while not game_won and not game_tie:
            game_board()
            try:
                # ask for the player's row input + check validation:
                row = int(input(f'Player {active_player}, choose a row between 0, 1, 2: '))
                if row not in range(3):
                    print('Invalid row, please enter a valid number position between 0, 1, 2')
                    continue
            except ValueError:
                print('Invalid character! , please enter only a valid number position between 0, 1, 2')
                continue
            try:
                # ask for the player's column input + check validation:
                column = int(input(f'Player {active_player}, choose a column between 0, 1, 2: '))
                if column not in range(3):
                    print('Invalid column, please enter a valid number position between 0, 1, 2')
                    continue
            except ValueError:
                print('Invalid character! , please enter only a valid number position between 0, 1, 2')
                continue
            # check if the spot on the board is already taken:
            if board[row][column] == player1 or board[row][column] == player2:
                print("Already taken! try a different position")

            else:  # input is valid and can be placed on board:
                place_player(active_player, row, column)

                # after editing the board, check if there is a win:
                if check_win():
                    print(f'\nPlayer {active_player} is the winner!')
                    game_won = True
                    game_board()

                    if not new_game_request():
                        print('\nUntil next time, hope you enjoyed the game!!')
                        break

                # check for a tie:
                elif check_tie():
                    print("It\'s a tie! ")
                    game_tie = True

                    if not new_game_request():
                        print('\nUntil next time, hope you enjoyed the game!')
                        break

                else:  # swap the turn to the other player:
                    active_player = swap_player(active_player)


def check_tie():
    for row in range(3):
        for col in range(3):
            if board[row][col] == empty:
                return False
    return True


def check_win():
    for row in board:  # check row win
        if row.count(row[0]) == len(row) and row[0] != empty:
            return True

    diags = []  # check diagonal line win - option 1
    for idx in range(len(board)):
        diags.append(board[idx][idx])
    if diags.count(diags[0]) == len(diags) and diags[0] != empty:
        return True

    # # check diagonal line win - option 2
    if board[2][0] == board[1][1] == board[0][2] != empty:
        return True

    for column in range(len(board)):  # check column win
        check = []
        for row in board:
            check.append(row[column])
        if check.count(check[0]) == len(check) and check[0] != empty:
            return True


main_game()
