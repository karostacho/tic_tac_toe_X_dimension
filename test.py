from board import create_the_board, create_list_of_items_in
from player_move import  make_user_move
from display import print_board, annouce_the_winner, annouce_the_draw, mark_move_on_the_board
from check_for_winner import check_diags, check_columns_and_rows, is_game_over, is_draw  
from computer_move import make_smart_move
from computer_move import find_board_size
def play():
    board = create_the_board()
    numbers = create_list_of_items_in(board)
    print_board(board)
    while not is_game_over(board, numbers) and not is_draw(board, numbers):
        user_move = make_user_move(board,numbers)
        mark_move_on_the_board(board, user_move, "X")
        if is_game_over(board,numbers) or is_draw(board,numbers):
            break
        else:
            computer_move = make_smart_move(board, numbers)
            mark_move_on_the_board(board, computer_move, "O")
    if is_draw(board, numbers) == True:
        annouce_the_draw()
    else:
        X_or_O = check_diags(board) or check_columns_and_rows(board)
        annouce_the_winner(X_or_O)
#play()

def is_line_need_to_be_blocked(line, move, numbers, board):
    board_size = find_board_size(board)
    if line.count(move) == board_size-1 and any(item in numbers for item in line):
        print("Ok")

board = [["X","X",3], ["X",5,6], [7,8,9]]
line = board[0]
move = "X"
numbers = [1,2,3,4,5,6,7,8,9]

def find_rows(board):
    for i in range(len(board)):
        row = board[i]
        print(row) 

find_rows(board)