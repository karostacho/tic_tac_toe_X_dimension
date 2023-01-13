from display import print_board, ask_for_move, inform_the_box_is_taken, inform_the_move_is_impossible
from board import is_box_taken

user_mark = "X"

def make_user_move(board, numbers):
    user_move = ask_for_move()
    if not user_move.isdigit():
        alert_user(user_move, board)
        return make_user_move(board, numbers)
    user_move = int(user_move)
    if user_move not in numbers:
        alert_user(user_move, board)
        return make_user_move(board, numbers)
    if is_box_taken(board, user_move):
        inform_the_box_is_taken(user_move)
        print_board(board)
        return make_user_move(board, numbers)
    else:
        return user_move

def alert_user(user_move, board):
    inform_the_move_is_impossible(user_move)
    print_board(board)
