# Name-constants to represent the seeds and cell contents
EMPTY = 0
CROSS = 1
CIRCLE = 2

# Name-constants to represent the various states of the game
PLAYING = 0
DRAW = 1
CROSS_WON = 2
CIRCLE_WON = 3

# The game board and the game status
board = []
# number of rows and columns
ROWS = 3
COLS = 3
current_state = ''  # the current state of the game - (PLAYING, DRAW, CROSS_WON, CIRCLE_WON)
current_player = ''  # the current player (CROSS or CIRCLE)
current_row, current_col = '', ''  # current seed's row and column


def init_game():
    """
    Initialize the game - board contents and the current states
    """
    global current_state, current_player
    for row in range(ROWS):
        one_row = []
        for col in range(COLS):
            one_row.append(EMPTY)  # all cells empty
        board.append(one_row)
    current_state = PLAYING  # ready to play
    current_player = CROSS  # cross plays first


def player_move(current):
    """
    Player with the "current" makes one move, with input validation.
    Update global variables "current_row" and "current_col".
    :param current:
    """
    valid_input = False  # for input validation
    while not valid_input:  # repeat until input is valid
        if current == CROSS:
            ans = input("Player 'X', enter your move (row[1-3] column[1-3]): ").split()
            row, col = int(ans[0]) - 1, int(ans[1]) - 1
        else:
            ans = input("Player 'O', enter your move (row[1-3] column[1-3]): ").split()
            row, col = int(ans[0]) - 1, int(ans[1]) - 1
        valid_input = is_valid_move(row, col, current)
        if not valid_input:
            print("This move at ({0},{1}) is not valid. Try again...".format(row + 1, col + 1))


def is_valid_move(row, col, current):
    global current_row, current_col
    if (0 <= row < ROWS) and (0 <= col < COLS) and (board[row][col] == EMPTY):
        current_row, current_col = row, col
        board[current_row][current_col] = current  # update game-board content
        return True
    else:
        return False


def update_game(current, current_row, current_col):
    """
    Update the "current_tate" after the player with "current" has placed on (current_row, current_col).
    :param current:
    :param current_row:
    :param current_col:
    """
    global current_state
    if has_won(current, current_row, current_col):  # check if winning move
        current_state = CROSS_WON if current == CROSS else CIRCLE_WON
    elif is_draw():  # check for draw
        current_state = DRAW
    # Otherwise, no change to current_state (still PLAYING).


def is_draw():
    """
    :return True if it is a draw (no more empty cell)
    Shall declare draw if no player can "possibly" win
    """
    draw = True
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == EMPTY:  # if there is empty cell
                draw = False
                break
    return draw


def has_won(current, current_row, current_col):
    """
    :param current:
    :param current_row:
    :param current_col:
    :return: True if the player with "current" has won after placing at (current_row, current_col)
    """
    return validate_3_in_diagonal(current) or validate_3_in_column(current_col, current) or \
           validate_3_in_row(current_row, current)


def validate_3_in_diagonal(current):
    """
    :param current:
    :return: True if the player with "current" has marked at least one diagonal after placing at
    (current_row, current_col)
    """
    return backward_diagonal(current) or forward_diagonal(current)


def backward_diagonal(current):
    """
    :param current:
    :return: True if the player with "current" has marked all backward diagonal after placing at
    (current_row, current_col)
    """
    return board[0][2] == current and board[1][1] == current and board[2][0] == current


def forward_diagonal(current):
    """
    :param current:
    :return: True if the player with "current" has marked all forward diagonal after placing at
    (current_row, current_col)
    """
    return board[0][0] == current and board[1][1] == current and board[2][2] == current


def validate_3_in_column(current_col, current):
    """
    :param current_col:
    :param current:
    :return: True if the player with "current" has marked some column after placing at
    (current_row, current_col)
    """
    return board[0][current_col] == current and board[1][current_col] == current and board[2][current_col] == current


def validate_3_in_row(current_row, current):
    """
    :param current_row:
    :param current:
    :return: True if the player with "current" has marked some row after placing at
    (current_row, current_col)
    """
    return board[current_row][0] == current and board[current_row][1] == current and board[current_row][2] == current


def print_board():
    """
    Print the game board.
    """
    for row in range(ROWS):
        for col in range(COLS):
            print_cell(board[row][col])  # print each of the cells
            if col != COLS - 1:
                print("|", end="")
        print()
        if row != ROWS - 1:
            print("-----------")


def print_cell(content):
    """
    Print a cell with the specified "content".
    :param content:
    """
    if content == EMPTY:
        print("   ", end="")
    elif content == CIRCLE:
        print(" O ", end="")
    else:
        print(" X ", end="")


""" The entry main method (the program starts here) """


def game_loop():
    global current_player
    # Initialize the game-board and current status
    init_game()
    while current_state == PLAYING:  # repeat if not game-over
        player_move(current_player)  # update currentRow and currentCol
        update_game(current_player, current_row, current_col)  # update current_state
        print_board()
        # Print message if game-over
        if current_state == CROSS_WON:
            print("'X' won! Bye!")
        elif current_state == CIRCLE_WON:
            print("'O' won! Bye!")
        elif current_state == DRAW:
            print("It's a Draw! Bye!")
        # Switch player
        if current_player == CROSS:
            current_player = CIRCLE
        else:
            current_player = CROSS
        # current_player = CIRCLE if current_player == CROSS else CROSS


game_loop()
