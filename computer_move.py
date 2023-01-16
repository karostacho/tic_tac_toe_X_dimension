import random
from board import is_box_taken, find_board_size
from board import find_lines_on_board, find_diag1
from player_move import user_mark

computer_mark = "O"

def take_available_box(line):
    for item in line:
        if str(item).isdigit():
            return item

def is_line_need_to_be_blocked(line, move, board):
    board_size = find_board_size(board)
    if line.count(move) == board_size-1 and any(str(item).isdigit() for item in line):
        return True

def is_player_move_in_line(line, user_move, computer_move):
    if line.count(computer_move) == 1 and line.count(user_move) == 0:
        return True
    if line.count(user_move) == 1 and line.count(computer_move) == 0:
        return True
   
def two_moves_in_the_same_line(board, move_x_or_o, list_of_lines):
    for line in list_of_lines:
        if is_line_need_to_be_blocked(line, move_x_or_o, board):
            return take_available_box(line)
        
def make_move_in_the_same_line(user_move, list_of_lines, computer_move):
    for line in list_of_lines:
        if is_player_move_in_line(line, user_move, computer_move):
            return take_available_box(line)

def make_random_computer_move(numbers, board):
    computer_move = random.choice(numbers)
    if is_box_taken(board, computer_move):
        return make_random_computer_move(numbers, board)
    else: 
        return computer_move

def take_center_number(board):
    board_size = find_board_size(board)
    diag_1 = find_diag1(board)
    center_number = diag_1[((board_size + 1) // 2) - 1]
    if center_number == user_mark or center_number == computer_mark:
        return False
    return center_number

def make_smart_move(board, numbers):
    list_of_lines = find_lines_on_board(board)
    if not two_moves_in_the_same_line(board, computer_mark, list_of_lines):
        computer_move = two_moves_in_the_same_line(board, user_mark, list_of_lines) or take_center_number(board) or make_move_in_the_same_line(user_mark, list_of_lines, computer_mark) or make_random_computer_move(numbers, board)
        return computer_move
    else:
        computer_move = two_moves_in_the_same_line(board, computer_mark, list_of_lines)
        return computer_move
