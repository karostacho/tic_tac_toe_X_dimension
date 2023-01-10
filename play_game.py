from board_creation import create_the_board, create_list_of_numbers
from player_move import mark_move_on_the_board, make_user_move, make_computer_move
from display import print_board, annouce_the_winner, annouce_the_draw
from check_for_winner import check_diags, check_columns_and_rows, is_game_over, is_draw  
from smart_computer import make_smart_move

def play():
    board = create_the_board()
    numbers = create_list_of_numbers(board)
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


play()



    