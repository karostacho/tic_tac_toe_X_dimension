from display import annouce_the_draw

def is_game_over(board, numbers):
    if check_diags(board) or check_columns_and_rows(board):
        return True
    if is_draw(board, numbers) == True:
        return True
    else:
        return False   

def is_draw(board, numbers):
    list_of_boxes = sum(board,[])
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
         
def check_diags(board):
    diag_1 = []
    diag_2 = []
    for i in range(len(board)):
        diag_1.append(board[i][i])
        diag_2.append(board[i][(len(board)-1)-i])
    if diag_1[1:] == diag_1[:-1]:
        return (diag_1[0])
    if diag_2[1:] == diag_2[:-1]:
        return (diag_2[0])
    


