from display import annouce_the_winner



def create_the_board(board_size):
    x = int(board_size)
    create_list_of_numbers(x)
    board = []
    for i in range(x):
        row = []
        for j in range(x):
            row.append((((j+1)+(x*i))))
        board.append(row)
    
    print(board)

def create_list_of_numbers(x):
    numbers = []
    for i in range(x*x):
        numbers.append(i+1)
    print(numbers)


create_the_board()
