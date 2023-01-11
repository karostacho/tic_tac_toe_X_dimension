import sys
import time
from random import randrange
from copy import deepcopy

# GLOBAL VARIABLES
default_empty_field = "."
board_dim = 3
move_time = 1
tie = "I think it is a tie.\n"


# BOARD
def init_board():
    """Returns an empty 3-by-3 board (with default character)."""
    board = [[default_empty_field for row in range(board_dim)] for col in range(board_dim)]
    return board


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    row_letters = ['A', 'B', 'C']
    typical_row = "{}   {} | {} | {} "
    borderline = "   ---+---+---"

    print("\n    1   2   3\n")
    for row in range(board_dim):
        print(typical_row.format(row_letters[row], board[row][0], board[row][1], board[row][2]))
        if row < board_dim - 1:
            print(borderline)
    print("\n")


# MOVING
def translate_coordinate(row):
    """Translates rows coordinates provided by player to numerical values compatible with the board"""
    if row == "A":
        return 0
    if row == "B":
        return 1
    if row == "C":
        return 2
    else:
        return -1


def is_this_place_occupied(board, row, col):
    """Checks if the given position is already occupied by any given player"""
    if board[row][col] == default_empty_field:
        return False
    else:
        return True


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row = -1
    col = -1
    valid_coordinates = [0, 1, 2]

    while row not in valid_coordinates or col not in valid_coordinates or is_this_place_occupied(board, row, col):
        user_coordinates = input("What is your move player {}: ".format(player.upper()))
        if user_coordinates == "quit":
            sys.exit(0)
        elif len(user_coordinates) == 2:
            row = translate_coordinate(user_coordinates[0].upper())
            col = int(user_coordinates[1]) - 1

    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = player


def next_player(player):
    """Returns next player for another turn"""
    if player == "x":
        return "o"
    else:
        return "x"


# CHECKING FOR WINNER
def get_current_results(board):
    """Returns a list of all rows columns and diagonal for checking the winner"""
    current_results = []
    diagonal1 = board[0][0] + board[1][1] + board[2][2]
    diagonal2 = board[0][2] + board[1][1] + board[2][0]
    for row in range(board_dim):
        current_results.append(board[row][0] + board[row][1] + board[row][2])
    for col in range(board_dim):
        current_results.append(board[0][col] + board[1][col] + board[2][col])
    current_results.append(diagonal1)
    current_results.append(diagonal2)
    return current_results


def has_won(board, player):
    """Returns True if player has won the game."""
    current_results = get_current_results(board)

    if player * 3 in current_results:
        return True
    else:
        return False


def full_board_check(board):
    """Returns True if board is full."""
    all_characters_on_the_board = []
    for row in range(board_dim):
        for col in range(board_dim):
            all_characters_on_the_board.append(board[row][col])

    if default_empty_field in all_characters_on_the_board:
        return False
    else:
        return True


def print_result(winner):
    """Congratulates winner"""
    print("Congratulations player {}.\nYou have won!\n".format(winner.upper()))


# AI IMPLEMENTATION
def random_coordinate():
    return randrange(board_dim)


def get_random_ai_move(board):
    """Returns the coordinates of a valid move for Random-AI."""
    row = random_coordinate()
    col = random_coordinate()

    while is_this_place_occupied(board, row, col):
        row = random_coordinate()
        col = random_coordinate()

    return row, col


def check_for_winning_move(board, board_copy, player):
    """Checks if the next move leads to victory.
    Returns a list of winning moves for the player and list of all possible moves"""
    winning_moves = []
    possible_moves = []
    for row in range(board_dim):
        for col in range(board_dim):
            if not is_this_place_occupied(board, row, col):
                mark(board_copy, player, row, col)
                possible_moves.append([row, col])
                if has_won(board_copy, player):
                    winning_moves.append([row, col])
                board_copy = deepcopy(board)
    return winning_moves, possible_moves


def get_random_coordinate_from_list(some_list):
    """Returns random move from a list of moves."""
    r = randrange(len(some_list))
    row = some_list[r][0]
    col = some_list[r][1]
    return row, col


