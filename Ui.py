import pygame
import sys
import main

from pygame.locals import *

pygame.init()

Display = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Chess')


# Color setup
WHITE = (255, 255, 255)
BLACK = (10, 110, 50)
Green = (0, 150, 0)
BLUE = (0,0,225)

Background = pygame.image.load('Background.jpg')

board_length = 8
box_size = 80
cnt = 0
font = pygame.font.Font('freesansbold.ttf', 32)

#Black Pices

BlackPawn = pygame.image.load('BlackPawn.png')
BlackRook = pygame.image.load('BlackRook.png')
BlackBishop = pygame.image.load('BlackBishop.png')
BlackNight = pygame.image.load('BlackNight.png')
BlackKing = pygame.image.load('BlackKing.png')
BlackQueen = pygame.image.load('BlackQueen.png')

# White piecs

WhitePawn = pygame.image.load('WhitePawn.png')
WhiteRook = pygame.image.load('WhiteRook.png')
WhiteBishop = pygame.image.load('WhiteBishop.png')
WhiteNight = pygame.image.load('WhiteNight.png')
WhiteKing = pygame.image.load('WhiteKing.png')
WhiteQueen = pygame.image.load('WhiteQueen.png')
# Dot

Dot = pygame.image.load('dot.png')

Display.blit(pygame.transform.scale(Background,(800,800)) ,(0, 0))

xpos = [90, 170, 250, 330, 410, 490, 570, 650]
ypos = [650, 570, 490, 410, 330, 250, 170, 90]
# 8 , A = 90
# 7 , B = 170
# 6 , C = 250
# 5 , D = 330
# 4 , E = 410
# 3 , F = 490
# 2 , G = 570
# 1 , H = 650

def print_board():
    posy = 100
    posx = 110
    for y in range(8, 0, -1):
        Display.blit(font.render(str(y), True, (255, 255, 255)) , (45,posy))
        posy += 80
        for i, x in enumerate(main.rows):
            piece_found = False
            for piece in main.BOARD:
                if piece.position.x == x and piece.position.y == y:
                    index = main.rows.index(x)
                    piece_found = True
                    if piece.color == main.BLACK:
                        piece_found = True
                        if isinstance(piece, main.Pawn):
                            Display.blit(BlackPawn, (xpos[index], ypos[y -1]))
                        if isinstance(piece, main.Rook):
                            Display.blit(BlackRook, (xpos[index], ypos[y -1]))
                        if isinstance(piece, main.Bishop):
                            Display.blit(BlackBishop, (xpos[index], ypos[y -1]))
                        if isinstance(piece, main.Knight):
                            Display.blit(BlackNight, (xpos[index], ypos[y -1]))
                        if isinstance(piece, main.King):
                            Display.blit(BlackKing, (xpos[index], ypos[y -1]))
                        if isinstance(piece, main.Queen):
                            Display.blit(BlackQueen, (xpos[index], ypos[y -1]))
                    else:
                        if isinstance(piece, main.Pawn):
                            Display.blit(WhitePawn, (xpos[index], ypos[y -1]))
                        if isinstance(piece, main.Rook):
                            Display.blit(WhiteRook, (xpos[index], ypos[y -1]))
                        if isinstance(piece, main.Bishop):
                            Display.blit(WhiteBishop, (xpos[index], ypos[y -1]))
                        if isinstance(piece, main.Knight):
                            Display.blit(WhiteNight, (xpos[index], ypos[y -1]))
                        if isinstance(piece, main.King):
                            Display.blit(WhiteKing, (xpos[index], ypos[y -1]))
                        if isinstance(piece, main.Queen):
                            Display.blit(WhiteQueen, (xpos[index], ypos[y -1]))

    for i in range(len(main.rows)):
        Display.blit(font.render(main.rows[i], True, (255, 255, 255)) , (posx,730))
        posx += 80

def dot_print(x, y):
    Display.blit(Dot, (x, y))

for i in range(1, board_length + 1):
        for j in range(1, board_length + 1):
            if cnt % 2 == 0:
                pygame.draw.rect(Display, WHITE, [box_size*j, box_size*i, box_size, box_size])
            else:
                pygame.draw.rect(Display, BLACK, [box_size*j, box_size*i, box_size, box_size])
            cnt += 1
        cnt -= 1

pre_val_a , pre_val_b  = 0 , 0
while True:
    print_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        button_states = pygame.mouse.get_pressed()
        if button_states[0] == 1:
            a,b = pygame.mouse.get_pos()
            for i in range(1, board_length + 1):
                for j in range(1, board_length + 1):
                    if a > box_size * j and a < box_size * j + box_size and b > box_size * i and b < box_size + box_size * i:
                        #pygame.draw.rect(Display, BLUE, [box_size*j, box_size*i, box_size, box_size])
                        for k in range(0, len(xpos)):
                            if xpos[k] > box_size * j and xpos[k] < box_size * j + box_size:
                                for z in range(0 , len(ypos)):
                                    if ypos[z]  > box_size * i and ypos[z] < box_size + box_size * i:
                                        print(xpos[k] , ypos[z])
                                        if a != pre_val_a and b != pre_val_b:
                                            pre_val_a = a
                                            pre_val_b = b
                                            piece = main.get_piece(main.Postion(main.rows[k], z + 1))
                                            valid_moves = main.get_valid_moves(piece)
                                            for move in valid_moves:
                                                print(move.y)
                                                dot_print(xpos[main.rows.index(move.x)], ypos[move.y - 1])
                                
            
                                            


    pygame.display.update()
