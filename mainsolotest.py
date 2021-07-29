#importações necessárias
import pygame
from pygame.constants import KEYDOWN, KEYUP, QUIT

#início do pygame
pygame.init()


#definição da tamanho da janela e título
window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Ponggg!!!")


#definição da imagem do campo
field = pygame.image.load('pygame/assets/field.png')

#definição da imagem do player1, localização e movimentos
player1 = pygame.image.load('pygame/assets/player1.png')
player1_y = 310
player1_moveup = False
player1_movedown = False

#definição da imagem do player2, localização e movimentos
player2 = pygame.image.load('pygame/assets/player2.png')
player2_y = 310
player2_moveup = False
player2_movedown = False

#definição da imagem da bola, e localização
ball = pygame.image.load('pygame/assets/ball.png')
ball_x = 617
ball_y = 337


#definição do movimento dos jogadores
def move_player():
    
    #serve para chamar uma variável de fora da função para dentro
    global player1_y
    global player2_y

    #definição dos píxeis para cada comando do player1
    if player1_moveup:
        player1_y -= 10
    else:
        player1_y += 0


    if player1_movedown:
        player1_y += 10
    else:
        player1_y -= 0


    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

    #player 2 moves:

    #definição dos píxeis para cada comando do player2
    if player2_moveup:
        player2_y -= 10
    else:
        player2_y += 0


    if player2_movedown:
        player2_y += 10
    else:
        player2_y -= 0


    if player2_y <= 0:
        player2_y = 0
    elif player2_y >= 575:
        player2_y = 575


#definição do movimento da bola
def move_ball():
    global ball_x
    global ball_y

    ball_x += 8


    
#função para a implementação das imagens
def draw():
    window.blit(field, (0, 0))
    window.blit(player1, (50, player1_y))
    window.blit(player2, (1150, player2_y))
    window.blit(ball, (ball_x, ball_y))


#loop para não deixar o pygame.display fechar e aplicar os eventos enquanto rodando 
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        
        #definições para teclas apertadas do player1
        if events.type == KEYDOWN:
            if events.key == pygame.K_w:
                player1_moveup = True
            if events.key == pygame.K_s:
                player1_movedown = True

        #definições para teclas soltas do player1
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_moveup = False
            if events.key == pygame.K_s:
                player1_movedown = False

        #definições para teclas apertadas do player2
        if events.type == KEYDOWN:
            if events.key == pygame.K_UP:
                player2_moveup = True
            if events.key == pygame.K_DOWN:
                player2_movedown = True

        #definições para teclas soltas do player2
        if events.type == KEYUP:
            if events.key == pygame.K_UP:
                player2_moveup = False
            if events.key == pygame.K_DOWN:
                player2_movedown = False


    #chamada das funções para o loop
    draw()
    move_ball()
    move_player()
    pygame.display.update()