from display import annouce_the_winner

board = [[1, 2, 3], [4, 4, 4], [7, 8, 1]] 

def check_columns_and_rows(board):
    for i in range(len(board)):
        row = board[i]
        column = [row[i] for row in board]
        if row[1:] == row[:-1]:
            return(row[0]) 
        if column [1:] == column[:-1]:
            return(column[0])
    return False
        
        
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
    else:
        return False

def is_game_over():
    if check_diags(board) or check_columns_and_rows(board):
        return True
    else:
        return False

if is_game_over():
    X_or_O = check_diags(board) or check_columns_and_rows(board)
    annouce_the_winner(X_or_O)

