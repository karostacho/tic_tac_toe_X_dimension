from board import create_the_board, create_list_of_items_in
from player_move import  make_user_move
from display import print_board, annouce_the_winner, annouce_the_draw, mark_move_on_the_board, ask_for_size_of_board
from check_for_winner import get_winner_if_line_full, is_game_over, is_draw  
from computer_move import make_smart_move

def play():
    board_size = ask_for_size_of_board()
    board = create_the_board(board_size)
    numbers = create_list_of_items_in(board)
    print_board(board)
    while not is_game_over(board):
        user_move = make_user_move(board,numbers)
        mark_move_on_the_board(board, user_move, "X")
        print_board(board)
        if is_game_over(board):
            break
        else:
            computer_move = make_smart_move(board, numbers)
            mark_move_on_the_board(board, computer_move, "O")
            print_board(board)
    if is_draw(board):
        annouce_the_draw()
    else:
        X_or_O = get_winner_if_line_full(board)
        annouce_the_winner(X_or_O)


play()



    