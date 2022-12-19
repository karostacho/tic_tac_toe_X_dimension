from display_board import print_board
import random

def make_user_move(board):
    user_move = input("What's your move?")
    user_move = int(user_move)
    repeated_move = is_box_taken(board, user_move)
    if repeated_move == False:
        return user_move
    else:
        print(f"Box {user_move} is already taken, please select another box")
        return make_user_move(board)
    
def make_computer_move(numbers):
    computer_move = random.choice(numbers)
    return computer_move

def play(board, move, X_or_O):
    for row in board:
        if move in row:
            x = int(board.index(row)) 
            y = int(row.index(move))
            board[x][y] = X_or_O
            print_board(board)

def is_box_taken(board, move):
    for row in board:
        if move in row:
            return False
    return True
        
            
#print(f"Box {move} is already taken, please select another box")    

def computer_plays(board, move, X_or_O):
    for row in board:
        if move in row:
            x = int(board.index(row)) 
            y = int(row.index(move))
            board[x][y] = X_or_O
            print_board(board)
    
