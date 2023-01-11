import random
from board import is_box_taken, find_board_size
from board import  find_lines_on_board

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
   
def two_moves_in_line(board, numbers, move_x_or_o, list_of_lines):
    for line in list_of_lines:
        if is_line_need_to_be_blocked(line, move_x_or_o, numbers, board):
            return take_available_box(line, numbers)
        
def make_move_in_the_same_line( numbers, move_x_or_o, list_of_lines):
    for line in list_of_lines:
        if is_player_move_in_line(line, move_x_or_o, numbers):
            return take_available_box(line, numbers)

def make_random_computer_move(numbers, board):
    computer_move = random.choice(numbers)
    repeated_move = is_box_taken(board, computer_move)
    if repeated_move:
        return make_random_computer_move(numbers, board)
    else: 
        return computer_move

def make_smart_move(board, numbers):
    list_of_lines = find_lines_on_board(board)
    if not two_moves_in_line(board, numbers, "O", list_of_lines):
        computer_move = two_moves_in_line(board, numbers, "X", list_of_lines) or make_move_in_the_same_line( numbers, "X", list_of_lines) or make_random_computer_move(numbers, board)
        return computer_move
    else:
        computer_move = two_moves_in_line(board, numbers, "O", list_of_lines)
        return computer_move