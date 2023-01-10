import random
from player_move import is_box_taken
from check_for_winner import find_diag1, find_diag2


def find_board_size(board):
    board_size = len(board)
    return board_size

def make_random_computer_move(numbers, board):
    computer_move = random.choice(numbers)
    repeated_move = is_box_taken(board, computer_move)
    if repeated_move:
        return make_random_computer_move(numbers, board)
    else: 
        return computer_move

def take_available_box(line, numbers):
    for item in line:
        if item in numbers:
            return item

def is_line_need_to_be_blocked(line, move, numbers, board):
    board_size = find_board_size(board)
    if line.count(move) == board_size-1 and any(item in numbers for item in line):
        return True

def is_player_move_in_line(line, move, numbers):
    if line.count(move) == 1 and any(item in numbers for item in line):
        return True

def two_moves_in_diag(board, numbers, XorO):
    move = XorO
    diag_1 = find_diag1(board)
    diag_2 = find_diag2(board)
    if is_line_need_to_be_blocked(diag_1, move, numbers, board) == True:
        return take_available_box(diag_1, numbers)
    if is_line_need_to_be_blocked(diag_2, move, numbers, board) == True:
        return take_available_box(diag_2, numbers)
    
def two_moves_in_row_or_column(board, numbers, XorO):
    move = XorO
    for i in range(len(board)):
        row = board[i]
        if is_line_need_to_be_blocked(row, move, numbers, board) == True:
            return take_available_box(row, numbers)
        column = [row[i] for row in board]
        if is_line_need_to_be_blocked(column, move, numbers, board) == True:
            return take_available_box(column, numbers)

def make_move_in_the_same_row_or_column(board, numbers, XorO):
    move = XorO
    for i in range(len(board)):
        row = board[i]
        if is_player_move_in_line(row, move, numbers) ==  True:
            return take_available_box(row, numbers)
        column = [row[i] for row in board]
        if is_player_move_in_line(column, move, numbers) == True:
            return take_available_box(column, numbers)

def make_move_in_the_same_diag(board, numbers, XorO):
    move = XorO
    diag_1 = find_diag1(board)
    diag_2 = find_diag2(board)
    if is_player_move_in_line(diag_1, move, numbers) == True:
        return take_available_box(diag_1, numbers)
    if is_player_move_in_line(diag_2, move, numbers) == True:
        return take_available_box(diag_2, numbers)

def make_smart_move(board, numbers):
    while not two_moves_in_diag(board, numbers, "O") and not two_moves_in_row_or_column(board, numbers, "O"):
        computer_move = two_moves_in_diag(board, numbers, "X") or two_moves_in_row_or_column(board, numbers, "X") or make_move_in_the_same_diag(board, numbers, "X") or make_move_in_the_same_row_or_column(board, numbers, "X") or make_random_computer_move(numbers, board)
        return computer_move
    computer_move = two_moves_in_diag(board, numbers, "O") or two_moves_in_row_or_column(board, numbers, "O")
    return computer_move



