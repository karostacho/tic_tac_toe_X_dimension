from player_move import play, make_user_move, make_computer_move, is_box_taken
from display_board import print_board
from game_end import is_game_over, annouce_the_winner


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numbers = [1,2,3,4,5,6,7,8,9]

while not is_game_over(board, "X") or is_game_over(board, "O") :
    print_board(board)
    user_move = make_user_move(board)
    play(board, user_move, "X")
    if is_game_over(board, "X") or is_game_over(board, "O"):
        break
    else:
        user_move2 = make_user_move(board)
        play(board, user_move2, "O")
        #computer_move = make_computer_move(numbers)
        #play(board, computer_move, "O")
X_or_O = is_game_over(board, "X", "X") or is_game_over(board, "O", "O")
annouce_the_winner(X_or_O)






    