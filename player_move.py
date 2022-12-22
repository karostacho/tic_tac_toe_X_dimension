from display_board import print_board
import random

def is_box_taken(board, move):
    for row in board:
        if move in row:
            return False
    return True

def make_user_move(board):
    user_move = input("What's your move?")
    user_move = int(user_move)
    repeated_move = is_box_taken(board, user_move)
    if repeated_move == False:
        return user_move
    else:
        print(f"Box {user_move} is already taken, please select another box")
        return make_user_move(board)
    
def make_computer_move(numbers, board):
    computer_move = random.choice(numbers)
    repeated_move = is_box_taken(board, computer_move)
    if repeated_move == False:
        return computer_move
    else: 
        return make_computer_move(numbers, board)

def mark_move_on_the_board(board, move, X_or_O):
    for row in board:
        if move in row:
            x = int(board.index(row)) 
            y = int(row.index(move))
            board[x][y] = X_or_O
            print_board(board)


           
    
