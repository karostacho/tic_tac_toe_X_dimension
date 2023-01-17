from tabulate import tabulate

def print_board(board):
    print(tabulate(board, tablefmt='simple_grid'))

def annouce_the_winner(X_or_O):
    print(f"Game over. The winner is Player '{X_or_O}'!")

def annouce_the_draw():
    print(f"Game over. It's a draw.")

def ask_for_move():
    return input("What's your move? ")

def inform_the_box_is_taken(user_move):
    print (f"Box {user_move} is already taken. Please select an available box.")

def inform_the_move_is_impossible(user_move):
    print (f"There is no such a box: '{user_move}'. Please select an available box.")

def ask_for_size_of_board():
    board_size = input("Please specify the size of your board. How many rows/columns would you like to have? ")
    if not board_size.isdigit():
        inform_size_of_board_must_be_integer_greater_than_2()
        return ask_for_size_of_board()
    board_size = int(board_size)
    if board_size <= 2:
        inform_size_of_board_must_be_integer_greater_than_2()
        return ask_for_size_of_board()
    else :
        return board_size

def inform_size_of_board_must_be_integer_greater_than_2():
    print("Please provide an integer greater than 2")
