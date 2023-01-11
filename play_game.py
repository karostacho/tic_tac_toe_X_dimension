from board_creation import create_the_board, create_list_of_numbers, create_board
from player_move import  make_user_move
from display import print_board, annouce_the_winner, annouce_the_draw, mark_move_on_the_board
from check_for_winner import check_diags, check_columns_and_rows, is_game_over, is_draw
from computer_move import make_smart_move


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


def play2():
    board = create_board(3)
    numbers = create_list_of_numbers(board)
    while not is_game_over(board, numbers) and not is_draw(board, numbers):
        computer_move_X = make_smart_move(board, numbers)
        mark_move_on_the_board(board, computer_move_X, "X")
        if is_game_over(board,numbers) or is_draw(board,numbers):
            break
        else:
            computer_move_O = make_smart_move(board, numbers)
            mark_move_on_the_board(board, computer_move_O, "O")
    if is_draw(board, numbers) == True:
        results.append('draw')
    else:
        X_or_O = check_diags(board) or check_columns_and_rows(board)
        results.append(X_or_O)


results = []
for x in range(10):
    play()
if ("X" in results):
    print("X was found.")
if ("O" in results):
    print("X was found.")
if ("X" not in results):
    print("X was not found.")
if ("O" not in results):
    print("O was not found.")
