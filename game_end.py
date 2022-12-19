def annouce_the_winner(X_or_O):
    print(f"The winner is Player '{X_or_O}'")

def find_the_winner(board, X_or_O):
    if X_or_O == board[0][0] == board[0][1] == board[0][2]:
        return X_or_O 
    if X_or_O == board[1][0] == board[1][1] == board[1][2]:
        return X_or_O 
    if X_or_O == board[2][0] == board[2][1] == board[2][2]:
       return X_or_O 
    if X_or_O == board[0][0] == board[1][0] == board[2][0]:
        return X_or_O 
    if X_or_O == board[0][1] == board[1][1] == board[2][1]:
        return X_or_O 
    if X_or_O == board[0][2] == board[1][2] == board[2][2]:
        return X_or_O 
    if X_or_O == board[0][0] == board[1][1] == board[2][2]:
        return X_or_O 
    if X_or_O == board[0][2] == board[1][1] == board[2][0]:
        return X_or_O
    else:
        return True

def is_game_over(board, X_or_O, move = True):
    if X_or_O == board[0][0] == board[0][1] == board[0][2]:
        return move
    elif X_or_O == board[1][0] == board[1][1] == board[1][2]:
        return move
    elif X_or_O == board[2][0] == board[2][1] == board[2][2]:
        return move
    elif X_or_O == board[0][0] == board[1][0] == board[2][0]:
        return move
    elif X_or_O == board[0][1] == board[1][1] == board[2][1]:
        return move
    elif X_or_O == board[0][2] == board[1][2] == board[2][2]:
        return move
    elif X_or_O == board[0][0] == board[1][1] == board[2][2]:
        return move
    elif X_or_O == board[0][2] == board[1][1] == board[2][0]:
        return move
    else:
        return False

    