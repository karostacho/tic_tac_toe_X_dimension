def find_board_size(board):
    return len(board)

def is_box_taken(board, move):
    for row in board:
        if move in row:
            return False
    return True

def find_diag1(board):
    diag_1 = []
    board_size = find_board_size(board)
    for i in range(board_size):
        diag_1.append(board[i][i])
    return diag_1

def find_diag2(board):
    diag_2 = []
    board_size = find_board_size(board)
    for i in range(board_size):
        diag_2.append(board[i][(len(board)-1)-i])
    return diag_2

def create_the_board(board_size):
    board = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append((j+1)+(board_size*i))
        board.append(row)
    return board

def create_list_of_items_in(board):
    items = []
    for row in board:
        for item in row:
            items.append(item)
    return items

def find_lines_on_board(board):
    list_of_lines = []
    diag_1 = find_diag1(board)
    list_of_lines.append(diag_1)
    diag_2 = find_diag2(board)
    list_of_lines.append(diag_2)
    board_size = find_board_size(board)
    for i in range(board_size):
        row = board[i]
        list_of_lines.append(row)
        column = [row[i] for row in board]
        list_of_lines.append(column)
    return list_of_lines

def mark_move_on_the_board(board, move, move_X_or_O):
    for row in board:
        if move in row:
            x = int(board.index(row)) 
            y = int(row.index(move))
            board[x][y] = move_X_or_O
            return move_X_or_O
            