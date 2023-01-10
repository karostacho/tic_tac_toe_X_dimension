from board_creation import create_list_of_numbers

def is_game_over(board, numbers):
    if check_diags(board) or check_columns_and_rows(board):
        return True
    if is_draw(board, numbers) == True:
        return True
    else:
        return False   

def is_draw(board, numbers):
    list_of_boxes = create_list_of_numbers(board)
    if not any(item in numbers for item in list_of_boxes) and not check_diags(board) and not check_columns_and_rows(board) :
        return True
    else:
        return False

def check_columns_and_rows(board):
    for i in range(len(board)):
        row = board[i]
        if row[1:] == row[:-1]:
            return (row[0])
        column = [row[i] for row in board]
        if column [1:] == column[:-1]:
            return (column[0]) 
         
def find_diag1(board):
    diag_1 = []
    for i in range(len(board)):
        diag_1.append(board[i][i])
    return diag_1

def find_diag2(board):
    diag_2 = []
    for i in range(len(board)):
        diag_2.append(board[i][(len(board)-1)-i])
    return diag_2

def check_diags(board):
    diag_1 = find_diag1(board)
    if diag_1[1:] == diag_1[:-1]:
        return (diag_1[0])
    diag_2 = find_diag2(board)
    if diag_2[1:] == diag_2[:-1]:
        return (diag_2[0])
    


