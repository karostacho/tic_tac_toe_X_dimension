from display import print_board, ask_for_move, inform_the_box_is_taken, inform_the_move_is_impossible
import random

def is_box_taken(board, move):
    for row in board:
        if move in row:
            return False
    return True

def make_user_move(board, numbers):
    user_move = ask_for_move()
    if not user_move.isdigit():
        inform_the_move_is_impossible(user_move)
        print_board(board)
        return make_user_move(board,numbers)
    user_move = int(user_move)
    if user_move not in numbers:
        inform_the_move_is_impossible(user_move)
        print_board()
        return make_user_move(board,numbers)
    repeated_move = is_box_taken(board, user_move)
    if repeated_move:
        inform_the_box_is_taken(user_move)
        print_board(board)
        return make_user_move(board,numbers)
    else:
        return user_move
    
def make_computer_move(numbers, board):
    computer_move = random.choice(numbers)
    repeated_move = is_box_taken(board, computer_move)
    if repeated_move:
        return make_computer_move(numbers, board)
    else: 
        return computer_move

def mark_move_on_the_board(board, move, X_or_O):
    for row in board:
        if move in row:
            x = int(board.index(row)) 
            y = int(row.index(move))
            board[x][y] = X_or_O
            print_board(board)


           
    