def get_super_ai_move(board, player, ai_player):
    """Returns the coordinates of a valid move for Smarter-AI."""
    center = board[1][1]
    corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
    walls = [[0, 1], [1, 0], [1, 2], [2, 1]]
    board_copy = deepcopy(board)  # copy by val
    winning_ai_moves, possible_moves = check_for_winning_move(board, board_copy, ai_player)
    winning_player_moves, possible_moves = check_for_winning_move(board, board_copy, player)

    if len(winning_ai_moves) > 0:  # go for a win
        row, col = get_random_coordinate_from_list(winning_ai_moves)
    elif len(winning_player_moves) > 0:  # bloc a win
        row, col = get_random_coordinate_from_list(winning_player_moves)
    elif default_empty_field == center:  # go to center
        row, col = 1, 1
    elif (board[0][0] == player and board[2][2] == player) or (
            board[0][2] == player and board[2][0] == player):  # go for wall to block player
        row, col = get_random_coordinate_from_list(walls)
        while is_this_place_occupied(board, row, col):
            row, col = get_random_coordinate_from_list(walls)
    elif default_empty_field != center:  # or go to free corner
        row, col = get_random_coordinate_from_list(corners)
        while is_this_place_occupied(board, row, col):
            row, col = get_random_coordinate_from_list(corners)
    else:  # do other move
        row, col = get_random_coordinate_from_list(possible_moves)

    return row, col


def do_complete_ai_move(board, player, row, col):
    '''Does a compleate move for AI with time delay'''
    time.sleep(move_time)
    mark(board, player, row, col)
    print_board(board)


# TICTACTOE = HUMAN-HUMAN
def tictactoe_game_hum_hum():
    game_status = "playing"
    player = "x"
    board = init_board()
    print_board(board)

    while game_status == "playing":

        row, col = get_move(board, player)
        mark(board, player, row, col)
        print_board(board)

        if has_won(board, player):
            print_result(player)
            break
        if full_board_check(board):
            print(tie)
            break

        player = next_player(player)


# TICTACTOE = HUMAN-AI
def tictactoe_game_hum_ai(game_mode):
    player = "x"
    ai_player = "o"
    board = init_board()
    print_board(board)

    while True:
        row, col = get_move(board, player)
        mark(board, player, row, col)
        print_board(board)
        if has_won(board, player):
            print_result(player)
            break

        if full_board_check(board):
            print(tie)
            break

        if game_mode == "2":
            row, col = get_random_ai_move(board)
        if game_mode == "3":
            row, col = get_super_ai_move(board, player, ai_player)
        mark(board, ai_player, row, col)
        print_board(board)
        if has_won(board, ai_player):
            print_result(ai_player)
            break


# TICTACTOE = RANDOM-SUPER_AI
def tictactoe_game_rand_superai(game_mode):
    ai_random = "x"
    ai_super = "o"
    board = init_board()
    print_board(board)

    while True:
        row, col = get_random_ai_move(board)
        do_complete_ai_move(board, ai_random, row, col)
        if has_won(board, ai_random):
            time.sleep(move_time)
            print_result(ai_random)
            break

        if full_board_check(board):
            print(tie)
            break

        # RANDOM vs RANDOM:
        # row, col = get_random_ai_move(board)
        # do_complete_ai_move(board, ai_super, row, col)
        # if has_won(board, ai_super):
        #     time.sleep(move_time)
        #     print_result(ai_super)
        #     break

        row, col = get_super_ai_move(board, ai_random, ai_super)
        do_complete_ai_move(board, ai_super, row, col)
        if has_won(board, ai_super):
            time.sleep(move_time)
            print_result(ai_super)
            break


# MAIN MENU
def main_menu():
    game_mode = ""
    game_modes = ['1', '2', '3', '4', 'quit']
    while True:
        print("Choose your opponent:")
        print("Enter 1 for human oponent")
        print("Enter 2 for beatable AI")
        print("Enter 3 for unbeatable AI")
        print("Enter 4 for random AI vs unbeatable AI")
        print("Type \"quit\" to exit game")
        while game_mode not in game_modes:
            game_mode = input()

        if game_mode == '1':
            tictactoe_game_hum_hum()
            game_mode = clear_game_mode()
        if game_mode == '2':
            tictactoe_game_hum_ai(game_mode)
            game_mode = clear_game_mode()
        if game_mode == '3':
            tictactoe_game_hum_ai(game_mode)
            game_mode = clear_game_mode()
        if game_mode == "4":
            tictactoe_game_rand_superai(game_mode)
            game_mode = clear_game_mode()
        if game_mode == 'quit':
            sys.exit(0)


def clear_game_mode():
    return ''


# SETUP
if __name__ == '__main__':
    main_menu()
