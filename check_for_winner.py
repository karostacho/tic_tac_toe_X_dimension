from board import create_list_of_items_in, find_lines_on_board

def is_game_over(board):
    if get_winner_if_line_full(board) or is_draw(board):
        return True
    else:
        return False   

def is_draw(board):
    list_of_items = create_list_of_items_in(board)
    return not any(str(item).isdigit() for item in list_of_items)

def get_winner_if_line_full(board):
    list_of_lines = find_lines_on_board(board)
    for line in list_of_lines:
        if line[1:] == line[:-1]:
            return line[0]
