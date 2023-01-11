import pygame

pygame.init()
board_size = 600
screen = pygame.display.set_mode([board_size, board_size])


def Napisz2(tekst, rozmiar, xTekst, yTekst):
    czcionka = pygame.font.SysFont("Arial", rozmiar)
    napis = czcionka.render(tekst, 1, (235, 52, 52))
    screen.blit(napis, (xTekst, yTekst))


pos = [0, 0]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos[0] = pygame.mouse.get_pos()[0]
            pos[1] = pygame.mouse.get_pos()[1]

    screen.fill((255, 255, 255))
    Napisz2("xxxxxxxx", 20, 100, 100)
    Napisz2("PosX: " + str(pos[0]) + "   PosY: " + str(pos[1]), 20, 50, 50)
    pygame.display.flip()
