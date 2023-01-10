from display import ask_for_size_of_board, inform_size_of_board_must_be_integer_greater_than_1

def create_the_board():
    board_size = ask_for_size_of_board()
    if not board_size.isdigit():
        inform_size_of_board_must_be_integer_greater_than_1()
        return create_the_board()
    board_size = int(board_size)
    if board_size <= 1:
        inform_size_of_board_must_be_integer_greater_than_1()
        return create_the_board()
    board = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append((((j+1)+(board_size*i))))
        board.append(row)
    return board

def create_list_of_numbers(board):
    numbers = []
    for row in board:
        for item in row:
            numbers.append(item)
    return numbers

