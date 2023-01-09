from display import ask_for_size_of_board

def create_the_board():
    board_size = int(ask_for_size_of_board())
    board = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append((((j+1)+(board_size*i))))
        board.append(row)
    return board
    

def create_list_of_numbers(board):
    numbers = sum(board,[])
    return numbers