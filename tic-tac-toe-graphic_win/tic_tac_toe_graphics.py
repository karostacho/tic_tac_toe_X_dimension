import os
import pygame
from pygame.locals import RLEACCEL
from tic_tac_toe import *

# INITIALIZATION
pygame.init()

# SCREEN AND DISPLAY
board_size = 600
fundamental_unit = int(board_size / 12)
margin = 75
screen = pygame.display.set_mode([board_size, board_size])
back_graphics_2 = pygame.image.load(os.path.join('tic-tac-toe-graphic_win/images/background_2.png'))
back_graphics_1 = pygame.image.load(os.path.join('tic-tac-toe-graphic_win/images/background_1.png'))
back_graphics_0 = pygame.image.load(os.path.join('tic-tac-toe-graphic_win/images/background_0.png'))
x_graph = (board_size - back_graphics_2.get_rect().width) / 2
y_graph = (board_size - back_graphics_2.get_rect().height) / 2

# TEXT
size = 72
shift = 50
congratulations = "You won player {} !"
tie = "It is a tie :-)"
display_time = 3

# PLAYER COLORS
player = "x"
ai_random_o = "o"
ai_random_x = "x"
ai_super = "o"
p1_x = pygame.image.load(os.path.join("tic-tac-toe-graphic_win/images/player_x.png")).convert()
p1_x.set_colorkey((255, 255, 255), RLEACCEL)
p2_o = pygame.image.load(os.path.join("tic-tac-toe-graphic_win/images/player_o.png")).convert()
p2_o.set_colorkey((255, 255, 255), RLEACCEL)

# BOARD
board = init_board()


# HELPER METHODS
def print_graphic_board(board, player_1, player_2):
    for row in range(board_dim):
        for col in range(board_dim):
            row_g = (row + 1) * (fundamental_unit * 3) - margin
            col_g = (col + 1) * (fundamental_unit * 3) - margin
            if board[row][col] == player_1:
                screen.blit(p1_x, (row_g, col_g))
            elif board[row][col] == player_2:
                screen.blit(p2_o, (row_g, col_g))


def display_board():
    screen.blit(back_graphics_1, (x_graph, y_graph))
    print_graphic_board(board, ai_random_x, ai_super)
    pygame.display.flip()


def set_mode(status):
    global game_status, board, player
    game_status = status
    board = init_board()
    player = "x"


def write(text, size, winner):
    font = pygame.font.SysFont("Ink Free", size)
    sentence = font.render(text.format(winner.upper()), 1, (173, 35, 171))
    x_text = (board_size - sentence.get_rect().width) / 2
    y_text = (board_size - sentence.get_rect().height) / 2 - shift
    screen.blit(back_graphics_0, (x_graph, y_graph))
    screen.blit(sentence, (x_text, y_text))
    pygame.display.flip()
    time.sleep(display_time)


# MAIN GAME
game_status = "menu"
pos = [-1, -1]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                set_mode("human-human")
            if event.key == pygame.K_2:
                set_mode("human-random")
            if event.key == pygame.K_3:
                set_mode("human-superai")
            if event.key == pygame.K_4:
                set_mode("ai-ai")
            if event.key == pygame.K_ESCAPE:
                set_mode("menu")

        if event.type == pygame.MOUSEBUTTONDOWN and game_status == "human-human":
            pos[0] = pygame.mouse.get_pos()[0] // (board_size // 3)
            pos[1] = pygame.mouse.get_pos()[1] // (board_size // 3)

            if is_this_place_occupied(board, pos[0], pos[1]):
                pass
            else:
                mark(board, player, pos[0], pos[1])
                print_graphic_board(board, ai_random_x, ai_super)
                if has_won(board, player):
                    pygame.display.flip()
                    time.sleep(move_time)
                    game_status = "menu"
                    write(congratulations, size, player)
                elif full_board_check(board):
                    game_status = "menu"
                    write(tie, size, player)
                player = next_player(player)

        if event.type == pygame.MOUSEBUTTONDOWN and game_status == "human-random":
            pos[0] = pygame.mouse.get_pos()[0] // (board_size // 3)
            pos[1] = pygame.mouse.get_pos()[1] // (board_size // 3)

            if is_this_place_occupied(board, pos[0], pos[1]):
                pass
            else:
                mark(board, player, pos[0], pos[1])
                print_graphic_board(board, ai_random_x, ai_super)
                if has_won(board, player):
                    pygame.display.flip()
                    time.sleep(move_time)
                    game_status = "menu"
                    write(congratulations, size, player)
                if full_board_check(board):
                    pygame.display.flip()
                    game_status = "menu"
                    write(tie, size, player)
                else:
                    row, col = get_random_ai_move(board)
                    mark(board, ai_random_o, row, col)
                    print_graphic_board(board, ai_random_x, ai_super)
                    if has_won(board, ai_random_o):
                        pygame.display.flip()
                        time.sleep(move_time)
                        game_status = "menu"
                        write(congratulations, size, ai_random_o)
                    if full_board_check(board):
                        pygame.display.flip()
                        game_status = "menu"
                        write(tie, size, player)

        if event.type == pygame.MOUSEBUTTONDOWN and game_status == "human-superai":
            pos[0] = pygame.mouse.get_pos()[0] // (board_size // 3)
            pos[1] = pygame.mouse.get_pos()[1] // (board_size // 3)
            if is_this_place_occupied(board, pos[0], pos[1]):
                pass
            else:
                mark(board, player, pos[0], pos[1])
                print_graphic_board(board, ai_random_x, ai_super)

                if has_won(board, player):
                    pygame.display.flip()
                    time.sleep(move_time)
                    game_status = "menu"
                    write(congratulations, size, player)
                if full_board_check(board):
                    pygame.display.flip()
                    game_status = "menu"
                    write(tie, size, player)
                else:
                    row, col = get_super_ai_move(board, player, ai_super)
                    mark(board, ai_super, row, col)
                    print_graphic_board(board, ai_random_x, ai_super)
                    if has_won(board, ai_super):
                        pygame.display.flip()
                        time.sleep(move_time)
                        game_status = "menu"
                        write(congratulations, size, ai_super)
                    if full_board_check(board):
                        pygame.display.flip()
                        game_status = "menu"
                        write(tie, size, player)

    if game_status == "menu":
        screen.blit(back_graphics_2, (x_graph, y_graph))
        pygame.display.flip()

    elif game_status == "human-human":
        display_board()

    elif game_status == "human-random":
        display_board()

    elif game_status == "human-superai":
        display_board()

    elif game_status == "ai-ai":
        screen.blit(back_graphics_1, (x_graph, y_graph))

        row, col = get_random_ai_move(board)
        mark(board, ai_random_x, row, col)
        time.sleep(move_time)
        print_graphic_board(board, ai_random_x, ai_super)
        if has_won(board, ai_random_x):
            pygame.display.flip()
            time.sleep(move_time)
            game_status = "menu"
            write(congratulations, size, ai_random_x)
        pygame.display.flip()

        if full_board_check(board):
            game_status = "menu"
            board = init_board()
            write(tie, size, player)

        row, col = get_super_ai_move(board, ai_random_x, ai_super)
        mark(board, ai_super, row, col)
        time.sleep(move_time)
        print_graphic_board(board, ai_random_x, ai_super)
        if has_won(board, ai_super):
            pygame.display.flip()
            time.sleep(move_time)
            game_status = "menu"
            write(congratulations, size, ai_super)
        pygame.display.flip()
