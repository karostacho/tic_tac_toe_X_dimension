import random
from player_move import is_box_taken, make_computer_move

def check_if_computer_can_block(board):
    computer_move = block_move_in_row_and_column(board) or block_move_in_diag(board)
    return computer_move

def find_number_in_list(line, numbers):
    for item in line:
        if item in numbers:
            return item
    
def block_move_in_row_and_column(board, numbers):
    user_move = "X"
    for i in range(3):
        row = board[i]
        if two_boxes_taken_in_line(row, user_move, numbers) == True:
            return find_number_in_list(row, numbers)
        column = [row[i] for row in board]
        if two_boxes_taken_in_line(column, user_move, numbers) == True:
            return find_number_in_list(column, numbers)

def random_computer_choice(numbers):
    computer_move = random.choice(numbers)
    return computer_move

def two_boxes_taken_in_line(line, user_move, numbers):
    if line.count(user_move) == 2 and any(item in numbers for item in line):
        return True


def block_move_in_diag(board, numbers):
    user_move = "X"
    diag_1 = []
    diag_2 = []
    for i in range(3):
        diag_1.append(board[i][i])
        diag_2.append(board[i][(len(board)-1)-i])
    if two_boxes_taken_in_line(diag_1, user_move, numbers) == True:
        return find_number_in_list(diag_1, numbers)
    if two_boxes_taken_in_line(diag_2, user_move, numbers) == True:
        return find_number_in_list(diag_2, numbers)

def make_smart_move(board, numbers):
    computer_move = block_move_in_diag(board, numbers) or block_move_in_row_and_column(board, numbers) or make_computer_move(numbers, board)
    return computer_move
        



