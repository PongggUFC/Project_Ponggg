#importações necessárias
import pygame
from pygame.constants import KEYDOWN, QUIT

#início do pygame
pygame.init()


#definição da tamanho da janela e título
window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Ponggg!!!")


#definição do campo, jogadores e a bola
field = pygame.image.load('pygame/assets/field.png')

player1 = pygame.image.load('pygame/assets/player1.png')
player1_y = 310

player2 = pygame.image.load('pygame/assets/player2.png')
player2_y = 310

ball = pygame.image.load('pygame/assets/ball.png')
ball_x = 617
ball_y = 337

def move_ball():
    global ball_x
    global ball_y

    ball_x += 8


    
#implementação das imagens
def draw():
    window.blit(field, (0, 0))
    window.blit(player1, (50, player1_y))
    window.blit(player2, (1150, player2_y))
    window.blit(ball, (ball_x, ball_y))


#loop para não deixar o pygame.display fechar 
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == KEYDOWN:
            if events.key == pygame.K_w:
                player1_y -= 10
            if events.key == pygame.K_s:
                player1_y += 10
            if events.key == pygame.K_UP:
                player2_y -= 10
            if events.key == pygame.K_DOWN:
                player2_y += 10

    draw()
    move_ball()
    pygame.display.update()