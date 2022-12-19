from tabulate import tabulate
def print_board(board):
    print(tabulate(board, tablefmt='simple_grid'))


