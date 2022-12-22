from player_move import mark_move_on_the_board, make_user_move, make_computer_move
from display_board import print_board
from game_end import is_game_over, annouce_the_winner


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numbers = [1,2,3,4,5,6,7,8,9]

while not is_game_over(board, "X") and not is_game_over(board, "O") :
    print_board(board)
    user_move = make_user_move(board)
    mark_move_on_the_board(board, user_move, "X")
    if is_game_over(board, "X") or is_game_over(board, "O"):
        break
    else:
        computer_move = make_computer_move(numbers,board)
        mark_move_on_the_board(board, computer_move, "O")
X_or_O = is_game_over(board, "X", "X") or is_game_over(board, "O", "O")
annouce_the_winner(X_or_O)





    